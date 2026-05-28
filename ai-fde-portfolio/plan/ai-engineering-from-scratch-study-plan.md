# rohitg00/ai-engineering-from-scratch 精选学习计划

日期：2026-05-28

## 结论

`rohitg00/ai-engineering-from-scratch` 从原来的 P3 参考库升级为：

> P1/P2 精选工程实践库 + AI Builder 训练库。

但它仍然不是主线课程，不全量学习，不替代 AI Evals / Harness / LLMOps 产品主线。它的正确用途是帮助你把产品判断推进到可运行、可评测、可追踪、可复盘的工程证据。

本地路径：

`/Users/fengyonglong/workspace/code/ai-engineering-from-scratch`

本地快照事实：

- README 显示 473 lessons、20 phases、约 320 小时。
- 最近提交：`86bbb614d9bbcb49baf155dc50eb0ecdaba3aa4f`，提交时间 `2026-05-27 20:52:57 +0000`。
- 每课通常包含 `docs/`、`code/`、`outputs/`，部分包含 `notebook/` 和 `assets/`。

## 纳入边界

| 优先级 | 范围 | 学习方式 | 用途 |
| --- | --- | --- | --- |
| P1 | Phase 11 / 13 / 14 / 17 中和 LLM Gateway、Eval Harness、Agent Harness、LLMOps 直接相关的 lessons | 连续 4 周精选学习 | 强化 AI Builder 证据和项目深度 |
| P2 | 可补概念、补代码结构、补面试讲法的 lessons | 遇到项目问题时查阅 | 补齐技术理解和产品表达 |
| P4 | 数学、深度学习训练、视觉、语音、RL、分布式推理、GPU/CUDA、复杂 serving 内核 | 暂不学习 | 避免偏离 AI PM / Harness 主线 |

## 优先学习范围

### Phase 11：LLM Engineering

重点：

- `06-rag`
- `07-advanced-rag`
- `10-evaluation`
- `11-caching-cost`
- `12-guardrails`
- `13-production-app`
- `14-model-context-protocol`
- `16-langgraph-state-machines`
- `17-agent-framework-tradeoffs`

产出方向：

- LLM Gateway 的 eval case、baseline、regression、CI gate。
- RAG Evaluation Harness 的指标和 bad case 设计。
- Prompt 版本、成本、guardrails、MCP、LangGraph 的产品化表达。

### Phase 13：Tools & Protocols

重点：

- `01-the-tool-interface`
- `02-function-calling-deep-dive`
- `05-tool-schema-design`
- `06-mcp-fundamentals`
- `20-opentelemetry-genai`
- `21-llm-routing-layer`

产出方向：

- Agent tool registry 设计表。
- 工具 schema、权限、参数校验、错误处理说明。
- trace 字段表和 MCP 产品概念卡。

### Phase 14：Agent Engineering

重点：

- `01-the-agent-loop`
- `03-tool-use`
- `20-agent-observability`
- `21-agent-failure-modes`
- `30-eval-driven-agent-development`
- `31-agent-verification-gates`
- `39-workbench-for-real-repos`

产出方向：

- Agent Harness 的 loop、tool registry、trace、失败归因、human review。
- Agent eval case、回归测试和 CI gate 草案。
- 面试讲法：Agent 不是会调用工具就行，而是要可追踪、可评测、可回归。

### Phase 17：Infrastructure & Production

重点：

- `01-inference-economics`
- `08-inference-metrics-goodput`
- `13-llm-observability`
- `16-model-routing`
- `19-ai-gateways`
- `21-ab-testing-llm-features`
- `22-load-testing-llm-apis`
- `27-finops-llms`

产出方向：

- LLM Gateway 的成本、质量、稳定性三角权衡。
- fallback、routing、latency、success rate、FinOps 的指标解释。
- A/B testing、load testing、observability 的产品功能拆解。

## 5 步学习法

不要照着全量敲一遍，也不要只运行一次看热闹。

每个 lesson 按 5 步完成：

1. 先读目标：读 `docs/en.md` 的 Problem、Learning Objectives、Use It、Ship It。
2. 先跑代码：运行 `code/*.py` 或主入口文件，观察输出的业务指标或系统行为。
3. 再读代码：只读关键类、数据结构、输入输出和决策逻辑。
4. 必须改一处：改一个参数、加一个 case、换一个策略、补一个失败场景。
5. 迁移到自己项目：把启发转成 LLM Gateway / RAG Evaluation Harness / Agent Harness 的功能、指标、复盘或面试讲法。

## 什么时候照敲

只在满足下面条件时照敲：

- 代码小于 150 行。
- 是核心概念结构，例如 agent loop、eval harness、routing simulator。
- 照敲后关掉原文，自己复述一遍输入、处理、输出和关键决策。

不照敲样板代码、工具包装代码、长脚本和暂时无法迁移到项目里的内容。

## 什么时候只运行

只运行适合用于快速筛选 lesson 是否值得深学，例如观察：

- pass rate
- baseline
- fallback
- cost saving
- latency
- success rate
- escalation

只运行不复盘，不算完成。

## 前 4 周计划

### 第 1 周：Eval Harness 强化

学习：

- `phases/11-llm-engineering/10-evaluation`

运行：

- `code/eval_framework.py`

产出：

- 给 LLM Gateway Eval Harness 增加 rubric、baseline、regression、CI gate 概念。
- 写一段 3 分钟面试讲法：为什么 eval 不是看几个输出，而是质量门禁。

### 第 2 周：Model Routing / AI Gateway

学习：

- `phases/17-infrastructure-and-production/16-model-routing`
- `phases/17-infrastructure-and-production/19-ai-gateways`

已验证运行结果摘要：

- Model routing simulator 可输出成本、质量、节省比例和 escalation。
- AI gateway simulator 可输出 success rate、latency、retry/fallback。

产出：

- 把 LLM Gateway 复盘升级为“成本、质量、稳定性三角权衡”。
- 增补一张 routing / fallback / gateway 指标表。

### 第 3 周：Agent Harness

学习：

- `phases/14-agent-engineering/01-the-agent-loop`
- `phases/14-agent-engineering/30-eval-driven-agent-development`

产出：

- Agent Harness 的 tool registry、trace、失败归因、eval case、CI gate 草案。
- 写一段面试表达：Agent 不是会调用工具就行，而是要可追踪、可评测、可回归。

### 第 4 周：Tools / MCP / Observability

学习：

- `phases/13-tools-and-protocols/01-the-tool-interface`
- `phases/13-tools-and-protocols/05-tool-schema-design`
- `phases/13-tools-and-protocols/20-opentelemetry-genai`

产出：

- Agent 工具 schema 设计表。
- trace 字段表。
- MCP 产品概念卡。

## Lesson 完成标准

每个 lesson 学完必须留下 4 个东西：

- 运行截图或输出摘要。
- 代码结构理解：输入、处理、输出、关键决策。
- 和项目的连接：能放进 LLM Gateway / RAG Evaluation Harness / Agent Harness 的哪一块。
- 职业表达：1 条简历 bullet 或 1 段 3 分钟面试讲法。

如果一个 lesson 不能转成这些产出，就降级为浏览，不继续深学。

## 与主线的关系

主线仍然是：

> AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力。

这个仓库的价值不是把你训练成纯 AI Engineer，而是帮你证明：

- 你懂产品问题背后的技术机制。
- 你能用 AI 辅助开发跑出可验证样例。
- 你能把 routing、eval、observability、agent failure 等工程问题转成平台功能、指标体系和面试表达。
