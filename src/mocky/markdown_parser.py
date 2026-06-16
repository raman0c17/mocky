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
        if markdown is None or BeautifulSoup is None:
            raise RuntimeError(
                "Missing dependencies for Markdown parsing. Install: markdown beautifulsoup4"
            )

        with open(file_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)
        soup = BeautifulSoup(html_content, "html.parser")

        slides = []
        presentation_title = None

        for element in soup.find_all(["h1", "h2", "p", "ul", "ol", "img", "a"]):
            if element.name == "h1":
                # Use the first `h1` as the title of the presentation
                if not presentation_title:
                    presentation_title = element.text
            elif element.name == "h2":
                # Start a new slide for each `##` (h2)
                slides.append({"title": element.text, "content": []})
            elif slides and element.name in ["p", "ul", "ol", "img", "a"]:
                # Add content to the current slide
                current_slide = slides[-1]
                if element.name == "img":
                    current_slide["content"].append({"image": element["src"]})
                elif element.name == "a":
                    current_slide["content"].append({"link": element["href"]})
                else:
                    current_slide["content"].append(element.text)

        # Return the title and slides
        return {"presentation_title": presentation_title, "slides": slides}
