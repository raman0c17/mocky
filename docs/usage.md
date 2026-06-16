# Usage

Mocky can be driven two ways: the interactive **CLI** or the **Python library**.

## The slide model

A deck is a list of slide dicts:

```python
slides = [
    {"title": "Slide title", "content": ["A bullet", "Another bullet"]},
    {"title": "With a picture", "content": [{"image": "/path/to/local.png"}]},
    {"title": "With a link", "content": [{"link": "https://example.com"}]},
]
```

Markdown maps to this model as: the first `#` is the deck title, every `##`
starts a new slide, and paragraphs / lists / images / links become content items.

## CLI

```bash
mocky
```

You'll get a menu:

1. **Generate from an idea** — pick a template, Mocky scaffolds Markdown into
   `generated_markdowns/`, writes agent prompts into `prompt_outputs/`, and
   renders a `.pptx` into `presentations/`.
2. **Convert an existing Markdown file** — drop a `.md` file in `input_files/`
   and convert it directly.

## Library

### Workflow A — from an idea

```python
from mocky import TemplateLibrary, MarkdownParser, PowerPointGenerator

idea = "Launching Mocky 1.0 to the open-source community"
markdown = TemplateLibrary.build_markdown(idea, "product-launch")
path = TemplateLibrary.save_markdown(markdown, "generated_markdowns", "launch.md")

parsed = MarkdownParser().parse_markdown(path)
PowerPointGenerator().create_presentation(parsed["slides"], "presentations/launch.pptx")
```

### Workflow B — from existing Markdown

```python
from mocky import MarkdownParser, PowerPointGenerator

parsed = MarkdownParser().parse_markdown("input_files/my_outline.md")
PowerPointGenerator().create_presentation(parsed["slides"], "presentations/out.pptx")
```

### Build slides yourself

```python
from mocky import PowerPointGenerator

slides = [
    {"title": "Hello", "content": ["First bullet", "Second bullet"]},
    {"title": "Thanks", "content": []},
]
PowerPointGenerator().create_presentation(slides, "presentations/manual.pptx")
```

!!! warning "Images"
    Mocky only fetches `http(s)` image URLs (with a timeout); other schemes are
    skipped. Local image paths must exist on disk or they're ignored.
