# LLM Gateway Eval Gate Before/After 报告

日期：2026-05-28

## 报告目的

这份报告用于证明 LLM Gateway 的 Eval Harness 不只是输出指标，而是能够根据门禁策略给出发布判断：

- `allow`：核心 case 通过，可以继续发布。
- `review`：质量通过，但成本、延迟或 fallback 超阈值，需要产品和工程复核。
- `block`：质量或关键失败类型不达标，不允许发布。

门禁策略来源：

- `projects/llm-gateway/config/eval_policy.json`

本地门禁命令：

- `python3 scripts/run_eval_gate.py --request examples/evaluation_request.json`
- `python3 scripts/run_eval_gate.py --request examples/evaluation_regression_request.json --no-fail`

CI 行为：

- `allow` 返回退出码 0。
- `block` 返回退出码 1。
- `review` 返回退出码 2。

## 评测策略

当前 V0 策略：

| 检查项 | 阈值 | 决策含义 |
| --- | --- | --- |
| `pass_rate` | `>= 0.95` | 核心 case 不能明显退化 |
| `avg_cost_usd` | `<= 0.001` | 平均成本不能超过门禁阈值 |
| `avg_latency_ms` | `<= 1200` | 平均延迟不能超过体验阈值 |
| `fallback_count` | `<= 1` | fallback 次数不能异常升高 |
| `blocked_failure_tags` | 不出现 `prompt_failure`、`routing_failure`、`policy_failure`、`harness_runtime_failure` | 关键环境失败必须阻断发布 |

## Before：基线评测

输入：

- `projects/llm-gateway/examples/evaluation_request.json`

运行结果摘要：

```json
{
  "summary": {
    "total": 3,
    "passed": 3,
    "failed": 0,
    "pass_rate": 1.0,
    "fail_rate": 0.0,
    "avg_cost_usd": 0.000102,
    "avg_latency_ms": 500.0,
    "fallback_count": 1,
    "failure_breakdown": {}
  },
  "gate": {
    "policy_id": "llm-gateway-release-gate-v0",
    "decision": "allow"
  }
}
```

产品判断：

- 通过率达到 1.0，高于 0.95 门禁。
- 平均成本、平均耗时和 fallback 次数均在阈值内。
- 未出现 Prompt、路由、策略或运行时环境失败。
- 结论：允许进入下一步发布或演示。

## After：回归样例

输入：

- `projects/llm-gateway/examples/evaluation_regression_request.json`

回归变化：

- 新增 `case-regression-001`，模拟 Prompt / rubric / 业务期望变化后，输出未满足新增质量要求。

运行结果摘要：

```json
{
  "summary": {
    "total": 3,
    "passed": 2,
    "failed": 1,
    "pass_rate": 0.6667,
    "fail_rate": 0.3333,
    "avg_cost_usd": 0.000144,
    "avg_latency_ms": 750.0,
    "fallback_count": 1,
    "failure_breakdown": {
      "quality_failure": 1
    }
  },
  "gate": {
    "policy_id": "llm-gateway-release-gate-v0",
    "decision": "block"
  },
  "failed_results": [
    {
      "case_id": "case-regression-001",
      "failure_tag": "quality_failure",
      "missing_keywords": [
        "不存在的门禁关键词"
      ]
    }
  ]
}
```

产品判断：

- 通过率下降到 0.6667，低于 0.95 门禁。
- failure breakdown 显示 `quality_failure`，说明不是供应商不可用，而是输出质量未满足新增要求。
- 成本、延迟和 fallback 仍在阈值内，因此问题不在成本或稳定性，而在质量规则和输出内容。
- 结论：阻断发布，先修复 case 质量或重新确认 rubric 是否合理。

## 面试表达

这份报告可以这样讲：

> 我不会把 Eval Harness 只当成测试脚本，而是把它当成 AI 平台的发布门禁。比如 LLM Gateway 里，同一批 case 可以输出 pass rate、成本、延迟、fallback 和失败归因；再根据 eval policy 给出 allow、review 或 block。正常版本会 allow；一旦新增质量要求导致 pass rate 降到阈值以下，gate 会 block，并指出具体失败 case 和 failure tag。这样 Prompt、模型或路由策略变更就不是凭感觉上线，而是有可解释的质量门禁。

## 后续增强

- 增加历史报告目录，保存每次评测输出。
- 增加 before/after 对比脚本，自动生成 Markdown 报告。
- 增加 GitHub Actions 或其他 CI 执行记录，模拟 Prompt 或路由策略变更前的发布检查。
- 把生产 trace 和 bad case 回流到 `evaluation_request.json`。
