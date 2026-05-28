from __future__ import annotations

import hashlib
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from .config import AppConfig, ModelConfig, PromptVersion, load_apps, load_eval_policy, load_models, load_prompt_versions
from .database import GatewayDatabase
from .eval_harness import EvalHarness


@dataclass
class GatewayRequest:
    app_id: str
    prompt: str
    model_id: Optional[str] = None
    route_strategy: str = "default"
    prompt_version_id: Optional[str] = None
    variables: Dict[str, Any] = field(default_factory=dict)
    max_retries: int = 1


@dataclass
class ProviderResult:
    content: str
    prompt_tokens: int
    completion_tokens: int
    latency_ms: int


class ProviderError(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


class MockProvider:
    """Deterministic provider used for local demos and tests."""

    def complete(self, model: ModelConfig, prompt: str) -> ProviderResult:
        start = time.perf_counter()
        if f"FORCE_FAIL:{model.id}" in prompt or "FORCE_FAIL:ALL" in prompt:
            raise ProviderError("MOCK_PROVIDER_ERROR", f"{model.id} forced failure")
        digest = hashlib.sha1(f"{model.id}:{prompt}".encode("utf-8")).hexdigest()[:8]
        prompt_tokens = max(1, len(prompt) // 4)
        completion_tokens = 80 + int(digest[:2], 16) % 80
        latency_ms = model.avg_latency_ms + int((time.perf_counter() - start) * 1000)
        content = (
            f"[{model.id}] 已处理请求。digest={digest}; "
            f"建议从业务目标、技术链路、成本和兜底策略四层展开。"
        )
        return ProviderResult(content, prompt_tokens, completion_tokens, latency_ms)


class GatewayService:
    def __init__(
        self,
        db: GatewayDatabase,
        models: Optional[Dict[str, ModelConfig]] = None,
        apps: Optional[Dict[str, AppConfig]] = None,
        prompts: Optional[Dict[str, PromptVersion]] = None,
        eval_policy: Optional[Dict[str, Any]] = None,
        provider: Optional[MockProvider] = None,
    ) -> None:
        self.db = db
        self.models = models or load_models()
        self.apps = apps or load_apps()
        self.prompts = prompts or load_prompt_versions()
        self.eval_policy = eval_policy or load_eval_policy()
        self.provider = provider or MockProvider()

    def chat(self, request: GatewayRequest) -> Dict[str, Any]:
        request_id = str(uuid.uuid4())
        app = self._require_app(request.app_id)
        if not app.enabled:
            return self._blocked(request_id, request, "APP_DISABLED", "应用已停用")

        rendered_prompt = self._render_prompt(request)
        budget_decision = self._budget_decision(app, request.model_id)
        if budget_decision[0] == "blocked":
            return self._blocked(request_id, request, "BUDGET_EXCEEDED", "应用月度预算已用尽")
        model_override = budget_decision[1]

        if self.db.recent_call_count(app.id) >= app.qps_limit:
            return self._blocked(request_id, request, "RATE_LIMITED", "应用级 QPS 超限")

        candidate_models = self._candidate_models(app, request, model_override)
        last_error: Optional[ProviderError] = None
        attempts: List[Dict[str, Any]] = []

        for index, model in enumerate(candidate_models):
            fallback_from = candidate_models[index - 1].id if index > 0 else None
            try:
                result = self.provider.complete(model, rendered_prompt)
                cost = self._estimate_cost(model, result.prompt_tokens, result.completion_tokens)
                self.db.log_call(
                    {
                        "request_id": request_id,
                        "app_id": app.id,
                        "model_id": model.id,
                        "provider": model.provider,
                        "route_strategy": request.route_strategy,
                        "prompt_version_id": request.prompt_version_id,
                        "status": "success",
                        "prompt_tokens": result.prompt_tokens,
                        "completion_tokens": result.completion_tokens,
                        "cost_usd": cost,
                        "latency_ms": result.latency_ms,
                        "fallback_from": fallback_from,
                    }
                )
                attempts.append({"model_id": model.id, "status": "success", "fallback_from": fallback_from})
                return {
                    "request_id": request_id,
                    "app_id": app.id,
                    "model_id": model.id,
                    "provider": model.provider,
                    "route_strategy": request.route_strategy,
                    "prompt_version_id": request.prompt_version_id,
                    "content": result.content,
                    "usage": {
                        "prompt_tokens": result.prompt_tokens,
                        "completion_tokens": result.completion_tokens,
                        "cost_usd": round(cost, 6),
                        "latency_ms": result.latency_ms,
                    },
                    "attempts": attempts,
                }
            except ProviderError as error:
                last_error = error
                self.db.log_call(
                    {
                        "request_id": request_id,
                        "app_id": app.id,
                        "model_id": model.id,
                        "provider": model.provider,
                        "route_strategy": request.route_strategy,
                        "prompt_version_id": request.prompt_version_id,
                        "status": "failed",
                        "fallback_from": fallback_from,
                        "error_code": error.code,
                        "error_message": error.message,
                    }
                )
                attempts.append(
                    {
                        "model_id": model.id,
                        "status": "failed",
                        "fallback_from": fallback_from,
                        "error_code": error.code,
                    }
                )
                if index >= request.max_retries:
                    break

        error_message = last_error.message if last_error else "所有模型均不可用"
        return {
            "request_id": request_id,
            "app_id": app.id,
            "status": "failed",
            "error_code": last_error.code if last_error else "NO_MODEL_AVAILABLE",
            "error_message": error_message,
            "attempts": attempts,
        }

    def usage(self, app_id: Optional[str] = None) -> Dict[str, Any]:
        return self.db.usage_summary(app_id)

    def model_catalog(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": model.id,
                "provider": model.provider,
                "provider_model": model.provider_model,
                "health": model.health,
                "enabled": model.enabled,
                "avg_latency_ms": model.avg_latency_ms,
                "blended_price_per_1k": model.blended_price_per_1k,
            }
            for model in sorted(self.models.values(), key=lambda item: item.priority)
        ]

    def evaluate(self, app_id: str, cases: List[Dict[str, Any]]) -> Dict[str, Any]:
        harness = EvalHarness(
            lambda case: self.chat(
                GatewayRequest(
                    app_id=app_id,
                    prompt=case["prompt"],
                    model_id=case.get("model_id"),
                    route_strategy=case.get("route_strategy", "default"),
                    prompt_version_id=case.get("prompt_version_id"),
                    variables=case.get("variables", {}),
                    max_retries=case.get("max_retries", 1),
                )
            ),
            policy=self.eval_policy,
        )
        return harness.run(app_id, cases)

    def _candidate_models(
        self,
        app: AppConfig,
        request: GatewayRequest,
        model_override: Optional[str],
    ) -> List[ModelConfig]:
        if model_override:
            primary_id = model_override
        elif request.model_id:
            primary_id = request.model_id
        elif request.route_strategy == "low_cost":
            primary_id = min(self._enabled_models(), key=lambda model: model.blended_price_per_1k).id
        elif request.route_strategy == "fastest":
            primary_id = min(self._enabled_models(), key=lambda model: model.avg_latency_ms).id
        elif request.route_strategy == "balanced":
            primary_id = min(
                self._enabled_models(),
                key=lambda model: (model.blended_price_per_1k * 0.7) + (model.avg_latency_ms / 1000 * 0.3),
            ).id
        else:
            primary_id = app.default_model

        ordered_ids = [primary_id] + [model_id for model_id in app.fallback_models if model_id != primary_id]
        candidates = [self.models[model_id] for model_id in ordered_ids if model_id in self.models and self.models[model_id].enabled]
        if not candidates:
            raise ValueError(f"No enabled candidate model for app={app.id}")
        return candidates

    def _enabled_models(self) -> List[ModelConfig]:
        return [model for model in self.models.values() if model.enabled and model.health != "down"]

    def _require_app(self, app_id: str) -> AppConfig:
        app = self.apps.get(app_id)
        if not app:
            raise KeyError(f"Unknown app_id: {app_id}")
        return app

    def _budget_decision(self, app: AppConfig, requested_model_id: Optional[str]) -> Tuple[str, Optional[str]]:
        current_cost = self.db.monthly_cost(app.id)
        if current_cost < app.monthly_budget_usd:
            return "ok", None
        if app.downgrade_model and app.downgrade_model != requested_model_id:
            return "downgrade", app.downgrade_model
        return "blocked", None

    def _render_prompt(self, request: GatewayRequest) -> str:
        if not request.prompt_version_id:
            return request.prompt
        prompt_version = self.prompts.get(request.prompt_version_id)
        if not prompt_version:
            raise KeyError(f"Unknown prompt_version_id: {request.prompt_version_id}")
        variables = {"user_prompt": request.prompt, **request.variables}
        try:
            return prompt_version.template.format(**variables)
        except KeyError as error:
            missing = error.args[0]
            raise ValueError(f"Missing prompt variable: {missing}") from error

    def _estimate_cost(self, model: ModelConfig, prompt_tokens: int, completion_tokens: int) -> float:
        return (prompt_tokens / 1000 * model.input_price_per_1k) + (
            completion_tokens / 1000 * model.output_price_per_1k
        )

    def _blocked(self, request_id: str, request: GatewayRequest, code: str, message: str) -> Dict[str, Any]:
        self.db.log_call(
            {
                "request_id": request_id,
                "app_id": request.app_id,
                "model_id": request.model_id or "none",
                "provider": "gateway",
                "route_strategy": request.route_strategy,
                "prompt_version_id": request.prompt_version_id,
                "status": "blocked",
                "error_code": code,
                "error_message": message,
            }
        )
        return {
            "request_id": request_id,
            "app_id": request.app_id,
            "status": "blocked",
            "error_code": code,
            "error_message": message,
        }
