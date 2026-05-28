from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.database import GatewayDatabase  # noqa: E402
from app.gateway import GatewayService  # noqa: E402


EXIT_CODES = {
    "allow": 0,
    "block": 1,
    "review": 2,
}


def load_request(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def compact_report(result: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "harness": result["harness"],
        "summary": result["summary"],
        "gate": result["gate"],
        "failed_results": [
            {
                "case_id": item["case_id"],
                "failure_tag": item["failure_tag"],
                "missing_keywords": item["assertions"]["missing_keywords"],
                "missing_tools": item["assertions"]["missing_tools"],
            }
            for item in result["results"]
            if not item["passed"]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run LLM Gateway eval gate and return a CI-like exit code.")
    parser.add_argument(
        "--request",
        default="examples/evaluation_request.json",
        help="Evaluation request JSON path, relative to the LLM Gateway project root.",
    )
    parser.add_argument(
        "--no-fail",
        action="store_true",
        help="Always exit 0 after printing the report. Useful for demos or before/after reports.",
    )
    args = parser.parse_args()

    request_path = Path(args.request)
    if not request_path.is_absolute():
        request_path = PROJECT_ROOT / request_path

    payload = load_request(request_path)
    service = GatewayService(GatewayDatabase(":memory:"))
    result = service.evaluate(payload["app_id"], payload["cases"])
    report = compact_report(result)
    print(json.dumps(report, ensure_ascii=False, indent=2))

    decision = result["gate"]["decision"]
    if args.no_fail:
        return 0
    return EXIT_CODES.get(decision, 1)


if __name__ == "__main__":
    raise SystemExit(main())
