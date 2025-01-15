import markdown
from bs4 import BeautifulSoup


class MarkdownParser:
    @staticmethod
    def parse_markdown(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        html_content = markdown.markdown(markdown_content)
        soup = BeautifulSoup(html_content, "html.parser")

        slides = []
        current_slide = {"title": None, "content": []}
        for element in soup.find_all(["h1", "h2", "img", "a", "p"]):
            if element.name == "h1":
                if current_slide["title"] is not None:
                    slides.append(current_slide)
                    current_slide = {"title": None, "content": []}
                current_slide["title"] = element.text
            elif element.name == "h2":
                current_slide["content"].append(element.text)
            elif element.name == "img":
                current_slide["content"].append({"image": element["src"]})
            elif element.name == "a":
                current_slide["content"].append({"link": element["href"]})
            elif element.name == "p":
                current_slide["content"].append(element.text)
        if current_slide["title"] is not None:
            slides.append(current_slide)
        return slides
