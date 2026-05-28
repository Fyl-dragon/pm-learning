# AI PM 作品集证据矩阵

日期：2026-05-28

## 用途

这份矩阵用来回答一个核心问题：

> 当前项目里的哪些材料，已经能证明“AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力”？哪些还只是计划，需要补证据？

使用方式：

- 改简历时，从“可写进简历”列提取 bullet。
- 准备面试时，从“面试讲法”列选择 2/5/8/15 分钟讲法。
- 做周复盘时，只补“证据缺口”和“下一步产出”，不再盲目新增资料。
- 投递岗位前，对照 JD 要求，把证据强的能力放前面，把证据弱的能力标为后续计划。

## 总体结论

| 方向 | 当前证据强度 | 判断 |
| --- | --- | --- |
| LLM Gateway / LLMOps 调用治理 | 强 | 已有代码、测试、README、项目复盘、简历 bullet 和 3/8/15 分钟讲法 |
| Eval Harness / 质量门禁 | 强 | 已有 V0 代码、策略配置、测试、本地 CI gate 脚本、before/after 报告和表达，能讲 baseline、rubric、regression、CI gate、release decision；还缺真实 CI 执行记录 |
| AI Builder 能力 | 中强 | 已有代码、测试、AI Builder 复盘 V1；还需要继续保留每次迭代的复盘记录 |
| 市场/JD 证据 | 中 | 已有 6 个岗位样本和 1 个薪资样本；样本有限，需要每周继续补充 |
| RAG Evaluation Harness | 弱到中 | 有设计 brief 和路线，但缺可运行最小链路 |
| Agent Harness | 弱到中 | 有设计 brief 和面试逻辑，但缺 tool registry / trace / eval case 的可运行样例 |
| 行业场景包装 | 弱 | 有制造业售后诊断 Agent brief，但还缺具体流程、数据样例和原型 |

## 能力到证据矩阵

| 目标能力 | 市场证据 | 当前项目证据 | 可写进简历 | 面试讲法 | 证据缺口 | 下一步产出 |
| --- | --- | --- | --- | --- | --- | --- |
| AI 平台产品 / LLM Gateway | 重庆/成都样本要求平台、API/SDK、多租户、治理、Agent 平台 | `projects/llm-gateway/`、`01-llm-gateway-case-study.md`、`projects/llm-gateway/README.md` | 设计多模型统一调用入口，支持路由、fallback、调用日志、成本统计和预算限流 | 3/8/15 分钟 LLM Gateway 项目讲法 | 缺开发者接入、权限/审计和 API/SDK 产品文档 | 补一页“开发者接入与权限治理方案” |
| Eval Harness / 质量门禁 | 岗位样本多次出现评测指标、失败案例、数据评估、模型评估 | `app/eval_harness.py`、`config/eval_policy.json`、`scripts/run_eval_gate.py`、测试用例、README 门禁概念、`06-llm-gateway-eval-gate-report.md` | 设计批量评测 case 和 Eval Harness V0，输出 pass rate、成本、耗时、fallback、trace、失败归因和 gate decision，并定义 baseline/rubric/regression/CI gate | Eval Harness 不是普通测试脚本，而是评估模型外部环境、版本回归和发布门禁 | 缺真实 CI 执行记录 | 增加 GitHub Actions 或本地执行截图/记录 |
| AI Builder / AI-assisted development | 重庆 AI 应用工程样本要求 RAG、Agent、Prompt、框架选型，说明技术理解能抬高议价 | `05-ai-builder-retrospective-v1.md`、LLM Gateway 测试结果、代码和 README | 使用 AI 辅助开发方式推进功能迭代、测试补充和文档复盘，形成需求到测试/eval再到产品表达的闭环 | AI Builder 不是让 AI 代写，而是在真实代码库中做需求拆解、测试检查和表达转换 | 缺连续多次迭代记录 | 每个项目新增一份 AI Builder 复盘 |
| RAG Evaluation Harness | 4/6 样本出现 RAG、知识库、上下文治理 | `02-rag-quality-governance-brief.md`、6 个月路线第 2 月 | 暂不写成已完成项目，可写为“规划 RAG 质量治理项目” | 企业知识库上线难点不是搭 Demo，而是标准问答集、召回、引用、版本回归和 bad case 闭环 | 缺可运行链路、标准问答集、指标表 | 做 RAG Evaluation Harness 最小链路 |
| Agent Harness / Agent 平台产品 | 5/6 样本出现 Agent、智能体、工具调用、工作流、Agent 平台 | `03-agent-harness-brief.md`、Harness 面试笔记、市场快照 | 暂不写成已完成项目，可作为下一阶段项目方向 | Agent 不是会调用工具就行，而是要 tool registry、状态、权限、trace、human review 和失败恢复 | 缺 tool registry、trace 样例、eval case | 做 Agent Harness V0：tool schema、trace、失败归因 |
| 行业 AI 场景 | 重庆本地机会偏制造业、政企、企业服务；当前背景有现场交付经验 | `04-manufacturing-diagnosis-agent-brief.md` | 可包装为“能把客户现场 bad case 转成评测集和质量治理流程” | 不做泛维修问答助手，要讲诊断路径、人工升级、工单闭环、工具轨迹和知识库回归 | 缺具体业务流程和样例数据 | 写制造业售后诊断 Agent 的流程图和 case 数据 |
| 职业定位和筛选 | 市场快照显示本地 Agent 平台机会存在，成都/远程薪资上限更高 | `direction-strategy.md`、`jd-analysis.md`、`market-snapshot-2026-05-28-ai-pm-jd.md` | AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力 | 主线不是 AI 全栈，也不是泛 FDE，而是技术型 AI 平台 PM | 样本少，薪资判断需持续更新 | 每周补 5 个真实 JD，并标注是否投递 |

## 作品集资产清单

| 资产 | 状态 | 用途 | 下一步 |
| --- | --- | --- | --- |
| LLM Gateway 代码 | 已有 | 证明能把平台产品需求推进到可运行原型 | 继续补门禁策略和 API/SDK 文档 |
| LLM Gateway README | 已有 | 面试前快速展示项目能力 | 增加截图或示例 eval 输出摘要 |
| LLM Gateway 项目复盘 | 已有 | 作品集文章和面试讲法来源 | 补开发者接入、权限/审计视角 |
| Eval Harness V0 | 已有 | 证明质量治理意识 | 增加真实 CI 执行记录 |
| AI Builder 复盘 V1 | 已有 | 证明 AI 辅助开发不是口号 | 每个后续项目继续补复盘 |
| 简历 V1 | 已有 | 投递前基础版本 | 根据目标岗位裁剪 2 个版本：平台 PM / Agent 产品 |
| 面试脚本 | 已有 | 2/3/8/15 分钟讲法和高频问答 | 增加面试官追问清单 |
| 市场快照 | 已有但样本有限 | 校准学习路线和薪资目标 | 每周更新真实 JD |
| RAG Evaluation Harness brief | 设计中 | 第 2 月项目方向 | 做可运行最小链路 |
| Agent Harness brief | 设计中 | 第 3 月项目方向 | 做 tool registry 和 trace 样例 |

## 当前最适合投递时的表达顺序

如果投递 AI 平台产品 / 大模型平台产品：

1. 大模型中转平台现职经验。
2. LLM Gateway / LLMOps Mini Platform 项目。
3. Eval Harness V0 和质量门禁。
4. AI Builder 能力。
5. RAG/Agent Harness 作为下一阶段规划。

如果投递 Agent 平台 / 智能体产品：

1. Agent Harness 理解：工具、状态、权限、trace、human review。
2. LLM Gateway 作为调用治理底座。
3. Eval Harness 作为 Agent 质量治理基础。
4. RAG/知识库质量治理规划。
5. 现场交付经验转 bad case 和评测集。

如果投递 AI 解决方案产品：

1. 软件工程 + 产品 + 现场交付背景。
2. LLM Gateway 证明平台理解。
3. 行业场景 brief 证明业务抽象能力。
4. Harness 证明不会只做一次性交付，而能沉淀平台能力。
5. 谨慎过滤纯驻场、售前和交付救火岗位。

## 本周补证据优先级

1. 给 LLM Gateway 增加真实 CI 执行记录或 GitHub Actions 示例，把本地 gate 脚本变成工程化流程。
2. 给 Agent Harness 写 tool registry 和 trace 样例，不急着做完整项目。
3. 给简历裁剪两个版本：AI 平台产品版、Agent 平台产品版。
4. 每周继续补 5 个真实 JD，避免路线脱离市场。
