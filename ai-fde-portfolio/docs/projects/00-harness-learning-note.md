# Harness / Evals / LLMOps 学习与面试笔记

## 这里说的 Harness 是什么

这里的 harness 指 AI Eval Harness / Agent Harness / Harness Engineering / LLMOps 质量治理，不是只指 CI/CD 公司 Harness.io。

我的理解：

> Harness 是模型外面的工程环境。它负责给模型提供工具、状态、权限、反馈、评测、轨迹和失败恢复，让 LLM/RAG/Agent 不只是能演示，而是可测试、可排查、可迭代、可上线。

当前职业定位：

> AI 平台产品经理 / AI Evals & Harness 产品方向。FDE 只作为客户现场、交付、集成、需求抽象经验标签，不作为主攻 title。

## 为什么值得加进准备计划

AI 项目上线后的问题，很多不是“模型不够强”，而是环境没有设计好：

- 没有可重复评测，所以不知道版本变更有没有变差。
- 没有 trace，所以 Agent 失败后不知道错在哪一步。
- 没有工具权限和参数约束，所以系统不可控。
- 没有 Bad Case 归因，所以优化只能靠感觉。
- 没有回归测试，所以知识库更新后旧问题可能答错。
- 没有发布门禁，所以 Prompt、模型、RAG 策略或工具链更新后可能把旧能力破坏掉。

## 三层项目表达

LLM Gateway：

- 提供调用治理。
- 关注路由、成本、稳定性、预算、Prompt 版本。

Eval Harness：

- 提供可重复评测。
- 关注测试集、批量运行、通过率、成本、耗时、fallback、失败归因、发布门禁。

RAG Evaluation Harness：

- 提供知识库质量闭环。
- 关注标准问答集、召回命中、引用可信度、幻觉风险、Bad Case、文档版本回归。

Agent Harness：

- 提供 Agent 执行环境。
- 关注工具注册、状态管理、权限、轨迹、人工确认、失败恢复。

Harness 产品化：

- 提供 AI Evals 后台能力。
- 关注评测集管理、运行记录、对比实验、人工标注、生产 trace 回流、权限、报表和 CI gate。

## 面试回答

如果面试官问你最近比较火的 harness 怎么看，可以这样答：

> 我不会把 harness 理解成某个单独框架，而是理解成模型外面的工程和产品系统。企业 AI 项目里，模型只是推理能力，harness 决定这个能力如何被测试、约束、追踪、回归和持续改进。比如 LLM Gateway 是调用治理，Eval Harness 是可重复评测，RAG Evaluation Harness 是知识库质量闭环，Agent Harness 是工具、状态、权限、轨迹和失败恢复。很多 Agent 失败并不是换更强模型就能解决，而是工具定义、状态管理、终止条件、权限边界和反馈回路没有设计好。

如果面试官问为什么不主攻 FDE，可以这样答：

> FDE 是真实趋势，但我不会把它作为主攻 title，因为它的含金量非常依赖公司和产品成熟度。在顶级 AI 公司里，FDE 可能是深度嵌入客户、重构工作流和推动生产落地；但在本地中小公司里，也可能退化成驻场实施、客户成功、交付救火和外包开发。我会把 FDE 当成能力标签，把客户现场经验转化为 Harness 产品能力：把 bad case、生产 trace、模型失败和成本问题转成评测集、回归测试、失败归因和发布门禁。

## 项目落点

- 第 1 个月：LLM Gateway 增加 Eval Harness V0。
- 第 2 个月：RAG 项目升级为 RAG Evaluation Harness & Knowledge Governance。
- 第 3 个月：Agent Harness Layer，强调 trace、工具权限、状态、失败恢复和人工确认。
- 第 4 个月：Harness 产品化后台，展示评测集管理、运行记录、对比实验、人工标注、生产 trace 回流和发布门禁。

## 参考资料

- Harness AI Evals PM 岗位样例：https://jobs.menlovc.com/companies/harness/jobs/79807444-director-of-product-management-ai-evals
- Braintrust eval lifecycle：https://www.braintrust.dev/docs/evaluate
- Langfuse LLM observability / evaluation docs：https://langfuse.com/docs
- OpenAI Evals：https://github.com/openai/evals
- LLM Readiness Harness：https://arxiv.org/abs/2603.27355
- AI Harness Engineering：https://arxiv.org/abs/2605.13357
- OpenAI Deployment Company：https://openai.com/index/openai-launches-the-deployment-company/
- Constellation Research on FDE risk：https://www.constellationr.com/insights/news/forward-deployed-engineers-promise-peril-ai-deployments
