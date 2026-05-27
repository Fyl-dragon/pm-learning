# AI Harness / LLMOps 学习资料优先级

日期：2026-05-27

## 选择原则

后续学习资料不再按“平台热不热、资料多不多”来选，而是按下面顺序筛选：

1. 中文优先：中文、中文翻译、中文文档优先；英文资料如果没有明确中文入口或字幕，默认降级。
2. 短路径优先：优先选具体课程、章节、仓库指南，不推荐泛泛的产品官网或课程平台总入口。
3. 作品集优先：资料必须能转成产品方案、评测指标、bad case、简历 bullet 或面试讲法。
4. 当前主线优先：优先服务 AI Evals / Harness / LLMOps、大模型平台产品、RAG/Agent 质量治理。
5. 低成本优先：免费和低成本资料优先；付费资料只有明显节省时间且能产出成果时才考虑。

## 优先级清单

| 优先级 | 资料 | 是否纳入 | 具体学习范围 | 语言门槛 | 产出物 | 取舍理由 |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | [Datawhale LLM Cookbook](https://github.com/datawhalechina/llm-cookbook) | 必须纳入 | Prompt Engineering、Building Systems、RAG、评估改进生成式 AI、搭建和评估高级 RAG 应用 | 中文为主 | 1 页基础能力笔记、Prompt/RAG/eval 能力地图、简历 bullet 草稿 | 中文资料，已对吴恩达大模型课程做筛选、翻译、复现和排序，适合先补基础 |
| P0 | [Datawhale Happy-LLM 第 7 章大模型应用](https://github.com/datawhalechina/happy-llm) | 必须纳入 | 只学第 7 章：模型评测、RAG 检索增强、Agent 智能体 | 中文为主 | LLM 评测/RAG/Agent 概念卡片、RAG Evaluation Harness 指标草案 | 中文、免费、系统性强；跳过训练大模型主线，避免偏工程研究 |
| P1 | [Hugging Face Agents Course 中文版](https://hugging-face.cn/learn/agents-course/unit0/introduction) | 纳入 | 单元 1、单元 2.3 LangGraph、单元 3 Agentic RAG、附加单元 2 代理可观测性和评估、最终项目 | 中文页面 | Agent Harness 产品拆解、Agent failure mode 清单、3-5 分钟面试讲法 | 有中文入口，结构清楚，Agent Harness 方向适配度高 |
| P1 | [promptfoo Eval Guides](https://www.promptfoo.dev/docs/guides/) | 纳入 | Getting Started、prompt eval、RAG eval、LLM-as-judge、CI/CD gate | 英文短文档 | 最小 Eval Harness 样例、测试集、评分规则、发布门禁说明 | 直接对应 Eval Harness，最容易转成作品集 |
| P1 | [Langfuse GitHub / Docs](https://github.com/langfuse/langfuse) | 纳入但不学整个平台 | traces、datasets、experiments、evals、prompt management | 英文为主，有中文 README | Langfuse 产品能力拆解表、信息架构草图、竞品对比 | 作为产品拆解对象，看它如何把观测、评测、提示词管理做成平台能力 |
| P2 | [OpenAI Evals](https://github.com/openai/evals) | 选择性纳入 | examples、eval templates、custom/private eval 概念 | 英文、偏工程 | eval template 概念卡、与 promptfoo/Langfuse 的定位对比 | 官方框架，适合建立评测体系认知，但不作为主课 |
| P2 | [DeepLearning.AI Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents/) | 可选纳入 | tracing、router eval、trajectory eval、LLM-as-judge、monitoring | 英文视频；中文字幕未确认，学习前先确认字幕或 transcript | Agent eval 指标表、trajectory eval 面试讲法 | 内容很贴 Agent Harness，但语言门槛高，默认不放主线 |
| P3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 只做参考库 | Phase 11 Evaluation、Phase 14 Agent Observability / Eval-driven Agent、Phase 17 AI Gateway / LLM Observability | 英文、工程化很重 | 遇到具体问题时摘录为技术背景，不安排连续学习 | 方向相关但体量过大，不能全量纳入产品学习计划 |
| P3 | Phoenix / DeepEval / RAGAS | 只做工具横评 | 指标、数据集、实验记录、RAG eval 能力 | 英文为主 | Eval Harness 工具对比表 | 不作为学习主线，只用于竞品/工具横评 |
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

### 第 3 阶段：Agent Harness

学 Hugging Face Agents Course 中文版，范围限定为 Agent 基础、LangGraph、Agentic RAG、代理可观测性和评估。

验收产出：

- Agent failure mode 清单。
- Agent trace / recovery / human review 产品流程。
- 3-5 分钟 Agent Harness 面试讲法。

### 第 4 阶段：产品拆解

拆 Langfuse、OpenAI Evals、promptfoo，不看源码细节，重点看产品能力、信息架构、指标体系、用户流程、权限和报表。

验收产出：

- Eval Harness 工具对比表。
- Harness 产品化后台功能清单。
- 产品方案或 PRD 片段。

### 第 5 阶段：rohitg00 作为查漏补缺

只在遇到具体问题时查对应章节，不安排连续学习，不允许挤占项目产出时间。

验收产出：

- 只摘录与 LLM Gateway、Eval Harness、Agent Harness 直接相关的背景点。
- 每次引用都必须转成项目说明、面试讲法或产品取舍。

## 每周投入上限

- 学习资料：2-4 小时。
- 项目产出、复盘、简历和面试表达：优先级高于资料学习。
- 如果一份资料连续 2 次学习后没有产出物，暂停该资料，回到项目问题本身。

## 资料纳入检查

每个资料只有满足下面条件，才算真正纳入学习计划：

- 有具体入口，不是泛平台。
- 有明确学习范围，不要求全量学习。
- 有语言门槛说明。
- 有学习时长或投入上限。
- 有可验收产出。
- 能连接到 AI 平台产品 / AI Evals & Harness 职业定位。

## 后续推荐约束

以后 AI 推荐课程、仓库、文档或视频时，必须先说明：

- 优先级：P0 / P1 / P2 / P3 / P4。
- 是否主线：主线、辅助、参考库、工具横评或排除。
- 中文可学性：中文、中文翻译、英文短文档、英文视频、字幕未确认。
- 具体学习范围：章节、单元、文档页或样例，不允许只给产品首页。
- 产出物：学习后必须交付什么。

如果无法说明这些信息，不推荐该资料。
