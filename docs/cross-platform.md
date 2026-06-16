# Cross-platform, Docker & library

## Platform-agnostic by design

Mocky's rendering engine is built on [`python-pptx`](https://python-pptx.readthedocs.io/),
which is pure Python. That means:

- No Microsoft PowerPoint or Office install required.
- No Windows-only COM (`pywin32` / `comtypes`) dependency.
- Identical behavior on **Windows (x64/ARM)**, **macOS (Intel/Apple Silicon)**, and **Linux**.

The public API is stable across platforms:

```python
from mocky import PowerPointGenerator
PowerPointGenerator().create_presentation(slides, "out.pptx")
```

## Use it as a library

Mocky is a normal installable package:

```bash
pip install mocky
```

```python
from mocky import (
    MarkdownParser,
    PowerPointGenerator,
    TemplateLibrary,
    AgentPromptBuilder,
    FileManager,
)
```

## Run it in a container

A slim image is provided (`python:3.12-slim`, non-root user, no Office needed):

```bash
# Build
docker build -t mocky .

# Run, mounting your input/output folders
docker run --rm -it \
  -v "$PWD/input_files:/app/input_files" \
  -v "$PWD/presentations:/app/presentations" \
  mocky
```

!!! tip "Multi-arch images"
    Because the stack is pure Python, the same Dockerfile builds for both
    `linux/amd64` and `linux/arm64` — e.g. with
    `docker buildx build --platform linux/amd64,linux/arm64`.
