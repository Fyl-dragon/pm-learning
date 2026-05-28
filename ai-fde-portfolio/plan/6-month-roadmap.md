# 6 个月 AI Builder 型 AI Harness / LLMOps 转型路线

## 定位

目标岗位优先级：

1. AI Evals / Harness / LLMOps 质量治理产品经理
2. 大模型平台产品经理，偏模型调用治理、评测、可观测性、成本和稳定性
3. RAG / Agent 平台产品经理，偏 trace、workflow、工具调用和失败归因
4. AI 解决方案产品经理，仅选择能沉淀平台能力的岗位
5. FDE，仅作为备选，不作为主攻 title

你的卖点组合：

- 软件工程 + Java 开发经验
- 产品经理经历
- 大模型平台/中转平台经验
- 外包、驻场、客户现场对接经验
- Eval Harness / Agent Harness / RAG Evaluation Harness 意识
- 重庆本地制造业、政企数字化、企业服务场景适配度

职业定位：

> AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力。重点关注 LLM Gateway、Eval Harness、RAG 质量治理、Agent Harness、调用可观测性、成本控制和失败归因，能够用 AI 辅助开发把需求推进到可运行原型，并把 AI 应用从“能调用”推进到“可评测、可追踪、可回归、可持续优化”。

AI Builder 使用边界：

- 不把主定位改成“AI 全栈产品经理”，也不转纯工程师路线。
- AI Builder 是能力标签：能用 Codex / Claude Code / Cursor 等工具做需求拆解、代码生成、测试、debug、文档和复盘。
- 每个技术学习任务都必须转成产品方案、可运行/可交互产物、测试/eval、简历 bullet 或面试讲法。
- 不学深度学习训练、CUDA、分布式训练、复杂前端工程和算法刷题，除非目标岗位明确要求。

FDE 使用边界：

- 保留为客户现场、交付、集成、需求抽象经验标签。
- 不把自己包装成纯 FDE，避免落入驻场实施、客户成功、交付救火、售前支持和外包开发的混合岗位。
- 只考虑明确包含 eval harness、production trace、platform feedback loop、product roadmap 的 FDE/解决方案岗位。

## 学习资料使用边界

学习资料必须服务作品集和面试表达，不再追求“资料越多越好”。

默认优先级见 `learning-resources-priority.md`：

1. P0：中文基础补齐资料，优先 Datawhale LLM Cookbook 和 Happy-LLM 第 7 章应用部分。
2. P1：能直接产出 Eval Harness / Agent Harness 的资料，优先 Hugging Face Agents Course 中文版、promptfoo、Langfuse。
3. P1/P2：rohitg00/ai-engineering-from-scratch 精选 Phase 11/13/14/17，作为 AI Builder 工程实践库；按 `ai-engineering-from-scratch-study-plan.md` 学，不全量学习。
4. P2：官方或高质量英文资料，选择性使用 OpenAI Evals、DeepLearning.AI Evaluating AI Agents。
5. P3：Phoenix、DeepEval、RAGAS 只做工具横评。
5. P4：泛课程平台或入口过大的资料，不纳入主线。

所有学习资料都必须标注具体章节、语言门槛、投入上限和产出物；如果不能转成产品方案、评测指标、bad case、简历 bullet 或面试讲法，就暂停学习。

## 横向技术能力线

技术路线详见 `ai-builder-technical-track.md`，贯穿 6 个月但不替代产品主线。

必须补强：

- Python / FastAPI 基础：API、日志、测试、异常、数据结构。
- 简单前端/后台原型：HTML/CSS/JS 或轻量 React，用于展示产品工作流。
- LLM API 工程：流式输出、错误处理、重试、fallback、成本统计、Prompt 版本。
- RAG 工程：chunk、embedding、向量库、召回、重排、引用、RAG eval。
- Agent 工程：tool calling、MCP、LangGraph / workflow、状态、权限、trace、human review。
- Evals / Harness：测试集、LLM-as-judge、CI gate、bad case、回归测试、生产 trace 回流。
- AI 辅助开发工作流：让 AI 生成代码，但用人工产品判断、测试、eval 和复盘控制质量。

## 第 1 个月：LLM Gateway / LLMOps Mini Platform + Eval Harness V0

目标：把现有“大模型中转平台经验”升级成“调用治理平台”项目。

必须完成：

- 多模型接入
- 路由策略
- fallback
- 调用日志
- Token 与成本统计
- 应用级用量报表
- 预算和限流
- Prompt 版本
- Eval Harness V0：测试集、批量运行、trace、成本/耗时/fallback 指标、失败归因
- 简历 V1
- 项目复盘 V1

学习资料：

- Datawhale LLM Cookbook：Prompt Engineering、Building Systems、评估改进生成式 AI。
- Datawhale LLM Universe：只学大模型应用开发、LLM API、RAG 应用和工程化实践相关章节。
- FastAPI 中文文档：只学 API、请求/响应、异常、测试相关章节。
- promptfoo：Getting Started、prompt eval、LLM-as-judge、CI/CD gate。
- rohitg00/ai-engineering-from-scratch：P1 精选学习 Phase 11 `10-evaluation`，按 5 步学习法产出 Eval Harness 迁移点。

AI Builder 产出：

- 至少完成 1 个 LLM Gateway 小功能、1 组测试、1 段 AI 辅助开发复盘。

## 第 2 个月：RAG Evaluation Harness & Knowledge Governance

目标：不做普通知识库，做企业上线后真正需要的质量闭环。

必须覆盖：

- 标准问答集
- 批量评测
- 召回命中分析
- Bad Case 管理
- 知识缺口识别
- 文档版本回归测试
- 引用可信度与幻觉风险
- 不同切分、Embedding、重排策略的 A/B 对比

学习资料：

- Datawhale LLM Cookbook：RAG、搭建和评估高级 RAG 应用。
- Happy-LLM 第 7 章：RAG 和模型评测相关内容。
- rohitg00/ai-engineering-from-scratch：选择性使用 Phase 11 `06-rag`、`07-advanced-rag` 和 `10-evaluation`，只学能迁移到 RAG Evaluation Harness 的部分。
- RAGAS / DeepEval / Phoenix：只做工具横评，不作为主课。

AI Builder 产出：

- 做出 RAG Evaluation Harness 最小链路：标准问答集、引用、召回命中、幻觉风险和版本回归。

## 第 3 个月：Agent Harness Layer

目标：不只做“会跑的 Agent”，而是展示你理解 Agent 为什么失控，以及如何评测、追踪、回归和恢复。

必须覆盖：

- Agent loop、Tool registry、State、Guardrails、Trace、Recovery
- 工具权限、参数 schema、终止条件、人工确认节点
- 运行轨迹、失败归因、回放和版本回归
- 客户现场 bad case 如何回流成评测集
- 面试表达：Agent 质量治理不是换更强模型，而是建设执行环境、可观测性和反馈闭环

学习资料：

- Hugging Face Agents Course 中文版：单元 1、单元 2.3 LangGraph、单元 3 Agentic RAG、附加单元 2 代理可观测性和评估。
- DeepLearning.AI Evaluating AI Agents：可选，学习前先确认字幕或 transcript，只学 tracing、router eval、trajectory eval、monitoring。
- rohitg00/ai-engineering-from-scratch：P1 精选学习 Phase 14 `01-the-agent-loop`、`20-agent-observability`、`21-agent-failure-modes`、`30-eval-driven-agent-development` 和 `31-agent-verification-gates`。

AI Builder 产出：

- 做出 Agent Harness 样例：tool registry、trace、失败归因、人工确认和回归测试。

## 第 4 个月：Harness 产品化

目标：做一个更像真实 AI Evals 产品经理作品的后台方案。

必须覆盖：

- 评测集管理
- 运行记录
- 对比实验
- 失败归因
- 人工标注
- 生产 trace 回流
- 发布门禁 / CI gate
- 权限、报表、项目空间
- RAG/Agent 场景下的 bad case 管理

行业场景可作为数据来源：制造业售后诊断 Agent、企业经营数据分析 Copilot、政企知识库助手。

学习资料：

- Langfuse：只拆 traces、datasets、experiments、evals、prompt management。
- OpenAI Evals：只学 examples、eval templates、custom/private eval 概念。
- promptfoo：补齐 red teaming、RAG eval 和 CI/CD gate 的产品化表达。
- rohitg00/ai-engineering-from-scratch：选择性使用 Phase 13 `01-the-tool-interface`、`05-tool-schema-design`、`20-opentelemetry-genai` 和 Phase 17 `16-model-routing`、`19-ai-gateways`、`27-finops-llms`。

AI Builder 产出：

- 做出 Harness 产品化后台可交互原型或轻量 Demo，至少覆盖评测集、运行记录、对比实验、失败归因和人工标注。

## 第 5 个月：作品集与面试启动

目标：把 Harness/Evals/LLMOps 项目变成市场报价。

必须完成：

- 简历 V2：主打 AI 平台产品 / AI Evals & Harness
- 3 个项目作品集：LLM Gateway、RAG Evaluation Harness、Agent Harness 或 Harness 产品化后台
- 每个作品集都同时展示 PRD、代码仓库、测试/eval、项目复盘和 AI 辅助开发复盘
- 每个项目 3 分钟、8 分钟、15 分钟讲法
- 每周 5-10 个岗位投递
- 面试反馈复盘

岗位搜索关键词：

- AI Evals
- LLMOps
- AI observability
- RAG evaluation
- Agent platform
- AI platform PM
- 大模型平台产品
- 模型评测 / 模型质量治理

岗位排除关键词：

- 纯驻场实施
- 客户成功
- 交付经理
- 售前支持
- 只写“懂大模型优先”但没有平台、评测、trace、治理能力的岗位

## 第 6 个月：决策与谈判

判断标准：

- 本公司涨到 11K-12K 且给 AI 平台治理、Eval Harness、RAG/Agent 质量闭环相关职责：可继续观察。
- 本公司只涨 500-1000 或继续模糊承诺：继续找。
- 外部 13K-15K 且方向匹配 Harness/Evals/LLMOps：认真考虑。
- 外部低于 11K：除非平台极强，否则不建议动。
