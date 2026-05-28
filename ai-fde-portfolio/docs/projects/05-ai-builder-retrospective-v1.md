# AI Builder 复盘 V1：LLM Gateway 质量治理包装

日期：2026-05-28

## 复盘对象

本次复盘对象不是从零写一个大而全项目，而是围绕 LLM Gateway 已有代码、测试和文档，用 AI 辅助把它包装成更能支撑 AI 平台产品经理面试的作品集材料。

目标：

- 把“API 中转 Demo”升级为“LLM Gateway / LLMOps 调用治理 + Eval Harness 质量门禁”。
- 把已有功能转成简历 bullet、项目复盘和 3/8/15 分钟面试讲法。
- 保持职业定位为 AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力，不转纯工程师。

## 需求

问题：

- 当前项目已有路由、fallback、日志、成本、预算、Prompt 版本和 Eval Harness。
- 但面试表达里还缺 baseline、rubric、regression、CI gate 这些能体现 Harness 产品深度的质量治理语言。
- 中期评测也指出，需要补 Eval Harness V0 的显式表达和 AI Builder 复盘。

验收标准：

- 项目复盘能解释 Eval Harness 如何做质量门禁。
- README 能说明 baseline、rubric、regression、CI gate。
- 简历 bullet 能体现可评测、可追踪、可回归。
- 面试材料有 3/8/15 分钟项目讲法。
- 本地测试通过。

## AI 辅助开发过程

我让 AI 做的事：

- 读取项目目标、LLM Gateway README、Eval Harness 代码、测试用例、简历和面试脚本。
- 从代码事实中提取已有能力：case、summary、trace、assertions、failure_breakdown、failure tag。
- 将代码事实翻译成产品语言：baseline、rubric、regression、CI gate、成本/质量/稳定性三角权衡。
- 更新项目复盘、README、简历 bullet 和面试讲法。

我人工判断的事：

- 不把未实现的功能写成已完成能力。
- 将 CI gate 写成“V0 门禁概念和下一步配置化”，避免夸大为完整 CI/CD 系统。
- 保留 AI Builder 定位，不把项目包装成纯工程师作品。
- 用市场 JD 样本验证 Agent、RAG、评测、工具调用和 AI Builder 方向确实值得强化。

## 测试与验证

本地验证：

- `python3 -m unittest discover -s tests`
- 结果：8 个测试通过。
- `python3 -m json.tool config/eval_policy.json`
- 结果：评测门禁策略 JSON 格式有效。

已有测试覆盖：

- low_cost 路由选择低价模型。
- provider 失败后 fallback 到备用模型。
- Prompt version 渲染业务上下文。
- usage summary 统计调用和成本。
- evaluation entrypoint 返回 pass rate 和 trace。
- Eval Harness 统计 fallback 和成本。
- Eval Harness 识别 quality_failure。
- Eval Harness 识别 prompt_failure。
- Eval Harness 根据 `config/eval_policy.json` 输出 `gate.decision`。

## 产品价值

这次 AI Builder 复盘证明的不是“会让 AI 写代码”，而是：

- 能基于真实代码和测试提炼产品能力。
- 能把技术输出转成平台治理语言。
- 能识别哪些能力已经实现，哪些仍是下一步计划。
- 能用测试和 eval 约束 AI 生成内容，避免把建议写成事实。

## 可写进简历的 bullet

- 使用 AI 辅助开发方式梳理 LLM Gateway 项目能力，基于现有代码、测试和 Eval Harness 输出，沉淀 baseline、rubric、regression、CI gate 等质量门禁表达，并转化为项目复盘、README、简历 bullet 和 3/8/15 分钟面试讲法。

## 面试表达

如果面试官问“你所谓 AI Builder 能力具体体现在哪里”，可以这样答：

> 我不会把 AI Builder 理解成让 AI 直接替我写完项目，而是让 AI 帮我在真实代码库里做需求拆解、材料整理、测试检查和表达转换。比如 LLM Gateway 这个项目，我先用代码和测试确认已有能力，再把 Eval Harness 的 case、summary、trace、failure tag 转成 baseline、rubric、regression、CI gate 的产品表达。这个过程里，我会人工判断哪些是已实现，哪些只是下一步，最后再用测试和文档复盘证明它不是空泛包装。
