import os
from ppt_generator import PowerPointGenerator
from file_manager import FileManager
from markdown_parser import MarkdownParser


def main():
    input_dir = "input_files"
    output_dir = "presentations"
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    while True:
        # Scan for Markdown files (.md) instead of .txt
        files = FileManager.scan_directory(input_dir, extension=".md")
        if not files:
            print("No files found. Please add Markdown files (.md) to the 'input_files' folder.")
            break

        # List available files
        print("\nAvailable Files:")
        for idx, file in enumerate(files, start=1):
            print(f"{chr(96 + idx)}: {file}")
        print("0: Exit")

        # Get user choice
        choice = input("Select a file to generate a presentation (a-z or 0): ").strip().lower()
        if choice == "0":
            break

        index = ord(choice) - 96
        if 1 <= index <= len(files):
            selected_file = files[index - 1]
            file_path = os.path.join(input_dir, selected_file)

            # Parse Markdown
            parser = MarkdownParser()
            slides = parser.parse_markdown(file_path)

            # Download images and update paths
            for slide in slides:
                for i, content in enumerate(slide["content"]):
                    if isinstance(content, dict) and "image" in content:
                        image_path = FileManager.download_image(content["image"], output_dir)
                        if image_path:
                            slide["content"][i]["image"] = image_path

            # Generate PowerPoint
            ppt_generator = PowerPointGenerator()
            output_path = os.path.abspath(os.path.join(output_dir, f"{os.path.splitext(selected_file)[0]}.pptx"))

            print(f"Saving presentation to: {output_path}")
            ppt_generator.create_presentation(slides, output_path)

            # Check if the file was created
            if os.path.exists(output_path):
                print(f"Presentation successfully saved at: {output_path}")
            else:
                print(f"Error: Presentation not saved at {output_path}. Check PowerPoint permissions or path validity.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
