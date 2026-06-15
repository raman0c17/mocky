import unittest
from agent_prompter import AgentPromptBuilder, AGENT_PROMPT_PATTERNS, AGENT_ENV_KEYS


class TestAgentPromptBuilder(unittest.TestCase):
    def test_list_agents_contains_known_agents(self):
        agents = AgentPromptBuilder.list_agents()
        self.assertIn("open design", agents)
        self.assertIn("anthropic api", agents)

    def test_build_prompt_returns_expected_prompt(self):
        idea = "Launch a new chatbot"
        template = "basic"
        prompt = AgentPromptBuilder.build_prompt("claude api", idea, template)
        self.assertIn(idea, prompt)
        self.assertIn(template, prompt)

    def test_build_all_prompts_include_agents(self):
        idea = "Build a training plan"
        template = "product-launch"
        prompts = AgentPromptBuilder.build_all_prompts(idea, template)
        self.assertEqual(set(prompts.keys()), set(AGENT_PROMPT_PATTERNS.keys()))

    def test_load_agent_config_reads_env_file(self):
        env_content = "OPEN_DESIGN_API_KEY=testkey\n# comment\nTRA E CLI KEY=bad\n"
        with unittest.mock.patch("builtins.open", unittest.mock.mock_open(read_data=env_content)):
            with unittest.mock.patch("os.path.exists", return_value=True):
                config = AgentPromptBuilder.load_agent_config(".env")
                self.assertIn("OPEN_DESIGN_API_KEY", config)
                self.assertEqual(config["OPEN_DESIGN_API_KEY"], "testkey")

    def test_get_expected_env_keys_contains_all_agents(self):
        keys = AgentPromptBuilder.get_expected_env_keys()
        self.assertEqual(keys["github copilot cli"], "GITHUB_COPILOT_CLI_TOKEN")
        self.assertEqual(len(keys), len(AGENT_ENV_KEYS))


if __name__ == "__main__":
    unittest.main()
