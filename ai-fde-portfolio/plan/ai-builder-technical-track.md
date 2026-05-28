# AI Builder 技术能力线

日期：2026-05-28

## 结论

不把职业主线改成“AI 全栈”，而是在现有主线下新增 AI Builder 能力：

> AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力。

AI Builder 的含义不是和全栈工程师拼完整工程深度，而是能用 AI 辅助开发把产品判断快速变成可运行原型、LLM 应用 Demo、Eval Harness 样例、RAG/Agent 质量治理工具，并用测试、eval、trace 和指标证明质量。

## 市场判断

快照日期：2026-05-28。

- Anthropic 的 Claude Code 产品经理岗位要求 PM 兼具产品和工程经验，包含至少 1 年职业工程师经历，并持续 hands-on 使用 AI coding tools。来源：https://www.anthropic.com/careers/jobs/4985920008
- Anthropic 官方案例显示 Claude Code 正在模糊技术和非技术工作的边界，产品设计、数据科学、法律、增长等团队都在用它做原型、测试、自动化和代码理解。来源：https://www.anthropic.com/news/how-anthropic-teams-use-claude-code
- Anthropic 的 agentic coding 指南强调 PM 可以基于真实代码库约束写需求，设计师可以把 Figma 转成功能原型，但也需要用测试规格、清晰验收标准、逐步实现和安全约束控制 AI 编程。来源：https://resources.anthropic.com/hubfs/Scaling%20agentic%20coding%20across%20your%20organization.pdf?hsLang=en
- OpenAI 的 API Agents PM 岗要求 PM 与 research / engineering 在技术层面协作，把 agent builder 的问题转成 SDK、API 等开发者产品能力。来源：https://openai.com/careers/product-manager-api-agents-san-francisco/
- OpenAI Applied Evals 岗位招聘 product-minded engineers 设计 evals 和 harnesses，说明 Evals/Harness 本身处在产品与工程交界处。来源：https://openai.com/careers/software-engineer-applied-evals/

判断：

- AI 产品岗正在变得更技术化，能读代码、写原型、跑测试、理解工程约束会明显加分。
- “AI 全栈”在招聘语境里多数仍是工程师 title，不适合作为你的主攻定位。
- 你的更优解是“技术型 AI PM + AI Builder + Harness/Evals 主线”，而不是从产品经理路线切换到纯全栈开发路线。

## 必须学

### Python / FastAPI 基础

目标：

- 能写 API、读日志、跑测试、理解接口、异常和数据结构。
- 能和工程讨论 endpoint、request/response、状态码、鉴权、限流、错误处理。

产出：

- LLM Gateway 增加 1-2 个可演示 API。
- 为核心链路补充测试用例。
- 能在面试中解释一个接口从请求到日志、路由、fallback、eval 的链路。

### 简单前端 / 后台原型

目标：

- 能用 HTML/CSS/JS 或轻量 React 做后台原型。
- 能表达评测集管理、运行记录、对比实验、失败归因、人工标注、报表等产品界面。

产出：

- Harness 产品化后台可交互原型。
- 至少覆盖列表、详情、运行记录、对比、空态、失败态和权限提示。

### LLM API 工程

目标：

- 理解模型调用、流式输出、错误处理、重试、fallback、成本统计、Prompt 版本。
- 能把“模型能力”翻译成平台能力和商业治理能力。

产出：

- LLM Gateway Demo V1。
- Prompt 版本与 Eval Harness 的联动说明。

### RAG 工程

目标：

- 理解 chunk、embedding、向量库、召回、重排、引用、RAG eval。
- 不追求底层算法推导，重点理解企业知识库上线后的质量闭环。

产出：

- RAG Evaluation Harness 最小链路。
- 标准问答集、引用可信度、召回命中、幻觉风险和文档版本回归指标。

### Agent 工程

目标：

- 理解 tool calling、MCP、LangGraph / Agent workflow、状态、权限、trace、human review。
- 能说明 Agent 失控不是只靠换模型解决，而要靠 harness、guardrails、trace 和回归。

产出：

- Agent Harness 的 tool registry、trace、失败归因和人工确认样例。

### Evals / Harness

目标：

- 建立测试集、LLM-as-judge、CI gate、bad case、回归测试、生产 trace 回流。
- 让项目从“能调用/能演示”升级到“可评测、可追踪、可回归、可持续优化”。

产出：

- Eval Harness 样例。
- 工具对比表。
- Harness 产品化后台方案。

### AI 辅助开发工作流

目标：

- 用 Codex / Claude Code / Cursor 做需求拆解、代码生成、测试、debug、文档和复盘。
- 学会给 AI 明确上下文、边界、验收标准和测试要求。

产出：

- 每个项目保留一段“AI 辅助开发复盘”：我让 AI 做了什么、我如何审查、哪些地方必须人工判断、如何用测试/eval 验证。

## 不学或降级

- 深度学习训练、PyTorch 训练大模型、分布式训练、CUDA、模型微调工程。
- 复杂前端框架深挖、算法刷题、云原生全家桶。
- 为了“看起来像全栈”而学太多与作品集无关的技术。
- 只做技术 Demo 但不能转成产品方案、质量指标、简历 bullet 或面试讲法的内容。

## 精选工程实践库

`/Users/fengyonglong/workspace/code/ai-engineering-from-scratch` 作为 AI Builder 精选工程实践库纳入，但不全量学习。

使用边界：

- P1：Phase 11 / 13 / 14 / 17 中和 LLM Gateway、Eval Harness、Agent Harness、LLMOps 直接相关的 lessons。
- P2：可补概念、补代码理解、补面试讲法的 lessons。
- P4：数学、训练、视觉、语音、RL、GPU/CUDA、复杂 serving 内核等暂不学。

学习方法：

1. 读 `docs/en.md` 的 Problem、Learning Objectives、Use It、Ship It。
2. 运行 `code/*.py` 或主入口文件，看输出指标。
3. 读关键类、输入输出、数据结构和决策逻辑。
4. 改一个参数、加一个 case、换一个策略或补一个失败场景。
5. 迁移到 LLM Gateway / RAG Evaluation Harness / Agent Harness，并写成复盘或面试讲法。

详细计划见 `ai-engineering-from-scratch-study-plan.md`。

## 6 个月产出映射

| 月份 | 技术能力补强 | 必须产出 |
| --- | --- | --- |
| 第 1 个月 | AI 辅助开发、Python/FastAPI、LLM API、测试 | LLM Gateway 小功能、测试、README、Eval Harness V0 |
| 第 2 个月 | RAG 工程、RAG eval、数据集和引用质量 | RAG Evaluation Harness 最小链路 |
| 第 3 个月 | Agent 工程、tool registry、trace、human review | Agent Harness 运行样例和失败归因样例 |
| 第 4 个月 | 简单前端/后台原型、产品化信息架构 | Harness 产品化后台可交互原型或轻量 Demo |
| 第 5 个月 | 作品集工程整理、代码仓库和面试演示 | PRD、代码、测试/eval、复盘、讲法打包 |
| 第 6 个月 | 面试和岗位匹配 | 用 AI Builder 能力解释“我能把需求推进到可运行、可评测的原型” |

## 每周节奏

- 工作日早上：技术产出优先，最多 1 个小功能或 1 个测试/eval 改进。
- 工作日晚上：只做复盘、简历表达或学习笔记，不安排重编码。
- 周六上午：集中打磨一个可演示项目能力。
- 周日上午：复盘技术学习是否转成项目、指标、简历和面试表达。

## 验收标准

每个 AI Builder 学习任务都必须同时满足：

- 有可运行或可交互产物。
- 有测试、eval、trace 或指标证明质量。
- 有产品解释：用户是谁、解决什么问题、为什么这样设计。
- 有面试表达：能用 3-5 分钟讲清楚。

如果只有代码没有产品解释，不算完成。如果只有产品文档没有可运行或可交互证据，也不算完成。
