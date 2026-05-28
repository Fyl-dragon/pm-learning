# 第 1 个月执行计划：LLM Gateway + Eval Harness V0

周期：2026-05-24 到 2026-06-23。

## 本月目标

直接做一个能讲进面试的大模型平台项目，避免停留在“调用 API”的层次。本月新增 harness 表达：让项目具备可重复评测、trace 和失败归因。

验收结果：

- LLM Gateway Demo V1
- Eval Harness V0
- 简历 V1
- 大模型平台项目复盘 V1
- 20 个岗位 JD 分析
- 2 分钟自我介绍
- 5 分钟项目讲解，包含 harness 和普通 API 中转的区别
- RAG 质量治理项目设计草图
- AI Builder 复盘 V1：本月至少记录一次“需求 -> AI 辅助开发 -> 人工审查 -> 测试/eval -> 产品表达”的过程

## 本月学习资料边界

本月只学习能直接帮助 LLM Gateway + Eval Harness V0 的资料，不扩展泛 AI 工程课程。

- P0：Datawhale LLM Cookbook 的 Prompt Engineering、Building Systems、评估改进生成式 AI。
- P0：Datawhale LLM Universe 的大模型应用开发、LLM API、RAG 应用和工程化实践相关章节。
- P1：FastAPI 中文文档的 API、请求/响应、异常、测试相关章节。
- P1：promptfoo Getting Started、prompt eval、LLM-as-judge、CI/CD gate。
- P1：rohitg00/ai-engineering-from-scratch 精选 Phase 11 `10-evaluation`，只服务 Eval Harness V0；按“读目标 -> 跑代码 -> 读关键结构 -> 改一处 -> 迁移项目”完成。

验收方式：

- 每次学习后必须补到项目 README、Eval Harness 指标表、项目复盘或面试讲稿里。
- 每次技术学习后必须留下可运行改动、测试/eval 或 AI Builder 复盘，避免只看资料。
- 如果资料只增加概念但没有项目产出，本月暂停继续学习。
- 每周资料学习总时长控制在 2-4 小时，项目产出优先。

## 每周节奏

工作日早上 7:50-9:20：

- 写代码
- 画架构
- 整理项目复盘
- 打磨面试表达

工作日晚上 9:20-10:00：

- 看 JD
- 改简历
- 写复盘
- 不安排重编码

周六上午：

- 集中打磨项目 2.5-3 小时

周日上午：

- 复盘、更新简历、安排下周

## Week 1：定位 + LLM Gateway V0

完成：

- 岗位 JD 分析 5-8 个
- 项目技术方案草图
- LLM Gateway V0
- 简历标题和个人优势 V1
- 大模型平台项目复盘框架

## Week 2：路由、重试、成本统计、Eval Harness V0

完成：

- 多模型路由规则
- 失败重试和 fallback
- Token/费用统计
- 应用维度用量统计
- 简单调用报表
- 批量 eval cases
- 通过率、平均成本、平均耗时、fallback 次数
- 失败归因：质量、模型、路由、Prompt、策略
- rohitg00 迁移点：把 `16-model-routing` / `19-ai-gateways` 的成本、质量、fallback、latency 指标转成 LLM Gateway 复盘表，不要求本月深学全部代码。

## Week 3：预算、限流、Prompt 版本

完成：

- 应用预算控制
- 简单限流策略
- Prompt 版本管理
- README
- 面试讲解稿 V1
- harness 面试表达 V1

## Week 4：项目包装 + 简历 V1

完成：

- 简历 V1
- 大模型平台项目复盘 V1
- LLM Gateway Demo V1
- Eval Harness V0
- AI Builder 复盘 V1
- 2 分钟自我介绍
- 5 分钟项目介绍
- RAG 质量治理项目设计草图
