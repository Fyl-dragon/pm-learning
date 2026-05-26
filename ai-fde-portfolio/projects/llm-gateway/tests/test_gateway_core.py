import unittest

from app.database import GatewayDatabase
from app.gateway import GatewayRequest, GatewayService


class GatewayCoreTest(unittest.TestCase):
    def setUp(self):
        self.db = GatewayDatabase(":memory:")
        self.service = GatewayService(self.db)

    def tearDown(self):
        self.db.close()

    def test_low_cost_route_chooses_cheapest_model(self):
        response = self.service.chat(
            GatewayRequest(
                app_id="app-sales-copilot",
                prompt="测试低价路由",
                route_strategy="low_cost",
            )
        )
        self.assertEqual(response["model_id"], "deepseek-chat")
        self.assertGreater(response["usage"]["cost_usd"], 0)

    def test_fallback_after_provider_failure(self):
        response = self.service.chat(
            GatewayRequest(
                app_id="app-sales-copilot",
                prompt="FORCE_FAIL:deepseek-chat 测试失败后切换模型",
                route_strategy="default",
                max_retries=2,
            )
        )
        self.assertEqual(response["model_id"], "qwen-plus")
        self.assertEqual(response["attempts"][0]["status"], "failed")
        self.assertEqual(response["attempts"][1]["fallback_from"], "deepseek-chat")

    def test_prompt_version_renders_business_context(self):
        response = self.service.chat(
            GatewayRequest(
                app_id="app-sales-copilot",
                prompt="客户想做售后诊断助手。",
                route_strategy="default",
                prompt_version_id="prompt-solution-v1",
                variables={"industry": "汽车", "scenario": "售后诊断"},
            )
        )
        self.assertEqual(response["prompt_version_id"], "prompt-solution-v1")

    def test_usage_summary_counts_calls_and_cost(self):
        self.service.chat(GatewayRequest(app_id="app-sales-copilot", prompt="第一次调用"))
        self.service.chat(GatewayRequest(app_id="app-sales-copilot", prompt="第二次调用"))
        usage = self.service.usage("app-sales-copilot")
        self.assertEqual(usage["calls"], 2)
        self.assertGreater(usage["cost_usd"], 0)

    def test_evaluation_entrypoint_returns_pass_rate(self):
        result = self.service.evaluate(
            "app-sales-copilot",
            [
                {
                    "id": "case-1",
                    "prompt": "客户需要 AI 方案。",
                    "expected_keywords": ["业务目标", "技术链路"],
                }
            ],
        )
        self.assertEqual(result["harness"]["name"], "llm-gateway-eval-harness")
        self.assertEqual(result["summary"]["total"], 1)
        self.assertEqual(result["summary"]["passed"], 1)
        self.assertEqual(result["summary"]["pass_rate"], 1.0)
        self.assertIn("trace", result["results"][0])

    def test_eval_harness_counts_fallback_and_cost(self):
        result = self.service.evaluate(
            "app-sales-copilot",
            [
                {
                    "id": "case-fallback",
                    "prompt": "FORCE_FAIL:deepseek-chat 客户要求失败后自动切换备用模型。",
                    "route_strategy": "default",
                    "max_retries": 2,
                    "expected_keywords": ["成本"],
                    "expected_model_id": "qwen-plus",
                }
            ],
        )
        self.assertEqual(result["summary"]["passed"], 1)
        self.assertEqual(result["summary"]["fallback_count"], 1)
        self.assertGreater(result["summary"]["avg_cost_usd"], 0)
        self.assertEqual(result["results"][0]["trace"]["attempts"][0]["status"], "failed")

    def test_eval_harness_attributes_quality_failure(self):
        result = self.service.evaluate(
            "app-sales-copilot",
            [
                {
                    "id": "case-quality-failure",
                    "prompt": "客户需要 AI 方案。",
                    "expected_keywords": ["不存在的验收关键词"],
                }
            ],
        )
        self.assertEqual(result["summary"]["failed"], 1)
        self.assertEqual(result["summary"]["failure_breakdown"]["quality_failure"], 1)
        self.assertEqual(result["results"][0]["failure_tag"], "quality_failure")

    def test_eval_harness_attributes_prompt_failure(self):
        result = self.service.evaluate(
            "app-sales-copilot",
            [
                {
                    "id": "case-prompt-failure",
                    "prompt": "缺少 prompt 模板变量。",
                    "prompt_version_id": "prompt-solution-v1",
                    "variables": {"industry": "汽车"},
                    "expected_failure_tag": "prompt_failure",
                }
            ],
        )
        self.assertEqual(result["summary"]["passed"], 1)
        self.assertEqual(result["results"][0]["passed"], True)
        self.assertEqual(result["results"][0]["failure_tag"], "none")


if __name__ == "__main__":
    unittest.main()
