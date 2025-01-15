import os

try:
    import win32com.client as win32
except ImportError as e:
    print("Error: PyWin32 is not installed or not configured properly.")
    print("Install or upgrade it using: pip install --upgrade pywin32")
    raise e

# Manually define the PowerPoint layout constants
PP_LAYOUT_TITLE = 1
PP_LAYOUT_TEXT = 2
PP_LAYOUT_BLANK = 12

class PowerPointGenerator:
    def __init__(self):
        """
        Initialize the PowerPoint application.
        """
        try:
            self.pptApp = win32.Dispatch("PowerPoint.Application")
            self.pptApp.Visible = True
        except Exception as e:
            print("Error initializing PowerPoint application:")
            print(e)
            raise e

    def create_presentation(self, slides, output_path):
        """
        Creates a PowerPoint presentation from a given list of slides.

        :param slides: A list of dictionaries with 'title' and 'content' keys.
        :param output_path: The full path to save the generated PPTX.
        """

        # Check if slides is empty
        if not slides:
            print("Warning: No slides to process. The presentation will be empty.")

        # Check if directory for output_path exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
                print(f"Created the directory for output: {output_dir}")
            except Exception as e:
                print(f"Error creating directory {output_dir}: {e}")
                return  # Abort if we cannot create the directory

        try:
            # Create new presentation
            pptPres = self.pptApp.Presentations.Add()
        except Exception as e:
            print("Error creating a new PowerPoint presentation:")
            print(e)
            return

        try:
            for idx, slide in enumerate(slides, start=1):
                # Decide layout based on whether slide["content"] exists
                layout = PP_LAYOUT_TEXT if slide.get("content") else PP_LAYOUT_TITLE

                try:
                    pptSlide = pptPres.Slides.Add(idx, layout)
                except Exception as ex:
                    print(f"Error adding slide {idx} to the presentation: {ex}")
                    continue  # Skip this slide and continue with the next

                # Set title
                try:
                    pptSlide.Shapes[0].TextFrame.TextRange.Text = slide.get("title", "Untitled Slide")
                except Exception as ex:
                    print(f"Error setting title on slide {idx}: {ex}")

                # If the layout is PP_LAYOUT_TEXT, fill in the text placeholder
                if layout == PP_LAYOUT_TEXT:
                    try:
                        # Join any string content; show special placeholders for dict items
                        content_text = "\n".join(
                            item if isinstance(item, str) else f"({list(item.keys())[0]})"
                            for item in slide.get("content", [])
                        )
                        pptSlide.Shapes[1].TextFrame.TextRange.Text = content_text
                    except Exception as ex:
                        print(f"Error setting text content on slide {idx}: {ex}")

                # Add images
                for content in slide.get("content", []):
                    if isinstance(content, dict) and "image" in content:
                        try:
                            pptSlide.Shapes.AddPicture(
                                FileName=content["image"],
                                LinkToFile=False,
                                SaveWithDocument=True,
                                Left=100,
                                Top=100,
                                Width=400,
                                Height=300,
                            )
                        except Exception as ex:
                            print(f"Error adding image on slide {idx}: {ex}")

            # Save the presentation
            try:
                pptPres.SaveAs(output_path)
                print(f"Presentation saved at: {output_path}")
            except Exception as e:
                print(f"Error saving the presentation to {output_path}: {e}")

        except Exception as e:
            print(f"Unexpected error while creating the presentation: {e}")
        finally:
            # Attempt to close the presentation and PowerPoint application
            try:
                pptPres.Close()
                self.pptApp.Quit()
            except Exception as ex:
                print("Error closing PowerPoint:")
                print(ex)
