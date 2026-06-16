# Contributing to Mocky

First off — thank you for taking the time to contribute! 🎉 Mocky is a community project, and every contribution, big or small, makes it better.

This document explains how to get set up, the workflow we follow, and what we expect from contributions.

## Table of contents

- [Code of Conduct](#code-of-conduct)
- [Ways to contribute](#ways-to-contribute)
- [Development setup](#development-setup)
- [Project structure](#project-structure)
- [Running tests](#running-tests)
- [Coding style](#coding-style)
- [Commit messages](#commit-messages)
- [Submitting a pull request](#submitting-a-pull-request)
- [Reporting bugs & requesting features](#reporting-bugs--requesting-features)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold it. Please report unacceptable behavior as described there.

## Ways to contribute

- 🐛 **Report bugs** using the bug report template.
- 💡 **Suggest features** using the feature request template.
- 📖 **Improve documentation** — even fixing a typo helps.
- 🧪 **Add tests** to increase coverage.
- 💻 **Submit code** for open issues, especially those labeled `good first issue` or `help wanted`.

## Development setup

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/mocky.git
   cd mocky
   ```

2. **Create a virtual environment** and install in editable mode with dev extras:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Verify your setup**:

   ```bash
   pytest
   ```

No Microsoft PowerPoint installation is required — Mocky renders `.pptx` with the pure-Python `python-pptx` engine.

## Project structure

```
mocky/
├── src/mocky/            # Library + CLI source
│   ├── __init__.py       # Public API exports
│   ├── cli.py            # `mocky` command entry point
│   ├── markdown_parser.py
│   ├── file_manager.py
│   └── ppt_generator.py  # python-pptx engine (cross-platform)
├── tests/                # pytest test suite
├── input_files/          # Sample Markdown inputs
└── presentations/        # Generated .pptx output
```

## Running tests

We use [`pytest`](https://docs.pytest.org/):

```bash
pytest                 # run everything
pytest -k parser       # run a subset
pytest --cov=mocky     # with coverage
```

Tests must pass on Windows, macOS, and Linux. Our CI runs the suite across all three on every pull request.

## Coding style

- Format with [`ruff`](https://docs.astral.sh/ruff/) (or `black`): `ruff format .`
- Lint with `ruff check .`
- Write clear docstrings for public functions and classes.
- Keep functions small and focused; prefer pure functions where possible.

## Commit messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add speaker-notes support
fix: handle empty slide content gracefully
docs: clarify Docker usage
test: cover image download failures
chore: bump python-pptx
```

This keeps history readable and powers automated changelogs.

## Submitting a pull request

1. Create a branch: `git checkout -b feat/my-feature`.
2. Make your changes, **add tests**, and ensure `pytest` and `ruff check .` pass.
3. Update documentation (`README.md`, `CHANGELOG.md`) where relevant.
4. Push and open a PR against the `master` branch.
5. Fill out the PR template and link any related issues (e.g. `Closes #123`).
6. A maintainer will review. Please be responsive to feedback — we aim to keep reviews friendly and fast.

By contributing, you agree that your contributions will be licensed under the project's [MIT License](./LICENSE).

## Reporting bugs & requesting features

Please use the [issue templates](https://github.com/raman0c17/mocky/issues/new/choose). Include:

- What you expected to happen vs. what actually happened
- Steps to reproduce (a minimal `.md` sample is ideal)
- Your OS, architecture, and Python version
- Relevant logs or stack traces

Thank you for helping make Mocky better! 💛
