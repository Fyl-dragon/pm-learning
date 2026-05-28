# Week 1 中期学习效果评测

日期：2026-05-28

评测范围：`2026-05-25` 到 `2026-05-28` 的 Week 1 中期进展。

## 项目已确认事实

- 当前主线是：AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力。
- Week 1 原计划覆盖岗位画像、LLM Gateway 最小链路、调用日志、成本统计、Eval Harness 雏形、模型路由、fallback、限流预算和项目包装。
- 本地已有 LLM Gateway 代码、测试、README、项目复盘、简历草稿、面试表达、JD 分析表和学习资料优先级文档。
- 2026-05-28 本地验证结果：`python3 -m unittest discover -s tests` 通过，8 个测试全部 OK。
- 2026-05-28 本地验证结果：`python3 -m app.cli_demo` 可输出一次完整调用结果和应用用量统计。

## 评分

| 维度 | 分数 0-5 | 证据 | 改进动作 |
| --- | --- | --- | --- |
| 计划完成度 | 3 | LLM Gateway、Eval Harness、README、复盘和面试材料已有；但 Week 1 要求的 5-8 个真实 JD 还没有补齐，目前只有样例行 | 本周日前补 5 个真实岗位样本，替换样例行 |
| 产出物质量 | 4 | `projects/llm-gateway` 可运行，8 个测试通过；`01-llm-gateway-case-study.md` 能解释治理价值 | 把 Eval Harness 的 baseline、rubric、regression、CI gate 写进项目复盘和 README |
| AI 产品思考深度 | 4 | 已从普通 API 中转上升到路由、fallback、成本、预算、Prompt 版本、Eval Harness 和失败归因 | 增加“成本、质量、稳定性三角权衡”指标表，避免只列功能 |
| 面试/简历转化 | 4 | `resume-v1.md` 有标题、定位和 bullet；`interview-scripts.md` 有 Harness、FDE、AI Builder 讲法 | 为 LLM Gateway 增加 3 分钟、8 分钟、15 分钟三个版本的讲法 |
| 岗位匹配度 | 3 | 职业方向和关键词已经清晰，但真实市场证据还薄，JD 分析表未形成样本 | 用重庆/远程/成都可考虑岗位补齐 5 个样本，标注来源和日期 |
| 下步清晰度 | 4 | Week 1 和 Month 1 已有明确任务，rohitg00 精选学习法已落库 | 把下周三件事写成可验收动作，不再新增资料 |

总分：22 / 30

判断：这是一个有价值的中期进展。当前最大的优势是项目已经从“学习计划”推进到了可运行代码、测试、复盘和面试表达；最大的短板是真实岗位样本和学习效果记录还不够硬，容易让职业定位看起来像自我判断，而不是市场需求倒推。

## 本周最有价值产出

LLM Gateway / LLMOps Mini Platform 已经具备作品集雏形：

- 能运行核心 Demo。
- 能通过标准库测试。
- 能解释多模型路由、fallback、成本、预算和 Prompt 版本。
- 能把 Eval Harness 讲成质量治理入口，而不是普通测试脚本。
- 能作为 AI Builder 证据，证明你不是只写产品文档，也能把需求推进到可运行原型和测试。

## 最大短板

真实市场样本不足。

当前 `career/jd-analysis.md` 还是样例行，不能证明“这些能力确实对应岗位需求”。这会影响两件事：

- 学习路线是否真的贴近招聘市场。
- 简历 bullet 是否能命中岗位关键词。

2026-05-28 追加进展：

- 已补充 `career/jd-analysis.md` 的 6 个岗位样本，覆盖重庆、成都和远程。
- 已新增 `career/market-snapshot-2026-05-28-ai-pm-jd.md`，把样本要求映射到学习路线、作品集和简历包装。
- 已补充 LLM Gateway 的 baseline、rubric、regression、CI gate 表达，并新增 3/8/15 分钟项目讲法。
- 已新增 `docs/projects/05-ai-builder-retrospective-v1.md`，作为 AI Builder 复盘 V1。
- 已新增 `career/portfolio-evidence-matrix.md`，把目标能力、市场证据、项目资产、简历/面试用法和证据缺口串起来。
- 已新增 `projects/llm-gateway/config/eval_policy.json` 并接入 Eval Harness 输出，支持 `gate.decision` 的 `allow` / `review` / `block` 判断。
- 已新增 `docs/projects/06-llm-gateway-eval-gate-report.md`，用 before/after 样例展示基线 `allow` 和质量回归 `block`。
- 样本仍然有限，后续需要每周继续补 5 个真实 JD。

## 下周前三件事

1. 补齐 5 个真实 JD 样本。
   - 验收：`career/jd-analysis.md` 至少有 5 行真实岗位，包含来源、日期、城市、薪资、能力要求和是否投递。

2. 强化 Eval Harness V0。
   - 验收：LLM Gateway README 和项目复盘新增 baseline、rubric、regression、CI gate 四个概念，并能说明它们如何避免模型/Prompt 更新后质量倒退。

3. 增加 AI Builder 复盘 V1。
   - 验收：写清楚一次“需求 -> AI 辅助开发 -> 人工审查 -> 测试/eval -> 产品表达”的过程，至少包含一个测试结果和一个面试 bullet。

## 监督规则

- 周日前不新增学习资料。
- 每学一个 rohitg00 lesson，必须留下运行输出摘要、代码结构理解、项目迁移点和面试表达。
- 如果一个任务不能转成项目、简历或面试表达，本周暂停。
- 未经明确要求，不创建自动提醒；如果后续要求监督，默认每周日上午复盘。
