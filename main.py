import os
from ppt_generator import PowerPointGenerator
from file_manager import FileManager
from markdown_parser import MarkdownParser
from template_lib import TemplateLibrary
from agent_prompter import AgentPromptBuilder


INPUT_DIR = "input_files"
OUTPUT_DIR = "presentations"
MARKDOWN_OUTPUT_DIR = "generated_markdowns"
PROMPT_OUTPUT_DIR = "prompt_outputs"


def safe_file_name(text):
    name = text.strip().replace(" ", "_")
    name = "".join(c for c in name if c.isalnum() or c in "_-.")
    return name or "presentation"


def save_prompt_bundle(prompts, output_dir, base_name):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{base_name}_prompts.txt")
    with open(path, "w", encoding="utf-8") as prompt_file:
        for agent, prompt in prompts.items():
            prompt_file.write(f"=== {agent} ===\n")
            prompt_file.write(prompt)
            prompt_file.write("\n\n")
    return path


def select_template():
    templates = TemplateLibrary.list_templates()
    print("\nAvailable templates:")
    for idx, template_name in enumerate(templates, start=1):
        template = TemplateLibrary.get_template(template_name)
        print(f"{idx}: {template_name} - {template['description']}")

    while True:
        choice = input("Select a template (number): ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(templates):
                return templates[index]
        print("Invalid template selection. Please enter a valid number.")


def prompt_for_idea():
    idea = input("Enter the presentation idea: ").strip()
    if not idea:
        print("An idea is required to generate a presentation.")
    return idea


def convert_markdown_to_ppt(markdown_path, output_dir):
    parser = MarkdownParser()
    parsed_data = parser.parse_markdown(markdown_path)
    presentation_title = parsed_data.get("presentation_title") or safe_file_name(os.path.basename(markdown_path).replace(".md", ""))
    slides = parsed_data.get("slides", [])

    for slide in slides:
        for i, content in enumerate(slide.get("content", [])):
            if isinstance(content, dict) and "image" in content:
                image_path = FileManager.download_image(content["image"], output_dir)
                if image_path:
                    slide["content"][i]["image"] = image_path

    ppt_generator = PowerPointGenerator()
    output_path = os.path.abspath(os.path.join(output_dir, f"{presentation_title}.pptx"))
    print(f"Saving presentation to: {output_path}")
    ppt_generator.create_presentation(slides, output_path)
    if os.path.exists(output_path):
        print(f"Presentation successfully saved at: {output_path}")
    else:
        print(f"Error: Presentation not saved at {output_path}. Check PowerPoint permissions or path validity.")


def idea_flow():
    idea = prompt_for_idea()
    if not idea:
        return

    template_name = select_template()
    markdown_text = TemplateLibrary.build_markdown(idea, template_name)
    markdown_file_name = f"{safe_file_name(idea)}.md"
    markdown_path = TemplateLibrary.save_markdown(markdown_text, MARKDOWN_OUTPUT_DIR, markdown_file_name)
    print(f"Generated markdown saved to: {markdown_path}")

    prompts = AgentPromptBuilder.build_all_prompts(idea, template_name)
    prompt_file_path = save_prompt_bundle(prompts, PROMPT_OUTPUT_DIR, safe_file_name(idea))
    print(f"Prompt bundle saved to: {prompt_file_path}")

    convert_markdown_to_ppt(markdown_path, OUTPUT_DIR)


def existing_file_flow(files):
    print("\nAvailable Markdown Files:")
    for idx, file_name in enumerate(files, start=1):
        print(f"{idx}: {file_name}")

    choice = input("Select a file number to convert to PPT: ").strip()
    if not choice.isdigit():
        print("Invalid selection. Please enter a valid number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(files):
        print("Invalid selection. Please try again.")
        return

    markdown_path = os.path.join(INPUT_DIR, files[index])
    convert_markdown_to_ppt(markdown_path, OUTPUT_DIR)


def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(MARKDOWN_OUTPUT_DIR, exist_ok=True)
    os.makedirs(PROMPT_OUTPUT_DIR, exist_ok=True)

    while True:
        files = FileManager.scan_directory(INPUT_DIR, extension=".md")
        print("\nChoose an action:")
        print("1: Generate a presentation from an idea")
        if files:
            print("2: Convert an existing Markdown file to PPT")
        print("0: Exit")

        choice = input("Select an action: ").strip()
        if choice == "0":
            break
        if choice == "1":
            idea_flow()
        elif choice == "2" and files:
            existing_file_flow(files)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
