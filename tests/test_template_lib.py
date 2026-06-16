"""Tests for the idea -> Markdown template library."""

from mocky.template_lib import DEFAULT_TEMPLATE, TemplateLibrary


def test_list_templates_includes_known_templates():
    templates = TemplateLibrary.list_templates()
    assert "basic" in templates
    assert "problem-solution" in templates
    assert "product-launch" in templates


def test_get_template_falls_back_to_default():
    template = TemplateLibrary.get_template("does-not-exist")
    assert template["name"] == DEFAULT_TEMPLATE


def test_build_markdown_contains_idea_as_title():
    markdown = TemplateLibrary.build_markdown("My Great Idea", "basic")
    assert markdown.startswith("# My Great Idea")
    assert "## Overview" in markdown
    assert "## Summary" in markdown


def test_build_markdown_problem_solution_sections():
    markdown = TemplateLibrary.build_markdown("Fix onboarding", "problem-solution")
    assert "## Problem" in markdown
    assert "## Solution" in markdown
    assert "## Roadmap" in markdown


def test_additional_fields_override_defaults():
    markdown = TemplateLibrary.build_markdown(
        "Launch", "basic", additional_fields={"overview": "Custom overview text"}
    )
    assert "Custom overview text" in markdown


def test_save_markdown_writes_file(tmp_path):
    markdown = TemplateLibrary.build_markdown("Saved Idea", "basic")
    path = TemplateLibrary.save_markdown(markdown, str(tmp_path), "saved.md")
    with open(path, encoding="utf-8") as f:
        assert f.read().startswith("# Saved Idea")
