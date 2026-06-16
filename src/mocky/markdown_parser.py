"""Parse Markdown into Mocky's slide model.

``#`` (first H1) becomes the presentation title; every ``##`` (H2) starts a new
slide. Paragraphs, lists, images and links inside a slide become content items.
"""

from __future__ import annotations

try:
    import markdown
except ImportError:
    markdown = None

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None


class MarkdownParser:
    @staticmethod
    def parse_markdown(file_path):
        """Parse a Markdown file into ``{"presentation_title", "slides"}``."""
        if markdown is None or BeautifulSoup is None:
            raise RuntimeError(
                "Missing dependencies for Markdown parsing. "
                "Install them with: pip install markdown beautifulsoup4"
            )

        with open(file_path, encoding="utf-8") as f:
            markdown_content = f.read()

        html_content = markdown.markdown(markdown_content)
        soup = BeautifulSoup(html_content, "html.parser")

        slides = []
        presentation_title = None

        for element in soup.find_all(["h1", "h2", "p", "ul", "ol", "img", "a"]):
            if element.name == "h1":
                if not presentation_title:
                    presentation_title = element.text
            elif element.name == "h2":
                slides.append({"title": element.text, "content": []})
            elif slides and element.name in ["p", "ul", "ol", "img", "a"]:
                current_slide = slides[-1]
                if element.name == "img":
                    current_slide["content"].append({"image": element["src"]})
                elif element.name == "a":
                    current_slide["content"].append({"link": element["href"]})
                else:
                    current_slide["content"].append(element.text)

        return {"presentation_title": presentation_title, "slides": slides}
