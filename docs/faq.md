# FAQ

## Do I need Microsoft PowerPoint or Office installed?

No. Mocky renders with `python-pptx`, which is pure Python. Nothing from
Microsoft Office is required on any platform.

## Which operating systems are supported?

Windows (x64 and ARM), macOS (Intel and Apple Silicon), and Linux. The same code
path runs everywhere.

## I got `error: externally-managed-environment` when installing.

That's a macOS/Homebrew (PEP 668) guard. Install inside a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Avoid `--break-system-packages`, which can damage your Homebrew Python.

## Does Mocky call AI services for me?

No. The agent prompt builder only *generates prompt text* for you to paste into
the agent of your choice. Your credentials never leave your machine.

## Where do generated files go?

- Scaffolded Markdown → `generated_markdowns/`
- Agent prompt bundles → `prompt_outputs/`
- Rendered decks → `presentations/`

All of these are git-ignored by default.

## How do I report a bug or request a feature?

Open an issue using the templates on the
[GitHub repository](https://github.com/raman0c17/mocky/issues).
