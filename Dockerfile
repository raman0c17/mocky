# syntax=docker/dockerfile:1

# Mocky runs anywhere Python runs. Because the default engine is pure-Python
# (python-pptx), no Microsoft Office / COM dependency is needed in the image.
FROM python:3.12-slim

# Avoid interactive prompts and keep Python output unbuffered
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies first to leverage Docker layer caching
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --upgrade pip && pip install .

# Default working folders (mount these as volumes at runtime)
RUN mkdir -p input_files presentations

# Drop privileges
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["mocky"]
