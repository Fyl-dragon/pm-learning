from __future__ import annotations

import time
from collections import Counter
from typing import Any, Callable, Dict, List, Optional


RunCase = Callable[[Dict[str, Any]], Dict[str, Any]]


class EvalHarness:
    """Repeatable evaluation harness for LLM gateway scenarios.

    The harness stays outside provider logic on purpose: it evaluates the
    whole environment around the model, including route strategy, prompt
    version, fallback behavior, cost and failure attribution.
    """

    def __init__(self, run_case: RunCase) -> None:
        self.run_case = run_case

    def run(self, app_id: str, cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        results = [self._run_one(app_id, case) for case in cases]
        passed = sum(1 for result in results if result["passed"])
        failed = len(results) - passed
        total_cost = sum(result["cost_usd"] for result in results)
        total_latency = sum(result["latency_ms"] for result in results)
        fallback_count = sum(result["fallback_count"] for result in results)
        failure_breakdown = Counter(
            result["failure_tag"] for result in results if result["failure_tag"] != "none"
        )
        return {
            "harness": {
                "name": "llm-gateway-eval-harness",
                "version": "v0",
                "started_at": started_at,
                "app_id": app_id,
            },
            "summary": {
                "total": len(results),
                "passed": passed,
                "failed": failed,
                "pass_rate": round(passed / len(results), 4) if results else 0,
                "fail_rate": round(failed / len(results), 4) if results else 0,
                "avg_cost_usd": round(total_cost / len(results), 6) if results else 0,
                "avg_latency_ms": round(total_latency / len(results), 2) if results else 0,
                "fallback_count": fallback_count,
                "failure_breakdown": dict(failure_breakdown),
            },
            "results": results,
        }

    def _run_one(self, app_id: str, case: Dict[str, Any]) -> Dict[str, Any]:
        started = time.perf_counter()
        expected = self._expected(case)
        try:
            response = self.run_case(case)
        except Exception as error:  # Harness must capture environment failures.
            latency_ms = int((time.perf_counter() - started) * 1000)
            failure_tag = self._exception_failure_tag(error)
            expected_failure_tag = case.get("expected_failure_tag")
            passed = expected_failure_tag == failure_tag
            return {
                "case_id": case.get("id", ""),
                "passed": passed,
                "failure_tag": "none" if passed else failure_tag,
                "expected_failure_tag": expected_failure_tag,
                "cost_usd": 0,
                "latency_ms": latency_ms,
                "fallback_count": 0,
                "assertions": {
                    "expected": expected,
                    "missing_keywords": [],
                    "missing_tools": [],
                    "model_matched": False,
                    "provider_matched": False,
                },
                "trace": {
                    "app_id": app_id,
                    "route_strategy": case.get("route_strategy", "default"),
                    "prompt_version_id": case.get("prompt_version_id"),
                    "attempts": [],
                    "tools": [],
                    "exception": {"type": error.__class__.__name__, "message": str(error)},
                },
            }

        latency_ms = response.get("usage", {}).get("latency_ms", int((time.perf_counter() - started) * 1000))
        attempts = response.get("attempts", [])
        observed_tools = response.get("trace", {}).get("tools", [])
        content = response.get("content", "")
        missing_keywords = [keyword for keyword in expected["keywords"] if keyword not in content]
        missing_tools = [tool for tool in expected["tools"] if tool not in observed_tools]
        model_matched = self._matches_expected(response.get("model_id"), expected["model_id"])
        provider_matched = self._matches_expected(response.get("provider"), expected["provider"])
        fallback_count = sum(1 for attempt in attempts if attempt.get("fallback_from"))
        failure_tag = self._response_failure_tag(response, missing_keywords, missing_tools, model_matched, provider_matched)
        expected_failure_tag = case.get("expected_failure_tag")

        if expected_failure_tag:
            passed = failure_tag == expected_failure_tag
            visible_failure_tag = "none" if passed else failure_tag
        else:
            passed = (
                response.get("status") not in {"failed", "blocked"}
                and not missing_keywords
                and not missing_tools
                and model_matched
                and provider_matched
            )
            visible_failure_tag = "none" if passed else failure_tag

        return {
            "case_id": case.get("id", ""),
            "passed": passed,
            "failure_tag": visible_failure_tag,
            "expected_failure_tag": expected_failure_tag,
            "cost_usd": response.get("usage", {}).get("cost_usd", 0),
            "latency_ms": latency_ms,
            "fallback_count": fallback_count,
            "assertions": {
                "expected": expected,
                "missing_keywords": missing_keywords,
                "missing_tools": missing_tools,
                "model_matched": model_matched,
                "provider_matched": provider_matched,
            },
            "trace": {
                "request_id": response.get("request_id"),
                "app_id": app_id,
                "model_id": response.get("model_id"),
                "provider": response.get("provider"),
                "route_strategy": response.get("route_strategy", case.get("route_strategy", "default")),
                "prompt_version_id": response.get("prompt_version_id", case.get("prompt_version_id")),
                "attempts": attempts,
                "tools": observed_tools,
                "error_code": response.get("error_code"),
                "error_message": response.get("error_message"),
            },
        }

    def _expected(self, case: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "keywords": case.get("expected_keywords", []),
            "tools": case.get("expected_tools", []),
            "model_id": case.get("expected_model_id"),
            "provider": case.get("expected_provider"),
            "failure_tag": case.get("expected_failure_tag"),
            "tags": case.get("tags", []),
        }

    def _matches_expected(self, actual: Optional[str], expected: Optional[str]) -> bool:
        return expected is None or actual == expected

    def _response_failure_tag(
        self,
        response: Dict[str, Any],
        missing_keywords: List[str],
        missing_tools: List[str],
        model_matched: bool,
        provider_matched: bool,
    ) -> str:
        error_code = response.get("error_code")
        if response.get("status") == "blocked":
            if error_code in {"BUDGET_EXCEEDED", "RATE_LIMITED", "APP_DISABLED"}:
                return "policy_failure"
            return "gateway_failure"
        if response.get("status") == "failed":
            if error_code == "NO_MODEL_AVAILABLE":
                return "routing_failure"
            return "model_failure"
        if missing_tools:
            return "tool_failure"
        if not model_matched or not provider_matched:
            return "routing_failure"
        if missing_keywords:
            return "quality_failure"
        return "none"

    def _exception_failure_tag(self, error: Exception) -> str:
        if isinstance(error, (KeyError, ValueError)):
            return "prompt_failure"
        return "harness_runtime_failure"

