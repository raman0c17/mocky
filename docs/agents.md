# AI agent prompts

Mocky can generate **ready-to-paste prompts** for a range of AI agents and CLIs.
It never calls those services itself — it produces prompt text you paste into the
agent of your choice, so you stay in control of your own credentials.

## Supported agents

Claude Code, Claude API, Anthropic API, Codex CLI, Cursor Agent, GitHub Copilot
CLI, Gemini CLI, Gemini API, Grok, Qwen, Aider, Windsurf CLI, Trae CLI, Open
Design, and Hermes — **15 in total**.

## API

```python
from mocky import AgentPromptBuilder

AgentPromptBuilder.list_agents()
# ['open design', 'windsurf cli', ..., 'anthropic api']

prompt = AgentPromptBuilder.build_prompt("claude code", "My idea", "product-launch")
print(prompt)

# Build prompts for every agent at once
all_prompts = AgentPromptBuilder.build_all_prompts("My idea", "basic")
```

## Credentials (optional)

If you keep agent keys in a local `.env`, Mocky can read them to label which
agents are configured:

```python
config = AgentPromptBuilder.load_agent_config(".env")
expected = AgentPromptBuilder.get_expected_env_keys()  # agent -> env var name
```

!!! danger "Never commit secrets"
    Copy `.env.example` to `.env` and fill in only the keys you use. `.env` is
    git-ignored by default. Mocky reads these keys locally and never transmits
    them.
