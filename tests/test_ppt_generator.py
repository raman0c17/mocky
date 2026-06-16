"""Tests for the cross-platform python-pptx rendering engine."""

import os

from pptx import Presentation

from mocky.ppt_generator import PowerPointGenerator


def test_create_presentation_writes_pptx(tmp_path):
    slides = [
        {"title": "Intro", "content": ["Hello world", "Second bullet"]},
        {"title": "Links", "content": [{"link": "https://example.com"}]},
        {"title": "Title only", "content": []},
    ]
    output_path = os.path.join(str(tmp_path), "deck.pptx")
    PowerPointGenerator().create_presentation(slides, output_path)

    assert os.path.exists(output_path)
    prs = Presentation(output_path)
    assert len(prs.slides) == 3


def test_create_presentation_creates_output_dir(tmp_path):
    nested = os.path.join(str(tmp_path), "nested", "dir")
    output_path = os.path.join(nested, "deck.pptx")
    PowerPointGenerator().create_presentation(
        [{"title": "Solo", "content": ["Only slide"]}], output_path
    )
    assert os.path.exists(output_path)


def test_empty_slides_still_saves(tmp_path):
    output_path = os.path.join(str(tmp_path), "empty.pptx")
    PowerPointGenerator().create_presentation([], output_path)
    assert os.path.exists(output_path)
