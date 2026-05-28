# LLM Gateway / LLMOps Mini Platform

这是 6 个月 AI Builder 型 AI Harness / LLMOps 转型计划的第一个主项目：大模型调用治理平台。

它不是普通 API 中转 Demo，核心是把平台产品面试里最常被问到的能力做出来：

- 多模型接入与统一调用入口
- 路由策略：默认、低价优先、最快优先、综合策略
- 失败重试与 fallback
- 应用级 QPS 限制
- 月度预算与降级模型
- Prompt 版本管理
- 调用日志、Token 与成本统计
- 应用维度用量报表
- Eval Harness V0：批量运行、trace、成本/耗时/fallback 指标、失败归因
- Eval Gate：基于 `config/eval_policy.json` 输出 `allow` / `review` / `block` 发布判断
- AI Builder 证据：可运行代码、测试用例、README、AI 辅助开发复盘

## 快速运行核心逻辑

不安装 FastAPI 也可以先跑核心 Demo：

```bash
cd /Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/projects/llm-gateway
python3 -m app.cli_demo
python3 -m unittest discover -s tests
```

## 启动 API 服务

安装依赖后启动：

```bash
cd /Users/fengyonglong/workspace/code/pm-learning/ai-fde-portfolio/projects/llm-gateway
python3 -m pip install -r requirements.txt
python3 -m uvicorn app.main:app --reload --port 8010
```

接口：

- `GET /health`
- `GET /v1/models`
- `POST /v1/gateway/chat`
- `GET /v1/apps/{app_id}/usage`
- `GET /v1/usage`
- `GET /v1/logs`
- `POST /v1/evaluations/run`

## 示例请求

```bash
curl -X POST http://127.0.0.1:8010/v1/gateway/chat \
  -H 'Content-Type: application/json' \
  -d @examples/chat_request.json
```

```bash
curl -X POST http://127.0.0.1:8010/v1/evaluations/run \
  -H 'Content-Type: application/json' \
  -d @examples/evaluation_request.json
```

回归门禁样例：

```bash
curl -X POST http://127.0.0.1:8010/v1/evaluations/run \
  -H 'Content-Type: application/json' \
  -d @examples/evaluation_regression_request.json
```

## Eval Harness 返回重点

`POST /v1/evaluations/run` 会返回：

- `summary.pass_rate` / `summary.fail_rate`
- `summary.avg_cost_usd` / `summary.avg_latency_ms`
- `summary.fallback_count`
- `summary.failure_breakdown`
- `gate.decision`
- `gate.checks[]`
- `results[].trace.attempts`
- `results[].assertions`

## Eval Harness V0 门禁概念

V0 的定位不是替代完整评测平台，而是让 LLM Gateway 具备最小质量门禁：

- baseline：记录一批稳定 case 的通过率、平均成本、平均耗时和 fallback 次数。
- rubric：用关键词、工具、模型/供应商匹配和预期失败标签做可解释判断。
- regression：当通过率下降、成本/耗时上升或失败归因集中出现时，标记为版本退化。
- CI gate：发布 Prompt、模型或路由策略前先跑核心 case，指标在阈值内才允许上线。
- release decision：根据 `config/eval_policy.json` 输出 `allow`、`review` 或 `block`。

最小门禁表：

| 指标 | 作用 |
| --- | --- |
| `pass_rate` | 判断核心能力是否退化 |
| `avg_cost_usd` | 判断路由策略是否导致成本失控 |
| `avg_latency_ms` | 判断体验是否变慢 |
| `fallback_count` | 判断模型或供应商稳定性 |
| `failure_breakdown` | 区分质量、路由、Prompt、策略和模型问题 |

示例门禁输出摘要：

```json
{
  "gate": {
    "policy_id": "llm-gateway-release-gate-v0",
    "decision": "allow",
    "checks": [
      {"name": "pass_rate", "status": "pass", "observed": 1.0, "threshold": 0.95},
      {"name": "avg_cost_usd", "status": "pass", "observed": 0.000102, "threshold": 0.001},
      {"name": "avg_latency_ms", "status": "pass", "observed": 500.0, "threshold": 1200},
      {"name": "fallback_count", "status": "pass", "observed": 1, "threshold": 1}
    ]
  }
}
```

更多 before/after 说明见：

- `../../docs/projects/06-llm-gateway-eval-gate-report.md`

## 本地 CI Gate 命令

正常门禁：

```bash
python3 scripts/run_eval_gate.py --request examples/evaluation_request.json
```

回归样例报告：

```bash
python3 scripts/run_eval_gate.py --request examples/evaluation_regression_request.json --no-fail
```

退出码：

| decision | exit code | 含义 |
| --- | --- | --- |
| `allow` | `0` | 可以进入下一步发布或演示 |
| `block` | `1` | 存在质量或关键环境失败，阻断发布 |
| `review` | `2` | 质量通过但成本、延迟或 fallback 超阈值，需要人工复核 |

失败归因标签：

- `quality_failure`：内容未满足期望关键词。
- `model_failure`：模型供应商失败。
- `routing_failure`：路由结果不符合预期，或没有可用模型。
- `prompt_failure`：Prompt 模板变量缺失或版本错误。
- `policy_failure`：预算、限流、应用停用等网关策略拦截。
- `tool_failure`：Agent 工具调用缺失，后续 Agent Harness 使用。

## 面试讲法

这个项目要重点讲“治理”，不要只讲“调用模型”：

1. 企业接入大模型后，最早暴露的问题不是模型能力，而是稳定性、成本、审计和多租户治理。
2. 所以平台入口必须记录 app、model、provider、prompt version、token、cost、latency、status。
3. 路由策略可以按成本、速度、健康状态做取舍；失败时 fallback 保证可用性。
4. 预算和降级模型把产品商业化、客户套餐、毛利控制连起来。
5. Eval Harness 让平台从“能跑一次”进入“有 baseline、有 rubric、有 regression、有 CI gate、有 release decision 的质量门禁”。
6. AI Builder 价值不是炫技，而是能把产品需求推进到可运行原型，再用测试、eval、trace 和指标证明质量。
