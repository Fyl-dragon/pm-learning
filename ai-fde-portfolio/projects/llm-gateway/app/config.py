from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = BASE_DIR / "config"


@dataclass(frozen=True)
class ModelConfig:
    id: str
    provider: str
    provider_model: str
    input_price_per_1k: float
    output_price_per_1k: float
    avg_latency_ms: int
    health: str
    priority: int
    enabled: bool = True

    @property
    def blended_price_per_1k(self) -> float:
        return self.input_price_per_1k + self.output_price_per_1k


@dataclass(frozen=True)
class AppConfig:
    id: str
    name: str
    owner: str
    monthly_budget_usd: float
    qps_limit: int
    default_model: str
    downgrade_model: Optional[str]
    fallback_models: List[str]
    enabled: bool = True


@dataclass(frozen=True)
class PromptVersion:
    id: str
    app_id: str
    name: str
    version: str
    template: str
    status: str


def load_json(name: str) -> Any:
    path = CONFIG_DIR / name
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_models() -> Dict[str, ModelConfig]:
    rows = load_json("models.json")["models"]
    return {row["id"]: ModelConfig(**row) for row in rows}


def load_apps() -> Dict[str, AppConfig]:
    rows = load_json("apps.json")["apps"]
    return {row["id"]: AppConfig(**row) for row in rows}


def load_prompt_versions() -> Dict[str, PromptVersion]:
    rows = load_json("prompts.json")["prompt_versions"]
    return {row["id"]: PromptVersion(**row) for row in rows}

