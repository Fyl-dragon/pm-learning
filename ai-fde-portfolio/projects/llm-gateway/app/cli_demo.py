from __future__ import annotations

import json

from .database import GatewayDatabase
from .gateway import GatewayRequest, GatewayService


def main() -> None:
    db = GatewayDatabase(":memory:")
    service = GatewayService(db)
    response = service.chat(
        GatewayRequest(
            app_id="app-sales-copilot",
            prompt="客户希望搭建一个汽车售后知识库，要求控制模型成本并保留调用日志。",
            route_strategy="balanced",
            prompt_version_id="prompt-solution-v1",
            variables={"industry": "汽车售后", "scenario": "维修知识库"},
            max_retries=2,
        )
    )
    print(json.dumps(response, ensure_ascii=False, indent=2))
    print(json.dumps(service.usage("app-sales-copilot"), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

