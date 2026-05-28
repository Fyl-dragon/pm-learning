# Week 1 执行表：2026-05-25 到 2026-05-31

## 周一：岗位画像 + 项目设计

早上：

- 分析 5 个岗位 JD。
- 记录高频能力：RAG、Agent、解决方案、Python、Java、交付、客户沟通、模型平台。
- 画 LLM Gateway 项目架构草图。

晚上：

- 写简历标题和个人定位。

产出：

- `career/jd-analysis.md`
- `docs/projects/01-llm-gateway-case-study.md`
- `career/resume-v1.md`

## 周二：LLM Gateway 最小链路

早上：

- 跑通统一模型调用入口。
- 支持至少 2 个模型配置。

晚上：

- 记录接口参数和响应结构。
- 写 3 条简历 bullet。

产出：

- `projects/llm-gateway/app/gateway.py`
- `projects/llm-gateway/examples/chat_request.json`

## 周三：调用日志 + 成本统计 + Eval Harness 雏形

早上：

- 记录应用、模型、provider、耗时、状态、token、费用。
- 增加批量评测返回结构：summary、results、trace。
- 对照 rohitg00 Phase 11 `10-evaluation`，只看 eval case、baseline、rubric、regression、CI gate 能迁移到本项目的部分。

晚上：

- 写“为什么 AI 平台必须做日志和成本统计”的面试表达。

产出：

- `projects/llm-gateway/app/database.py`
- `projects/llm-gateway/app/eval_harness.py`
- `career/interview-scripts.md`

## 周四：模型路由 + 失败重试 + 失败归因

早上：

- 实现 default、low_cost、fastest、balanced 路由。
- 实现失败后 fallback。
- Eval Harness 记录 fallback 次数和失败标签。

晚上：

- 写“模型路由如何降低成本、提升可用性”的面试表达。

产出：

- 核心测试通过
- 项目讲法初稿

## 周五：限流和预算雏形

早上：

- 应用级 QPS 限制。
- 月度预算与降级模型。

晚上：

- 整理 README 初稿。

产出：

- `projects/llm-gateway/README.md`

## 周六上午：项目集中打磨

任务：

- 串联调用、路由、fallback、日志、统计。
- 补演示请求。
- 形成项目演示材料。
- 跑一批 eval cases，确认通过率、成本、耗时、fallback、失败归因都有输出。

验收：

- `python3 -m unittest discover -s tests` 通过。

## 周日上午：复盘 + 简历化

复盘问题：

- 本周实际完成了什么？
- 哪个功能最能体现平台价值？
- 哪个功能还只是玩具级？
- 面试时这个项目怎么讲才不像 Demo？
- harness 和普通测试脚本的区别是什么？
- 本周看的资料是否有明确优先级、章节、语言门槛和产出物？
- 本周是否有 AI Builder 证据：代码/原型、测试/eval、AI 辅助开发复盘？
- rohitg00 lesson 是否留下了运行输出摘要、代码结构理解、项目迁移点和面试表达？
- 下周要补哪 3 个关键点？

## 本周复盘区

- 完成：
- 卡点：
- 下周三件事：
- 简历新增表达：
- 当前公司观察：
- 资料学习产出：
- AI Builder 产出：
- 评测记录：`ai-fde-portfolio/evaluations/2026-05-28-week-01-midweek-review.md`
