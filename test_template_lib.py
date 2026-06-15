import unittest
from template_lib import TemplateLibrary, TEMPLATES


class TestTemplateLibrary(unittest.TestCase):
    def test_list_templates_returns_template_names(self):
        template_names = TemplateLibrary.list_templates()
        self.assertIn("basic", template_names)
        self.assertIn("product-launch", template_names)

    def test_get_template_returns_default_for_unknown(self):
        template = TemplateLibrary.get_template("unknown-template")
        self.assertEqual(template["name"], "basic")

    def test_build_markdown_contains_idea_and_template(self):
        idea = "New startup pitch"
        markdown_text = TemplateLibrary.build_markdown(idea, "basic")
        self.assertIn(idea, markdown_text)
        self.assertIn("## Overview", markdown_text)

    def test_save_markdown_writes_file(self):
        markdown_text = "# Example Presentation\n\n## Slide 1\nContent"
        with unittest.mock.patch("template_lib.open", unittest.mock.mock_open()) as mock_file:
            with unittest.mock.patch("template_lib.os.makedirs") as mock_makedirs:
                path = TemplateLibrary.save_markdown(markdown_text, "generated_markdowns", "example.md")
                self.assertTrue(path.endswith("example.md"))
                mock_makedirs.assert_called_once_with("generated_markdowns", exist_ok=True)
                mock_file.assert_called_once_with(path, "w", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
