# AI Harness / LLMOps 学习资料优先级

日期：2026-05-28

## 选择原则

后续学习资料不再按“平台热不热、资料多不多”来选，而是按下面顺序筛选：

1. 中文优先：中文、中文翻译、中文文档优先；英文资料如果没有明确中文入口或字幕，默认降级。
2. 短路径优先：优先选具体课程、章节、仓库指南，不推荐泛泛的产品官网或课程平台总入口。
3. 作品集优先：资料必须能转成产品方案、评测指标、bad case、简历 bullet 或面试讲法。
4. 当前主线优先：优先服务 AI Evals / Harness / LLMOps、大模型平台产品、RAG/Agent 质量治理。
5. 低成本优先：免费和低成本资料优先；付费资料只有明显节省时间且能产出成果时才考虑。
6. AI Builder 补强：技术资料必须服务产品原型、LLM 应用 Demo、Eval Harness、RAG/Agent 质量治理工具，不把路线带偏成纯全栈工程师。

## 优先级清单

| 优先级 | 资料 | 是否纳入 | 具体学习范围 | 语言门槛 | 产出物 | 取舍理由 |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | [Datawhale LLM Cookbook](https://github.com/datawhalechina/llm-cookbook) | 必须纳入 | Prompt Engineering、Building Systems、RAG、评估改进生成式 AI、搭建和评估高级 RAG 应用 | 中文为主 | 1 页基础能力笔记、Prompt/RAG/eval 能力地图、简历 bullet 草稿 | 中文资料，已对吴恩达大模型课程做筛选、翻译、复现和排序，适合先补基础 |
| P0 | [Datawhale Happy-LLM 第 7 章大模型应用](https://github.com/datawhalechina/happy-llm) | 必须纳入 | 只学第 7 章：模型评测、RAG 检索增强、Agent 智能体 | 中文为主 | LLM 评测/RAG/Agent 概念卡片、RAG Evaluation Harness 指标草案 | 中文、免费、系统性强；跳过训练大模型主线，避免偏工程研究 |
| P0 | [Datawhale LLM Universe](https://github.com/datawhalechina/llm-universe) | 必须纳入 | 大模型应用开发、LLM API、RAG 应用和工程化实践相关章节 | 中文为主 | 可运行 LLM/RAG 小样例、项目 README、AI Builder 复盘 | 中文、动手实践导向，适合把产品方案推进到可运行 Demo |
| P1 | [FastAPI 中文文档](https://fastapi.tiangolo.com/zh/) | 纳入 | Path Operation、Request Body、Response、Exception、Testing | 中文页面 | LLM Gateway API 小功能、接口说明、测试用例 | 只补 API 后端能力，不深挖复杂后端工程 |
| P1 | [Hugging Face Agents Course 中文版](https://hugging-face.cn/learn/agents-course/unit0/introduction) | 纳入 | 单元 1、单元 2.3 LangGraph、单元 3 Agentic RAG、附加单元 2 代理可观测性和评估、最终项目 | 中文页面 | Agent Harness 产品拆解、Agent failure mode 清单、3-5 分钟面试讲法 | 有中文入口，结构清楚，Agent Harness 方向适配度高 |
| P1 | [promptfoo Eval Guides](https://www.promptfoo.dev/docs/guides/) | 纳入 | Getting Started、prompt eval、RAG eval、LLM-as-judge、CI/CD gate | 英文短文档 | 最小 Eval Harness 样例、测试集、评分规则、发布门禁说明 | 直接对应 Eval Harness，最容易转成作品集 |
| P1 | [Langfuse GitHub / Docs](https://github.com/langfuse/langfuse) | 纳入但不学整个平台 | traces、datasets、experiments、evals、prompt management | 英文为主，有中文 README | Langfuse 产品能力拆解表、信息架构草图、竞品对比 | 作为产品拆解对象，看它如何把观测、评测、提示词管理做成平台能力 |
| P1 | 本项目 LLM Gateway 代码库 | 必须纳入 | app、tests、config、README；每次只改一个小功能或一组测试 | 中文项目上下文 | 代码改动、测试结果、产品复盘、简历 bullet | 最贴近你的当前履历，能直接形成 AI Builder 证据 |
| P2 | [OpenAI Evals](https://github.com/openai/evals) | 选择性纳入 | examples、eval templates、custom/private eval 概念 | 英文、偏工程 | eval template 概念卡、与 promptfoo/Langfuse 的定位对比 | 官方框架，适合建立评测体系认知，但不作为主课 |
| P2 | [Model Context Protocol Docs](https://modelcontextprotocol.io/docs/getting-started/intro) | 选择性纳入 | MCP 概念、tools、resources、client/server 边界 | 英文短文档 | Agent tool registry / MCP 产品概念卡 | 只服务 Agent Harness，不做协议实现深挖 |
| P2 | AI 辅助开发工具官方资料：Codex / Claude Code / Cursor | 选择性纳入 | 项目上下文、任务拆解、测试、debug、代码审查、变更复盘 | 英文为主 | AI 辅助开发复盘模板和一次真实项目复盘 | 学工作流，不追工具崇拜；必须绑定本项目产出 |
| P1 | [rohitg00/ai-engineering-from-scratch 精选 Phase 11/13/14/17](https://github.com/rohitg00/ai-engineering-from-scratch) | 精选纳入 | Phase 11 Evaluation/RAG/Guardrails/MCP/LangGraph；Phase 13 Tool Interface/Schema/MCP/OpenTelemetry；Phase 14 Agent Loop/Observability/Failure Modes/Eval-driven Agent；Phase 17 Model Routing/AI Gateways/Observability/FinOps | 英文、工程化较重；本地仓库已克隆 | 运行输出摘要、代码结构理解、项目迁移点、简历 bullet 或 3 分钟面试讲法 | 本地 README 显示 473 lessons、20 phases、约 320 小时，最近提交为 2026-05-27；质量和新鲜度较高，适合作为 AI Builder 精选实践库，但不全量学习 |
| P2 | [DeepLearning.AI Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents/) | 可选纳入 | tracing、router eval、trajectory eval、LLM-as-judge、monitoring | 英文视频；中文字幕未确认，学习前先确认字幕或 transcript | Agent eval 指标表、trajectory eval 面试讲法 | 内容很贴 Agent Harness，但语言门槛高，默认不放主线 |
| P2 | rohitg00/ai-engineering-from-scratch 其他相关 lessons | 选择性查阅 | 可补概念、补代码理解、补面试讲法的 lesson | 英文、工程化较重 | 只摘录能迁移到项目的技术点 | 遇到具体项目问题时作为工程实践字典，不做连续学习 |
| P3 | Phoenix / DeepEval / RAGAS | 只做工具横评 | 指标、数据集、实验记录、RAG eval 能力 | 英文为主 | Eval Harness 工具对比表 | 不作为学习主线，只用于竞品/工具横评 |
| P4 | rohitg00/ai-engineering-from-scratch 中与当前主线无关的部分 | 不纳入 | 数学、深度学习训练、视觉、语音、RL、分布式推理、GPU/CUDA、复杂 serving 内核 | 英文、投入极大 | 无 | 与 AI 平台产品 / Harness / AI Builder 作品集收益不匹配，暂不学习 |
| P4 | 复杂前端框架、算法刷题、云原生全家桶、模型训练课程 | 不纳入 | 不作为当前主线 | 多数投入大 | 无 | 与当前 AI PM 作品集收益不匹配，容易偏离产品主线 |
| P4 | DeepLearning.AI 全部课程库 | 不纳入 | 不学整个课程库 | 英文居多 | 无 | 入口太大、筛选成本高，会干扰当前主线 |

## 学习顺序

### 第 1 阶段：中文基础补齐

先学 Datawhale LLM Cookbook 的必修内容，再补“评估改进生成式 AI”和“搭建和评估高级 RAG 应用”。同时只读 Happy-LLM 第 7 章应用部分，用来补 LLM 评测、RAG、Agent 的共同语言。

验收产出：

- 一页中文学习笔记。
- LLM 应用产品能力地图。
- 3 条能放进简历或面试的技术理解表达。

### 第 2 阶段：Eval Harness 上手

用 promptfoo 做一个最小评测集，覆盖测试用例、评分规则、模型对比、失败样例和 CI gate 概念。

验收产出：

- 一个最小 Eval Harness 样例。
- 一张 eval 指标表。
- 一组 bad case / golden dataset 示例。

### 第 3 阶段：AI Builder 最小开发能力

用 Datawhale LLM Universe、FastAPI 中文文档和本项目 LLM Gateway 代码库补齐 AI 辅助开发能力，只做与项目有关的小功能、接口、测试和 README。

验收产出：

- 一个 LLM Gateway API 或 eval 小功能。
- 一组测试用例。
- 一段 AI 辅助开发复盘：需求、AI 生成、人工审查、测试结果、产品价值。

### 第 4 阶段：Agent Harness

学 Hugging Face Agents Course 中文版，范围限定为 Agent 基础、LangGraph、Agentic RAG、代理可观测性和评估。

验收产出：

- Agent failure mode 清单。
- Agent trace / recovery / human review 产品流程。
- 3-5 分钟 Agent Harness 面试讲法。

### 第 5 阶段：产品拆解

拆 Langfuse、OpenAI Evals、promptfoo，不看源码细节，重点看产品能力、信息架构、指标体系、用户流程、权限和报表。

验收产出：

- Eval Harness 工具对比表。
- Harness 产品化后台功能清单。
- 产品方案或 PRD 片段。

### 第 6 阶段：rohitg00 精选工程实践

按 `ai-engineering-from-scratch-study-plan.md` 的前 4 周计划精选学习，不全量学习，不允许挤占项目产出时间。学习方式固定为“读目标 -> 跑代码 -> 读关键结构 -> 改一处 -> 迁移到项目”。

验收产出：

- 每个 lesson 留下运行输出摘要。
- 每个 lesson 写清输入、处理、输出、关键决策。
- 每个 lesson 必须连接到 LLM Gateway、RAG Evaluation Harness 或 Agent Harness。
- 每个 lesson 转成 1 条简历 bullet 或 1 段 3 分钟面试讲法。

## 每周投入上限

- 学习资料：2-4 小时。
- 项目产出、复盘、简历和面试表达：优先级高于资料学习。
- 如果一份资料连续 2 次学习后没有产出物，暂停该资料，回到项目问题本身。
- AI Builder 技术学习不能挤占 Harness/Evals 主线；每周最多 1 个小功能或 1 组测试/eval 改进。

## 资料纳入检查

每个资料只有满足下面条件，才算真正纳入学习计划：

- 有具体入口，不是泛平台。
- 有明确学习范围，不要求全量学习。
- 有语言门槛说明。
- 有学习时长或投入上限。
- 有可验收产出。
- 能连接到 AI 平台产品 / AI Evals & Harness 职业定位。
- 如果是开发技术资料，必须能连接到 AI Builder 产出：可运行原型、测试/eval、项目复盘或面试讲法。

## 后续推荐约束

以后 AI 推荐课程、仓库、文档或视频时，必须先说明：

- 优先级：P0 / P1 / P2 / P3 / P4。
- 是否主线：主线、辅助、参考库、工具横评或排除。
- 中文可学性：中文、中文翻译、英文短文档、英文视频、字幕未确认。
- 具体学习范围：章节、单元、文档页或样例，不允许只给产品首页。
- 产出物：学习后必须交付什么。
- 分类：产品主线资料、AI Builder 技术补强资料、市场/职业资料、参考库或排除。

如果无法说明这些信息，不推荐该资料。

## rohitg00 仓库使用约束

- 不照抄全量代码。
- 不只运行一次看结果。
- 代码小于 150 行且是核心概念时，可以照敲关键结构；照敲后必须关掉原文复述设计。
- 每次学习必须改一个参数、加一个 case、换一个策略或补一个失败场景。
- 只运行不复盘不算完成。
- 数学、训练、视觉、语音、RL、GPU/CUDA 等内容默认 P4。
