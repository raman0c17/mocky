"""Tests for the multi-agent prompt builder."""

import pytest

from mocky.agent_prompter import AGENT_ENV_KEYS, AgentPromptBuilder


def test_list_agents_includes_claude_and_codex():
    agents = AgentPromptBuilder.list_agents()
    assert "claude code" in agents
    assert "codex cli" in agents
    assert "anthropic api" in agents


def test_build_prompt_includes_idea_and_template():
    prompt = AgentPromptBuilder.build_prompt("claude code", "Sell more widgets", "basic")
    assert "Sell more widgets" in prompt
    assert "basic" in prompt


def test_build_prompt_unknown_agent_raises():
    with pytest.raises(ValueError):
        AgentPromptBuilder.build_prompt("nonexistent", "idea", "basic")


def test_build_all_prompts_covers_every_agent():
    prompts = AgentPromptBuilder.build_all_prompts("An idea", "product-launch")
    assert set(prompts.keys()) == set(AgentPromptBuilder.list_agents())
    assert all("An idea" in text for text in prompts.values())


def test_expected_env_keys_match_agents():
    keys = AgentPromptBuilder.get_expected_env_keys()
    assert keys == AGENT_ENV_KEYS
    assert keys["claude code"] == "CLAUDE_CODE_API_KEY"


def test_load_agent_config_parses_env(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("# comment\nCLAUDE_API_KEY=abc123\n\nGROK_API_KEY = xyz\n")
    config = AgentPromptBuilder.load_agent_config(str(env_file))
    assert config["CLAUDE_API_KEY"] == "abc123"
    assert config["GROK_API_KEY"] == "xyz"


def test_load_agent_config_missing_file_returns_empty(tmp_path):
    assert AgentPromptBuilder.load_agent_config(str(tmp_path / "nope.env")) == {}
