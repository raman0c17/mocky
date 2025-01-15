import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import main

class TestMain(unittest.TestCase):

    @patch('main.os.makedirs')
    @patch('main.input')
    @patch('main.PowerPointGenerator')
    @patch('main.FileManager.scan_directory')
    @patch('main.MarkdownParser')
    def test_main_valid_choice(self, MockMarkdownParser, mock_scan_directory, MockPowerPointGenerator, mock_input, mock_makedirs):
        # Setup mocks
        mock_scan_directory.return_value = ['test_file.txt']
        mock_input.side_effect = ['a', '0']
        mock_parser = MockMarkdownParser.return_value
        mock_parser.parse_markdown.return_value = [{"title": "Test", "content": []}]
        mock_ppt = MockPowerPointGenerator.return_value

        # Run main
        main.main()

        # Verify directory creation
        mock_makedirs.assert_any_call('input_files', exist_ok=True)
        mock_makedirs.assert_any_call('presentations', exist_ok=True)

        # Verify scan_directory was called twice due to the loop
        assert mock_scan_directory.call_count == 2
        mock_scan_directory.assert_has_calls([
            unittest.mock.call('input_files'),
            unittest.mock.call('input_files')
        ])

        # Verify presentation creation
        mock_ppt.create_presentation.assert_called_once_with(
            [{"title": "Test", "content": []}],
            os.path.join('presentations', 'test_file.pptx')
        )

    @patch('main.os.makedirs')
    @patch('main.input')
    @patch('main.FileManager.scan_directory')
    def test_main_invalid_choice(self, mock_scan_directory, mock_input, mock_makedirs):
        mock_scan_directory.return_value = ['test_file.txt']
        mock_input.side_effect = ['z', '0']

        with patch('builtins.print') as mock_print:
            main.main()
            mock_print.assert_any_call("Invalid choice. Please try again.")

        mock_makedirs.assert_any_call('input_files', exist_ok=True)
        mock_makedirs.assert_any_call('presentations', exist_ok=True)

if __name__ == '__main__':
    unittest.main()