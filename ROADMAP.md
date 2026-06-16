# Mocky Roadmap

This roadmap tracks where Mocky is headed and doubles as the **merge + migration plan** for the work currently on the `dev` branch and the three technical goals: **platform-agnostic rendering**, **container deployment**, and **library use**.

## 🌿 Branch status

The `dev` branch (by @imkartikey) is **4 commits ahead** of `master` and introduces a major new direction. This pack is designed to merge cleanly with it.

| `dev` addition | Status | Action in this pack |
| --- | --- | --- |
| MIT `LICENSE` | ✅ done | Matches our chosen license — keep it. |
| `template_lib.py` (idea → Markdown templates) | ✅ done | Absorbed into `src/mocky/template_lib.py`. |
| `agent_prompter.py` (15 agent prompt patterns + `.env`) | ✅ done | Absorbed into `src/mocky/agent_prompter.py`. |
| `.env.example` (agent credentials) | ✅ done | Keep; ensure `.env` stays git-ignored (see Security). |
| Refactored `main.py` (idea/convert menu) | ✅ done | Ported to `src/mocky/cli.py`. |
| Graceful missing-dependency handling | ✅ done | Preserved across all modules. |
| New tests (`test_agent_prompter.py`, `test_template_lib.py`) | ✅ done | Carried into `tests/`. |
| Windows-only `win32com` PPTX engine | ⚠️ blocker | **Replaced** with cross-platform `python-pptx` engine. |

## ✅ Done / in this release

### Platform-agnostic rendering engine (the key fix)

The `dev` branch made the `win32com` import optional, but the actual PPTX generation still **only runs on Windows with PowerPoint installed**. This pack replaces that backend with a pure-Python engine.

| | Legacy engine | New default engine |
| --- | --- | --- |
| Library | `pywin32` (`win32com`) | [`python-pptx`](https://python-pptx.readthedocs.io/) |
| Needs PowerPoint installed | Yes | **No** |
| Windows x64 / ARM64 | x64 only | ✅ both |
| macOS Intel / Apple Silicon | ❌ | ✅ both |
| Linux x64 / ARM64 | ❌ | ✅ both |
| Works in CI / containers | ❌ | ✅ |

The public API is unchanged: `PowerPointGenerator().create_presentation(slides, output_path)`. The `dev` `main.py`/`cli.py` flow works as-is on top of the new engine.

### Idea → deck workflow (from `dev`)

- Template library (`basic`, `problem-solution`, `product-launch`).
- Multi-agent prompt generation for 15 agents/CLIs, including Claude and Codex.
- Interactive menu: generate from an idea, or convert existing Markdown.

### Usable as a library

- Modules reorganized under `src/mocky/` with a stable public API in `mocky/__init__.py`.
- Packaged with `pyproject.toml`; `pip install mocky`, `from mocky import ...`, and a `mocky` console entry point.

### Deployable as a container

- Slim `Dockerfile` (`python:3.12-slim`) with no Office dependency.
- Multi-arch images (`linux/amd64`, `linux/arm64`) can be published via `docker buildx` in CI.

## 🚧 Next up

- [ ] **Direct AI generation** — actually call the agent APIs configured in `.env` (the prompt bundle is step one).
- [ ] **Themes & branded templates** — accept a `.pptx` template for styling.
- [ ] **Richer Markdown** — nested lists, code blocks, tables, blockquotes; speaker notes.
- [ ] **Non-interactive flags** — `mocky --idea "..." --template product-launch --out deck.pptx` for CI/scripting.
- [ ] **Publish to PyPI + GHCR** on tagged releases.

## 🔐 Security follow-ups

- Confirm `.gitignore` excludes `.env`, `generated_markdowns/`, `prompt_outputs/`, and `*.pptx`.
- Validate/timeout remote image downloads (untrusted Markdown can reference arbitrary URLs).

Want to help? Check the [issues](https://github.com/raman0c17/mocky/issues) and read [`CONTRIBUTING.md`](./CONTRIBUTING.md).
