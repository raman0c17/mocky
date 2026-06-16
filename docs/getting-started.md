# Getting started

## Requirements

- Python 3.9 or newer
- Works on Windows (x64/ARM), macOS (Intel/Apple Silicon), and Linux

## Install

=== "From PyPI"

    ```bash
    pip install mocky
    ```

=== "From source"

    ```bash
    git clone https://github.com/raman0c17/mocky.git
    cd mocky
    python3 -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -e ".[dev]"
    ```

!!! tip "externally-managed-environment error?"
    On macOS/Homebrew Python, install inside a virtual environment (the `python3 -m venv .venv` step above). Avoid `--break-system-packages`.

## Your first deck

```bash
mocky
```

Choose **"Generate a presentation from an idea"**, type your idea, pick a
template, and Mocky writes a `.pptx` into `presentations/`.

## Verify your install

```bash
python -c "import mocky; print(mocky.__version__)"
```

Next: see [Usage](usage.md) for the CLI and library workflows.
