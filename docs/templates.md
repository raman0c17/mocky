# Templates

The template library turns a one-line idea into a structured Markdown outline you
can render directly or refine first.

## Built-in templates

| Template | Best for | Sections |
| --- | --- | --- |
| `basic` | General-purpose decks | Overview, Why It Matters, Key Points, Next Steps, Summary |
| `problem-solution` | Pitches and proposals | Problem, Solution, Benefits, Roadmap, Next Steps |
| `product-launch` | Launch narratives | Market Opportunity, Features, Go-To-Market, Success Metrics, Launch Plan |

## API

```python
from mocky import TemplateLibrary

TemplateLibrary.list_templates()
# ['basic', 'problem-solution', 'product-launch']

markdown = TemplateLibrary.build_markdown("My idea", "problem-solution")
TemplateLibrary.save_markdown(markdown, "generated_markdowns", "my_idea.md")
```

`build_markdown` accepts an optional `additional_fields` dict to override any
section's default text:

```python
markdown = TemplateLibrary.build_markdown(
    "My idea",
    "basic",
    additional_fields={"overview": "A custom overview paragraph."},
)
```

## Adding a template

Templates are plain dictionaries in `src/mocky/template_lib.py`. Add an entry to
`TEMPLATES` with a `name`, `description`, and a list of `sections` (each section
is a Markdown string with `{placeholder}` fields), then send a PR. New templates
are a great [first contribution](contributing.md)!
