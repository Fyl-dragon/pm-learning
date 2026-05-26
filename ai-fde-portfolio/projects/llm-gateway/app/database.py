from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


SCHEMA = """
CREATE TABLE IF NOT EXISTS call_logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  request_id TEXT NOT NULL,
  app_id TEXT NOT NULL,
  model_id TEXT NOT NULL,
  provider TEXT NOT NULL,
  route_strategy TEXT NOT NULL,
  prompt_version_id TEXT,
  status TEXT NOT NULL,
  prompt_tokens INTEGER NOT NULL DEFAULT 0,
  completion_tokens INTEGER NOT NULL DEFAULT 0,
  cost_usd REAL NOT NULL DEFAULT 0,
  latency_ms INTEGER NOT NULL DEFAULT 0,
  fallback_from TEXT,
  error_code TEXT,
  error_message TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_call_logs_app_created
ON call_logs(app_id, created_at);

CREATE INDEX IF NOT EXISTS idx_call_logs_request
ON call_logs(request_id);
"""


class GatewayDatabase:
    def __init__(self, path: str = ":memory:") -> None:
        self.path = path
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.init_schema()

    def init_schema(self) -> None:
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    def log_call(self, row: Dict[str, Any]) -> None:
        defaults = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "cost_usd": 0,
            "latency_ms": 0,
        }
        payload = {**defaults, **row}
        fields = [
            "request_id",
            "app_id",
            "model_id",
            "provider",
            "route_strategy",
            "prompt_version_id",
            "status",
            "prompt_tokens",
            "completion_tokens",
            "cost_usd",
            "latency_ms",
            "fallback_from",
            "error_code",
            "error_message",
        ]
        placeholders = ", ".join("?" for _ in fields)
        sql = f"INSERT INTO call_logs ({', '.join(fields)}) VALUES ({placeholders})"
        self.conn.execute(sql, [payload.get(field) for field in fields])
        self.conn.commit()

    def monthly_cost(self, app_id: str) -> float:
        row = self.conn.execute(
            """
            SELECT COALESCE(SUM(cost_usd), 0) AS total_cost
            FROM call_logs
            WHERE app_id = ?
              AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
              AND status = 'success'
            """,
            (app_id,),
        ).fetchone()
        return float(row["total_cost"])

    def recent_call_count(self, app_id: str, seconds: int = 1) -> int:
        row = self.conn.execute(
            """
            SELECT COUNT(*) AS total
            FROM call_logs
            WHERE app_id = ?
              AND created_at >= datetime('now', ?)
            """,
            (app_id, f"-{seconds} seconds"),
        ).fetchone()
        return int(row["total"])

    def usage_summary(self, app_id: Optional[str] = None) -> Dict[str, Any]:
        params: Iterable[Any] = (app_id,) if app_id else ()
        where = "WHERE app_id = ?" if app_id else ""
        total = self.conn.execute(
            f"""
            SELECT
              COUNT(*) AS calls,
              COALESCE(SUM(cost_usd), 0) AS cost_usd,
              COALESCE(SUM(prompt_tokens + completion_tokens), 0) AS total_tokens,
              COALESCE(AVG(NULLIF(latency_ms, 0)), 0) AS avg_latency_ms,
              SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) AS success_calls,
              SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) AS failed_calls,
              SUM(CASE WHEN status = 'blocked' THEN 1 ELSE 0 END) AS blocked_calls
            FROM call_logs
            {where}
            """,
            tuple(params),
        ).fetchone()
        by_model_rows = self.conn.execute(
            f"""
            SELECT model_id, COUNT(*) AS calls, COALESCE(SUM(cost_usd), 0) AS cost_usd
            FROM call_logs
            {where}
            GROUP BY model_id
            ORDER BY cost_usd DESC
            """,
            tuple(params),
        ).fetchall()
        return {
            "calls": int(total["calls"]),
            "cost_usd": round(float(total["cost_usd"]), 6),
            "total_tokens": int(total["total_tokens"]),
            "avg_latency_ms": round(float(total["avg_latency_ms"]), 2),
            "success_calls": int(total["success_calls"] or 0),
            "failed_calls": int(total["failed_calls"] or 0),
            "blocked_calls": int(total["blocked_calls"] or 0),
            "by_model": [
                {
                    "model_id": row["model_id"],
                    "calls": int(row["calls"]),
                    "cost_usd": round(float(row["cost_usd"]), 6),
                }
                for row in by_model_rows
            ],
        }

    def latest_logs(self, limit: int = 20) -> List[Dict[str, Any]]:
        rows = self.conn.execute(
            """
            SELECT *
            FROM call_logs
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [dict(row) for row in rows]


def default_db_path() -> str:
    data_dir = Path(__file__).resolve().parents[1] / ".data"
    data_dir.mkdir(exist_ok=True)
    return str(data_dir / "gateway.sqlite3")
