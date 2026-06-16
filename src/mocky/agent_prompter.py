"""Build Markdown-deck prompts for a range of AI agents / CLIs.

Adapted from the ``dev`` branch work by @imkartikey. The builder never sends
requests itself — it produces prompt text you can paste into the agent of your
choice. Credentials (when present) are read locally from ``.env`` only to label
which agents are configured.
"""

from __future__ import annotations

import os

AGENT_ENV_KEYS = {
    "open design": "OPEN_DESIGN_API_KEY",
    "windsurf cli": "WINDSURF_CLI_TOKEN",
    "trae cli": "TRAE_CLI_KEY",
    "claude code": "CLAUDE_CODE_API_KEY",
    "claude api": "CLAUDE_API_KEY",
    "cursor agent": "CURSOR_AGENT_KEY",
    "codex cli": "CODEX_CLI_TOKEN",
    "hermes": "HERMES_API_KEY",
    "gemini cli": "GEMINI_CLI_TOKEN",
    "gemini api": "GEMINI_API_KEY",
    "grok": "GROK_API_KEY",
    "qwen": "QWEN_API_KEY",
    "github copilot cli": "GITHUB_COPILOT_CLI_TOKEN",
    "aider": "AIDER_API_KEY",
    "anthropic api": "ANTHROPIC_API_KEY",
}

AGENT_PROMPT_PATTERNS = {
    "open design": (
        "Open Design prompt:\n"
        "Create a markdown presentation for the idea:\n\n{idea}\n\n"
        "Use the selected template: {template}. Include clear slide titles, "
        "bullets, and any supporting visual guidance."
    ),
    "windsurf cli": (
        "Windsurf CLI prompt:\n"
        "Generate a markdown deck for the idea, following the {template} "
        "pattern. Output should be structured slide-by-slide with headings "
        "and bullets."
    ),
    "trae cli": (
        "Trae CLI prompt:\n"
        "Build a presentation draft in markdown using the idea and the "
        "{template} template. Keep slides concise and audience-focused."
    ),
    "claude code": (
        "Claude Code prompt:\n"
        "Produce a markdown presentation from this idea:\n{idea}\n"
        "Use the {template} template. Format as markdown slides with "
        "headings and bullet lists."
    ),
    "claude api": (
        "Claude API prompt:\n"
        "Generate a markdown presentation for the idea '{idea}'. Use the "
        "{template} layout. Provide slide titles, key talking points, and a "
        "summary."
    ),
    "cursor agent": (
        "Cursor Agent prompt:\n"
        "Write a markdown presentation based on the idea: {idea}. Follow the "
        "{template} template and prioritize slide clarity and structure."
    ),
    "codex cli": (
        "Codex CLI prompt:\n"
        "Render a markdown slide deck for the idea '{idea}'. Match the "
        "{template} structure and emphasize high-level points."
    ),
    "hermes": (
        "Hermes prompt:\n"
        "Create a markdown presentation draft for the idea '{idea}'. Use the "
        "{template} outline and ensure each slide is easy to convert to PPT."
    ),
    "gemini cli": (
        "Gemini CLI prompt:\n"
        "Draft a markdown presentation in the {template} style for idea: "
        "{idea}. Include slide titles, bullets, and a final summary slide."
    ),
    "gemini api": (
        "Gemini API prompt:\n"
        "Build a markdown presentation from the idea '{idea}'. Apply the "
        "{template} framework and use clear slide sections."
    ),
    "grok": (
        "Grok prompt:\n"
        "Compose a markdown presentation for the idea '{idea}' using the "
        "{template} structure. Deliver a concise slide outline with key "
        "points."
    ),
    "qwen": (
        "Qwen prompt:\n"
        "Create a markdown-based presentation for the idea '{idea}' using "
        "the {template} template. Keep content structured and slide-ready."
    ),
    "github copilot cli": (
        "GitHub Copilot CLI prompt:\n"
        "Generate a markdown slide deck from the idea '{idea}'. Follow the "
        "{template} template and make it ready for PPT conversion."
    ),
    "aider": (
        "Aider prompt:\n"
        "Write a markdown presentation using the idea '{idea}' and the "
        "{template} template. Organize content into headings and bullet "
        "points."
    ),
    "anthropic api": (
        "Anthropic API prompt:\n"
        "Produce a markdown presentation draft for the idea '{idea}'. Use "
        "the {template} template and create clear slide sections."
    ),
}


class AgentPromptBuilder:
    @staticmethod
    def list_agents():
        return list(AGENT_PROMPT_PATTERNS.keys())

    @staticmethod
    def build_prompt(agent_name, idea, template_name):
        pattern = AGENT_PROMPT_PATTERNS.get(agent_name)
        if not pattern:
            raise ValueError(f"Unknown agent: {agent_name}")
        return pattern.format(idea=idea, template=template_name)

    @staticmethod
    def build_all_prompts(idea, template_name):
        return {
            agent: AgentPromptBuilder.build_prompt(agent, idea, template_name)
            for agent in AGENT_PROMPT_PATTERNS
        }

    @staticmethod
    def load_agent_config(env_path=".env"):
        config = {}
        if os.path.exists(env_path):
            with open(env_path, encoding="utf-8") as env_file:
                for line in env_file:
                    trimmed = line.strip()
                    if not trimmed or trimmed.startswith("#"):
                        continue
                    if "=" in trimmed:
                        key, value = trimmed.split("=", 1)
                        config[key.strip()] = value.strip()
        return config

    @staticmethod
    def get_expected_env_keys():
        return AGENT_ENV_KEYS.copy()
