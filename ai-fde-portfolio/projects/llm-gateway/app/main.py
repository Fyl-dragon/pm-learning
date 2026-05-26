from __future__ import annotations

from typing import Any, Dict, List, Optional

from .database import GatewayDatabase, default_db_path
from .gateway import GatewayRequest, GatewayService

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel, Field
except ModuleNotFoundError:  # pragma: no cover - local core tests do not require FastAPI.
    FastAPI = None  # type: ignore
    HTTPException = None  # type: ignore
    BaseModel = object  # type: ignore
    Field = None  # type: ignore


if FastAPI:

    class ChatRequest(BaseModel):
        app_id: str
        prompt: str
        model_id: Optional[str] = None
        route_strategy: str = "default"
        prompt_version_id: Optional[str] = None
        variables: Dict[str, Any] = Field(default_factory=dict)
        max_retries: int = 1

    class EvaluationRequest(BaseModel):
        app_id: str
        cases: List[Dict[str, Any]]


def create_app() -> "FastAPI":
    if not FastAPI:
        raise RuntimeError("FastAPI is not installed. Run: python3 -m pip install -r requirements.txt")

    api = FastAPI(
        title="LLM Gateway / LLMOps Mini Platform",
        description="多模型调用治理、成本统计、路由、降级和评测入口 Demo。",
        version="0.1.0",
    )
    service = GatewayService(GatewayDatabase(default_db_path()))

    @api.get("/health")
    def health() -> Dict[str, str]:
        return {"status": "ok"}

    @api.get("/v1/models")
    def models() -> List[Dict[str, Any]]:
        return service.model_catalog()

    @api.post("/v1/gateway/chat")
    def chat(payload: ChatRequest) -> Dict[str, Any]:
        try:
            return service.chat(GatewayRequest(**payload.model_dump()))
        except (KeyError, ValueError) as error:
            raise HTTPException(status_code=400, detail=str(error)) from error

    @api.get("/v1/apps/{app_id}/usage")
    def app_usage(app_id: str) -> Dict[str, Any]:
        return service.usage(app_id)

    @api.get("/v1/usage")
    def total_usage() -> Dict[str, Any]:
        return service.usage()

    @api.get("/v1/logs")
    def logs(limit: int = 20) -> List[Dict[str, Any]]:
        return service.db.latest_logs(limit)

    @api.post("/v1/evaluations/run")
    def run_evaluation(payload: EvaluationRequest) -> Dict[str, Any]:
        return service.evaluate(payload.app_id, payload.cases)

    return api


app = create_app() if FastAPI else None

