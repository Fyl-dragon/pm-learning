# AI 产品 / Agent 平台 / AI Builder 岗位市场快照

## 调研范围

- 日期：2026-05-28
- 目标岗位：AI 平台产品经理、AI Agent 产品经理、AI 产品运营/建设、AI 应用工程师作为技术能力对标
- 地区：重庆优先，成都/远程作为相邻或可参考样本
- 样本数量：6 个岗位样本 + 1 个重庆薪资统计样本
- 结论置信度：样本有限，适合作为 Week 1 学习路线校准，不适合直接推导完整市场趋势

## 来源列表

| 来源 | 链接 | 岗位/地区 | 日期 | 可信度 |
| --- | --- | --- | --- | --- |
| BeBee / 猎聘来源 | https://bebee.com/cn/jobs/ai-agent--techmap_cn_82635507 | AI 平台产品经理（Agent 平台方向）/ 重庆 | 检索于 2026-05-28；页面显示 2 天前、截至 2026-07-20 | 中 |
| BOSS 直聘搜索结果 | https://www.zhipin.com/zhaopin/904d936bb2f094f90XB62d26/ | AI 产品经理 / 重庆两江新区 | 检索于 2026-05-28；页面抓取约 3 周前 | 低 |
| 智联招聘 | https://www.zhaopin.com/jobdetail/CCL1523250530J40957243902.htm | AI 应用工程师 / 重庆沙坪坝 | 检索于 2026-05-28；页面抓取约 1 周前 | 中 |
| 智联招聘 | https://www.zhaopin.com/jobdetail/CCL1498742180J40770777506.htm | AI 智能体产品经理 / 成都青羊 | 检索于 2026-05-28；页面更新于 2026-05-01 | 高 |
| 领英 / 猎聘来源 | https://cn.linkedin.com/jobs/view/%E6%99%BA%E8%83%BD%E4%BD%93%E5%BB%BA%E8%AE%BE%E7%BB%8F%E7%90%86-at-%E5%AE%A2%E5%A6%82%E4%BA%91-4373727107 | 智能体建设经理 / 成都 | 检索于 2026-05-28；页面抓取约 3 周前，职位已停止接受申请 | 中 |
| 远程工作者 | https://remote-china.com/labels/41/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BDAI | AI 相关产品经理 / 远程 | 检索于 2026-05-28；页面抓取约 1 周前 | 中 |
| 职友集 | https://www.jobui.com/salary/chongqing-rengongzhinengchanpinjingli/ | 重庆人工智能产品经理薪资统计 | 检索于 2026-05-28；统计截至 2025-11-17，样本 3 份 | 低 |

## 样本摘要

| 城市 | 岗位 | 薪资 | 方向 | 对路线的含义 |
| --- | --- | --- | --- | --- |
| 重庆 | AI 平台产品经理（Agent 平台方向） | 8-12K | Agent 平台、MCP、Workflow、RAG、多租户、灰度、API/SDK、数据治理 | 与当前定位高度贴合，但薪资只到下一阶段底线附近，需要用作品集争取上限 |
| 重庆 | AI 产品经理 | 10-15K | AI 经验、智能体产品化设计 | 证明重庆本地已有 AI 产品经理样本，但来源信息较少，需要后续补更完整 JD |
| 重庆 | AI 应用工程师 | 15-20K | 大模型行业应用、多 Agent、RAG、Prompt、框架选型 | 不是主投产品岗，但证明 AI Builder 技术能力在重庆有更高薪资锚点 |
| 成都 | AI 智能体产品经理 | 10-20K·13 薪 | Agent 从 0 到 1、PRD、状态机、工具调用、RAG、评测指标、失败案例分析 | 说明 Agent 产品岗正在要求产品同时懂工作流、工具和评测 |
| 成都 | 智能体建设经理 | 18-25K | Agent 运营、标注体系、知识库、解决率、数据评估 | 更偏运营/建设，但对评测集、标注和知识库质量治理有参考价值 |
| 远程 | AI 相关产品经理 | 20-30K | B 端、OpenClaw / Agent、自动化工作流 | 远程机会可能薪资更高，但竞争和交付要求更强，适合作为外部上限参考 |

## 高频要求

| 要求 | 频次/证据 | 对应能力 | 用户现有证据 | 缺口 |
| --- | --- | --- | --- | --- |
| Agent 平台 / 智能体产品化 | 5/6 样本出现 Agent、智能体、工具调用、工作流或 Agent 平台 | Agent Harness、tool registry、状态、权限、trace、human review | 已有 Agent Harness 方向文档和面试讲法 | 还缺可运行 Agent Harness 样例和工具 schema 表 |
| RAG / 知识库 / 上下文治理 | 4/6 样本出现 RAG、知识库或上下文 | RAG Evaluation Harness、知识库质量治理 | 6 个月路线已有第 2 月 RAG Evaluation Harness | 还缺标准问答集、引用可信度和文档版本回归样例 |
| 评测指标 / 数据闭环 / 失败分析 | 4/6 样本出现评价体系、解决率、失败案例、监控、指标或模型评估 | Eval Harness、失败归因、CI gate、生产 trace 回流 | LLM Gateway 已有 Eval Harness V0 和失败归因 | 还缺 baseline、rubric、regression、CI gate 的显式表达 |
| 平台型产品抽象 | 3/6 样本出现平台底座、通用能力、API/SDK、多租户、权限、治理 | LLM Gateway、平台产品、B 端抽象 | 当前项目已覆盖路由、fallback、预算、日志、Prompt 版本 | 需要补 API/SDK 接入文档、权限/审计和开发者体验表达 |
| AI Builder 技术理解 | 4/6 样本要求理解 Python、LLM 框架、API、Agent、Prompt 或工程落地 | AI 辅助开发、FastAPI、RAG/Agent 工程理解 | 已有开发背景和 LLM Gateway 代码/test | 需要补一次 AI 辅助开发复盘和 rohitg00 lesson 迁移记录 |
| 行业落地和跨团队推进 | 4/6 样本强调业务场景、跨算法/后端/业务/实施协作 | 产品经理经验、现场交付、外包和驻场经验 | 个人背景吻合，已有 FDE 风险判断 | 简历需要把现场经验包装成 bad case 回流和平台能力沉淀 |

## 结论

- 已具备：
  - 软件工程背景、开发经验、产品经理经验、当前大模型中转平台经验。
  - LLM Gateway 项目已能承接“平台型产品 + 调用治理 + Eval Harness”的表达。
  - 外包、驻场和客户现场经验能包装为需求抽象、交付风险识别和 bad case 回流能力。

- 需要补：
  - Agent Harness 可运行样例。
  - RAG Evaluation Harness 标准问答集和指标。
  - Eval Harness 的 baseline、rubric、regression、CI gate 明确表达。
  - 真实 JD 样本持续更新，至少每周 5 个。

- 需要包装：
  - 把“做过开发”改成“能用 AI Builder 把需求推进到可运行原型，并用测试/eval/trace 证明质量”。
  - 把“做过驻场/外包”改成“理解企业现场 AI 落地失败原因，能把 bad case、trace、客户反馈沉淀成评测集和平台治理能力”。
  - 把“AI 中转平台”改成“LLM Gateway / LLMOps 调用治理 + Eval Harness 质量治理”。

## 对学习路线的影响

1. 主线不改：继续保持 AI 平台产品经理 / AI Evals & Harness 产品方向，具备 AI Builder 能力。
2. 下周不新增资料，优先强化 LLM Gateway 的 Eval Harness 表达，补 baseline、rubric、regression、CI gate。
3. Agent Harness 的优先级上升：重庆和成都样本都明显要求 Agent 平台、工具调用、工作流和 RAG。
4. AI Builder 技术线必须保留：重庆 AI 应用工程岗位的薪资锚点高于本地部分产品岗，说明技术理解能显著抬高议价，但仍不把主定位改成纯工程师。
5. 重庆本地 AI 产品机会存在，但样本少、薪资跨度大；阶段目标 12K 仍合理，13K-15K 需要更强作品集或考虑成都/远程机会。
