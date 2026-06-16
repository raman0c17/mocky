# AGENTS.md

Guidance for AI coding agents (OpenAI Codex, Claude, Cursor, Gemini, etc.) working in the Mocky repository. Humans should read [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## What Mocky is

Mocky turns an idea into a PowerPoint deck. It (1) scaffolds Markdown from a **template library**, (2) generates **prompt bundles for many AI agents**, and (3) renders a `.pptx`. The default rendering engine is the pure-Python [`python-pptx`](https://python-pptx.readthedocs.io/) library, so the project is fully cross-platform and needs **no Microsoft Office install**.

## Project layout

```
src/mocky/
  __init__.py        # Public API exports
  cli.py             # `mocky` console entry point (idea / convert menu)
  markdown_parser.py # Markdown -> slide model (graceful missing-dep handling)
  file_manager.py    # Directory scan + image download (graceful missing-dep handling)
  ppt_generator.py   # python-pptx rendering engine (cross-platform)
  template_lib.py    # Idea -> Markdown templates (basic / problem-solution / product-launch)
  agent_prompter.py  # Builds prompts for 15 agents; reads keys from .env
tests/               # pytest suite (must pass on Windows/macOS/Linux)
input_files/         # sample Markdown
presentations/       # generated .pptx output
generated_markdowns/ # scaffolded Markdown output
prompt_outputs/      # generated agent prompt bundles
```

> Migrating from the flat `dev` layout? Each top-level module maps 1:1 into `src/mocky/`.

## Setup commands

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # optional, for agent keys
```

## Validation — run before proposing changes

```bash
ruff check .          # lint
ruff format --check . # formatting
pytest                # tests
```

All three must pass. CI runs the suite on `ubuntu-latest`, `windows-latest`, and `macos-latest` across Python 3.9–3.13 — keep changes portable.

## Conventions

- **Stay cross-platform.** Never put OS-specific dependencies (e.g. `pywin32`/COM) on the default code path. Optional backends must be feature-detected.
- **Conventional Commits** (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
- Public functions get docstrings and, where practical, type hints.
- Add or update tests for any behavior change.
- Tests must not hit the network — mock image downloads and any agent API calls.

## Safety notes

- **Secrets:** `.env` holds agent API keys. Never commit it, never print it, never send it anywhere. Only read keys locally.
- **Untrusted input:** Markdown can reference arbitrary image URLs. Validate URLs, set timeouts, and never write outside the configured output directory.

## Good first tasks for agents

- Add a new template to `template_lib.py`.
- Add `--idea/--template/--out` non-interactive CLI flags.
- Increase parser test coverage (nested lists, code blocks, tables).
- Implement direct AI generation using the keys in `.env`.
