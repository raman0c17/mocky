"""Mocky — turn an idea into a polished PowerPoint deck.

Public API:
    MarkdownParser       Parse Markdown into a slide model.
    PowerPointGenerator  Render a slide model to a cross-platform .pptx.
    FileManager          Scan directories and download referenced images.
    TemplateLibrary      Scaffold Markdown from an idea + template.
    AgentPromptBuilder   Build prompt bundles for AI agents/CLIs.
"""

from .agent_prompter import AgentPromptBuilder
from .file_manager import FileManager
from .markdown_parser import MarkdownParser
from .ppt_generator import PowerPointGenerator
from .template_lib import TemplateLibrary

__version__ = "0.2.0"

__all__ = [
    "AgentPromptBuilder",
    "FileManager",
    "MarkdownParser",
    "PowerPointGenerator",
    "TemplateLibrary",
    "__version__",
]
