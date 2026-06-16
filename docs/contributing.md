# Contributing

Thanks for your interest in improving Mocky! The full guide lives in
[`CONTRIBUTING.md`](https://github.com/raman0c17/mocky/blob/master/CONTRIBUTING.md).
Here's the short version.

## Dev setup

```bash
git clone https://github.com/raman0c17/mocky.git
cd mocky
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Before you open a PR

```bash
ruff check .
ruff format --check .
pytest
```

- Keep changes **cross-platform** — no OS-specific dependencies on the default path.
- Follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.
- Add or update tests where it makes sense.

## Good first issues

- Add a new template to the [template library](templates.md).
- Add a new agent to the [prompt builder](agents.md).
- Improve these docs.

## Code of Conduct

This project follows the
[Contributor Covenant](https://github.com/raman0c17/mocky/blob/master/CODE_OF_CONDUCT.md).
