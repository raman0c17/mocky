import os
import unittest
from unittest.mock import patch, mock_open
import src.mocky.main as main


class TestMain(unittest.TestCase):

    @patch('main.open', new_callable=mock_open)
    @patch('main.os.makedirs')
    @patch('main.PowerPointGenerator')
    @patch('main.AgentPromptBuilder.build_all_prompts')
    @patch('main.TemplateLibrary.save_markdown')
    @patch('main.TemplateLibrary.build_markdown')
    @patch('main.MarkdownParser')
    @patch('main.FileManager.scan_directory')
    @patch('main.input')
    def test_main_idea_flow(self, mock_input, mock_scan_directory, MockMarkdownParser, mock_build_markdown, mock_save_markdown, mock_build_prompts, MockPowerPointGenerator, mock_makedirs, mock_open_file):
        mock_scan_directory.return_value = []
        mock_input.side_effect = ['1', 'My idea', '1', '0']

        mock_build_markdown.return_value = '# My idea\n\n## Slide 1\nContent'
        mock_save_markdown.return_value = os.path.join('generated_markdowns', 'My_idea.md')
        mock_build_prompts.return_value = {'claude api': 'prompt text'}

        mock_parser = MockMarkdownParser.return_value
        mock_parser.parse_markdown.return_value = {
            'presentation_title': 'My idea',
            'slides': [{'title': 'Slide 1', 'content': []}]
        }
        mock_ppt = MockPowerPointGenerator.return_value

        main.main()

        mock_makedirs.assert_any_call('input_files', exist_ok=True)
        mock_makedirs.assert_any_call('presentations', exist_ok=True)
        mock_makedirs.assert_any_call('generated_markdowns', exist_ok=True)
        mock_makedirs.assert_any_call('prompt_outputs', exist_ok=True)

        mock_build_markdown.assert_called_once_with('My idea', 'basic')
        mock_build_prompts.assert_called_once_with('My idea', 'basic')
        mock_ppt.create_presentation.assert_called_once()

    @patch('main.os.makedirs')
    @patch('main.FileManager.scan_directory')
    @patch('main.input')
    def test_main_invalid_choice(self, mock_input, mock_scan_directory, mock_makedirs):
        mock_scan_directory.return_value = []
        mock_input.side_effect = ['9', '0']

        with patch('builtins.print') as mock_print:
            main.main()
            mock_print.assert_any_call('Invalid choice. Please try again.')

        mock_makedirs.assert_any_call('input_files', exist_ok=True)
        mock_makedirs.assert_any_call('presentations', exist_ok=True)
        mock_makedirs.assert_any_call('generated_markdowns', exist_ok=True)
        mock_makedirs.assert_any_call('prompt_outputs', exist_ok=True)


if __name__ == '__main__':
    unittest.main()
