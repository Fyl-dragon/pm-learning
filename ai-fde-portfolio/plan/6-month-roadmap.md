# 6 个月 AI Harness / LLMOps 转型路线

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

> AI 平台产品经理 / AI Evals & Harness 产品方向。重点关注 LLM Gateway、Eval Harness、RAG 质量治理、Agent Harness、调用可观测性、成本控制和失败归因，把 AI 应用从“能调用”推进到“可评测、可追踪、可回归、可持续优化”。

FDE 使用边界：

- 保留为客户现场、交付、集成、需求抽象经验标签。
- 不把自己包装成纯 FDE，避免落入驻场实施、客户成功、交付救火、售前支持和外包开发的混合岗位。
- 只考虑明确包含 eval harness、production trace、platform feedback loop、product roadmap 的 FDE/解决方案岗位。

## 学习资料使用边界

学习资料必须服务作品集和面试表达，不再追求“资料越多越好”。

默认优先级见 `learning-resources-priority.md`：

1. P0：中文基础补齐资料，优先 Datawhale LLM Cookbook 和 Happy-LLM 第 7 章应用部分。
2. P1：能直接产出 Eval Harness / Agent Harness 的资料，优先 Hugging Face Agents Course 中文版、promptfoo、Langfuse。
3. P2：官方或高质量英文资料，选择性使用 OpenAI Evals、DeepLearning.AI Evaluating AI Agents。
4. P3：工程化参考库，只在遇到具体问题时查 rohitg00/ai-engineering-from-scratch、Phoenix、DeepEval、RAGAS。
5. P4：泛课程平台或入口过大的资料，不纳入主线。

所有学习资料都必须标注具体章节、语言门槛、投入上限和产出物；如果不能转成产品方案、评测指标、bad case、简历 bullet 或面试讲法，就暂停学习。

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
- promptfoo：Getting Started、prompt eval、LLM-as-judge、CI/CD gate。
- rohitg00/ai-engineering-from-scratch：仅查 Phase 11 Evaluation 相关内容，不连续学习。

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
- RAGAS / DeepEval / Phoenix：只做工具横评，不作为主课。

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
- rohitg00/ai-engineering-from-scratch：仅查 Phase 14 Agent Observability / Eval-driven Agent 相关内容。

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

## 第 5 个月：作品集与面试启动

目标：把 Harness/Evals/LLMOps 项目变成市场报价。

必须完成：

- 简历 V2：主打 AI 平台产品 / AI Evals & Harness
- 3 个项目作品集：LLM Gateway、RAG Evaluation Harness、Agent Harness 或 Harness 产品化后台
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
