# Mocky

**Turn an idea or a Markdown outline into a polished PowerPoint deck — no Microsoft Office required.**

Mocky runs the same on Windows, macOS, and Linux because it renders with
[`python-pptx`](https://python-pptx.readthedocs.io/) instead of automating
Microsoft Office.

## What you get

- :material-lightbulb-on: **Idea → deck.** Scaffold a structured Markdown outline from a one-line idea using a template library.
- :material-robot: **AI-agent prompts.** Generate ready-to-paste prompts for 15 agents/CLIs (Claude, Codex, Gemini, Cursor, and more).
- :material-microsoft-powerpoint: **Real `.pptx`.** A cross-platform engine renders genuine PowerPoint files.
- :material-package-variant: **CLI *and* library.** Use the `mocky` command or `import mocky` in your own code.
- :material-docker: **Container-ready.** Ship it as a Docker image.

## Quick taste

```python
from mocky import TemplateLibrary, MarkdownParser, PowerPointGenerator

markdown = TemplateLibrary.build_markdown("Launching Mocky 1.0", "product-launch")
path = TemplateLibrary.save_markdown(markdown, "generated_markdowns", "launch.md")

parsed = MarkdownParser().parse_markdown(path)
PowerPointGenerator().create_presentation(parsed["slides"], "presentations/launch.pptx")
```

Ready to try it? Head to [Getting started](getting-started.md).

!!! note "Open source"
    Mocky is released under the [MIT License](https://github.com/raman0c17/mocky/blob/master/LICENSE). Contributions are welcome — see [Contributing](contributing.md).
