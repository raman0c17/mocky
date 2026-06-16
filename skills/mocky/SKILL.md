---
name: mocky
description: >-
  Turn an idea or a Markdown outline into a polished, cross-platform PowerPoint
  (.pptx) deck. Use this skill when the user wants to create slides, a deck, or
  a presentation from a topic, idea, or Markdown file. Mocky scaffolds Markdown
  from a template library, can generate prompts for other AI agents, and renders
  the final .pptx with a pure-Python engine (no Microsoft Office required).
license: MIT
---

# Mocky — Idea / Markdown → PowerPoint

## What this skill does

Mocky converts an **idea** or a **Markdown outline** into a `.pptx` deck. It runs
the same on Windows, macOS, and Linux because it renders with
[`python-pptx`](https://python-pptx.readthedocs.io/) — no PowerPoint install
needed.

Use this skill when the user asks to:
- "Make a presentation / slides / deck about X."
- "Turn this Markdown into PowerPoint."
- "Draft a pitch deck for this idea."

## Prerequisites

```bash
pip install mocky        # or: pip install python-pptx markdown beautifulsoup4 requests
```

## Slide model

Mocky represents a deck as a list of slide dicts:

```python
slides = [
    {"title": "Slide title", "content": ["A bullet", "Another bullet"]},
    {"title": "With a picture", "content": [{"image": "/path/to/local.png"}]},
    {"title": "With a link", "content": [{"link": "https://example.com"}]},
]
```

Markdown maps to this model as: first `#` = deck title, each `##` = a new slide,
and paragraphs / lists / images / links become content items.

## Workflow A — from an idea

1. Pick a template: `basic`, `problem-solution`, or `product-launch`.
2. Scaffold Markdown, then render it.

```python
from mocky import TemplateLibrary, MarkdownParser, PowerPointGenerator

idea = "Launching Mocky 1.0 to the open-source community"
markdown = TemplateLibrary.build_markdown(idea, "product-launch")
path = TemplateLibrary.save_markdown(markdown, "generated_markdowns", "launch.md")

parsed = MarkdownParser().parse_markdown(path)
PowerPointGenerator().create_presentation(parsed["slides"], "presentations/launch.pptx")
```

## Workflow B — from existing Markdown

```python
from mocky import MarkdownParser, PowerPointGenerator

parsed = MarkdownParser().parse_markdown("input_files/my_outline.md")
PowerPointGenerator().create_presentation(parsed["slides"], "presentations/out.pptx")
```

## Optional — generate prompts for other agents

If the user wants to refine the deck with a specific AI agent, Mocky can emit a
prompt for it (Claude, Codex, Cursor, Gemini, and more):

```python
from mocky import AgentPromptBuilder

prompt = AgentPromptBuilder.build_prompt("claude code", idea, "product-launch")
print(prompt)
```

## Guidance for the agent

- Prefer **Workflow A** when the user gives a topic/idea; **Workflow B** when they
  provide Markdown or a file.
- Keep slides concise: a title plus a few bullets each.
- Only reference images that exist locally or via `http(s)` URLs; Mocky downloads
  remote images with a timeout and ignores other schemes.
- Always write output under `presentations/` (or a user-specified path) and report
  the final `.pptx` path back to the user.
- Never read, print, or transmit the contents of a user's `.env` file.
