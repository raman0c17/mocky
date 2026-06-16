# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Idea → deck workflow**: a template library (`basic`, `problem-solution`, `product-launch`) that scaffolds Markdown from a one-line idea. (from `dev`, @imkartikey)
- **Agent prompt builder**: generates ready-to-paste prompts for 15 AI agents/CLIs (Claude, Codex, Cursor, Gemini, Grok, and more) and reads credentials from `.env`. (from `dev`, @imkartikey)
- `.env.example` documenting supported agent credentials. (from `dev`)
- Interactive CLI menu: generate from an idea, or convert existing Markdown. (from `dev`)
- Graceful handling of missing optional dependencies across modules. (from `dev`)
- Cross-platform PowerPoint rendering using `python-pptx` (no PowerPoint install required).
- Packaging via `pyproject.toml`; Mocky is now installable (`pip install mocky`) and importable as a library, with a `mocky` console entry point.
- `Dockerfile` and `.dockerignore` for containerized use.
- Community health files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue/PR templates, Dependabot.
- `AGENTS.md` for AI coding agents and a Claude Skill under `skills/mocky/`.
- Cross-platform CI matrix (Windows, macOS, Linux × Python 3.9–3.13).
- Tests for the template library and agent prompter. (from `dev`)

### Changed
- Replaced the Windows-only COM automation backend (`win32com`/`pywin32`) with the portable `python-pptx` engine.
- Reorganized source from a flat layout into a `src/mocky/` package.

### Removed
- `pywin32` from default dependencies.

## [0.1.0] - 2026-06-11

### Added
- Initial release: Markdown-to-PowerPoint conversion via a CLI loop.
