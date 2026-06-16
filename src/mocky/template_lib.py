import os
from datetime import datetime


TEMPLATES = {
    "basic": {
        "name": "basic",
        "description": "Simple title slide, key points slides, and a summary slide.",
        "sections": [
            "# {title}",
            "## Overview\n{overview}",
            "## Why It Matters\n{why_it_matters}",
            "## Key Points\n{key_points}",
            "## Next Steps\n{next_steps}",
            "## Summary\n{summary}",
        ],
    },
    "problem-solution": {
        "name": "problem-solution",
        "description": "Problem, solution, benefits, and roadmap structure.",
        "sections": [
            "# {title}",
            "## Problem\n{problem}",
            "## Solution\n{solution}",
            "## Benefits\n{benefits}",
            "## Roadmap\n{roadmap}",
            "## Next Steps\n{next_steps}",
        ],
    },
    "product-launch": {
        "name": "product-launch",
        "description": "Launch narrative with market, features, and adoption plan.",
        "sections": [
            "# {title}",
            "## Market Opportunity\n{market_opportunity}",
            "## Product Features\n{features}",
            "## Go-To-Market\n{go_to_market}",
            "## Success Metrics\n{success_metrics}",
            "## Launch Plan\n{launch_plan}",
        ],
    },
}

DEFAULT_TEMPLATE = "basic"


class TemplateLibrary:
    @staticmethod
    def list_templates():
        return [template["name"] for template in TEMPLATES.values()]

    @staticmethod
    def get_template(template_name):
        return TEMPLATES.get(template_name) or TEMPLATES[DEFAULT_TEMPLATE]

    @staticmethod
    def build_markdown(idea, template_name, additional_fields=None):
        template = TemplateLibrary.get_template(template_name)
        fields = {
            "title": idea,
            "overview": f"An introduction to the idea: {idea}",
            "why_it_matters": f"Why this idea is important and the value it creates.",
            "key_points": "- Key point 1\n- Key point 2\n- Key point 3",
            "next_steps": "- Define goals\n- Build a plan\n- Execute with milestones",
            "summary": f"This presentation outlines the idea '{idea}' and recommended next steps.",
            "problem": f"A clear problem statement for the idea '{idea}'.",
            "solution": f"A solution approach based on the idea '{idea}'.",
            "benefits": "- Benefit 1\n- Benefit 2\n- Benefit 3",
            "roadmap": "- Phase 1\n- Phase 2\n- Phase 3",
            "market_opportunity": f"Market and opportunity context for the idea '{idea}'.",
            "features": "- Feature 1\n- Feature 2\n- Feature 3",
            "go_to_market": "- Target audience\n- Channels\n- Launch activities",
            "success_metrics": "- Metric 1\n- Metric 2\n- Metric 3",
            "launch_plan": "- Preparation\n- Launch\n- Evaluation",
        }
        if additional_fields:
            fields.update(additional_fields)

        rendered_sections = [section.format(**fields) for section in template["sections"]]
        return "\n\n".join(rendered_sections)

    @staticmethod
    def save_markdown(markdown_text, output_dir, file_name=None):
        os.makedirs(output_dir, exist_ok=True)
        if not file_name:
            safe_name = markdown_text.splitlines()[0].strip("# ").replace(" ", "_")
            file_name = f"{safe_name}.md"
        output_path = os.path.join(output_dir, file_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)
        return output_path
