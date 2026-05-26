# Harness 学习与面试笔记

## 这里说的 Harness 是什么

这里的 harness 指 Agent Harness / Evaluation Harness / Harness Engineering，不是 CI/CD 公司 Harness.io。

我的理解：

> Harness 是模型外面的工程环境。它负责给模型提供工具、状态、权限、反馈、评测、轨迹和失败恢复，让 LLM/RAG/Agent 不只是能演示，而是可测试、可排查、可迭代、可上线。

## 为什么值得加进准备计划

AI 项目上线后的问题，很多不是“模型不够强”，而是环境没有设计好：

- 没有可重复评测，所以不知道版本变更有没有变差。
- 没有 trace，所以 Agent 失败后不知道错在哪一步。
- 没有工具权限和参数约束，所以系统不可控。
- 没有 Bad Case 归因，所以优化只能靠感觉。
- 没有回归测试，所以知识库更新后旧问题可能答错。

## 三层项目表达

LLM Gateway：

- 提供调用治理。
- 关注路由、成本、稳定性、预算、Prompt 版本。

Eval Harness：

- 提供可重复评测。
- 关注测试集、批量运行、通过率、成本、耗时、fallback、失败归因。

Agent Harness：

- 提供 Agent 执行环境。
- 关注工具注册、状态管理、权限、轨迹、人工确认、失败恢复。

## 面试回答

如果面试官问你最近比较火的 harness 怎么看，可以这样答：

> 我不会把 harness 理解成某个单独框架，而是理解成模型外面的工程系统。企业 AI 项目里，模型只是推理能力，harness 决定这个能力如何被测试、约束、追踪和恢复。比如 LLM Gateway 是调用治理，Eval Harness 是可重复评测，Agent Harness 是工具、状态、权限、轨迹和失败恢复。很多 Agent 失败并不是换更强模型就能解决，而是工具定义、状态管理、终止条件、权限边界和反馈回路没有设计好。

## 项目落点

- 第 1 个月：LLM Gateway 增加 Eval Harness V0。
- 第 2 个月：RAG 项目升级为 RAG Evaluation Harness & Knowledge Governance。
- 第 3 个月：FDE 助手增加 Agent Harness Layer。
- 第 4 个月：制造业售后诊断 Agent 展示 Agent Harness 在垂直行业的落地。

## 参考资料

- OpenAI: https://openai.com/index/unlocking-the-codex-harness/
- OpenAI: https://openai.com/ms-BN/index/harness-engineering/
- Microsoft Research: https://www.microsoft.com/en-us/research/publication/auditing-agent-harness-safety/

