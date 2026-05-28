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
- AI Builder 证据：可运行代码、测试用例、README、AI 辅助开发复盘

## 快速运行核心逻辑

不安装 FastAPI 也可以先跑核心 Demo：

```bash
cd /Users/fyl/workspace/产品/ai-fde-portfolio/projects/llm-gateway
python3 -m app.cli_demo
python3 -m unittest discover -s tests
```

## 启动 API 服务

安装依赖后启动：

```bash
cd /Users/fyl/workspace/产品/ai-fde-portfolio/projects/llm-gateway
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

## Eval Harness 返回重点

`POST /v1/evaluations/run` 会返回：

- `summary.pass_rate` / `summary.fail_rate`
- `summary.avg_cost_usd` / `summary.avg_latency_ms`
- `summary.fallback_count`
- `summary.failure_breakdown`
- `results[].trace.attempts`
- `results[].assertions`

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
5. Eval Harness 让平台从“能跑一次”进入“可重复评测、可定位失败、可持续优化”。
6. AI Builder 价值不是炫技，而是能把产品需求推进到可运行原型，再用测试、eval、trace 和指标证明质量。
