import os
import win32com.client as win32


class PowerPointGenerator:
    def __init__(self):
        self.pptApp = win32.Dispatch("PowerPoint.Application")
        self.pptApp.Visible = True

    def create_presentation(self, slides, output_path):
        pptPres = self.pptApp.Presentations.Add()

        try:
            for idx, slide in enumerate(slides, 1):
                layout = win32.constants.ppLayoutText if slide["content"] else win32.constants.ppLayoutTitle
                pptSlide = pptPres.Slides.Add(idx, layout)
                pptSlide.Shapes[0].TextFrame.TextRange.Text = slide["title"]
                if layout == win32.constants.ppLayoutText:
                    pptSlide.Shapes[1].TextFrame.TextRange.Text = "\n".join(
                        item if isinstance(item, str) else f"({list(item.keys())[0]})"
                        for item in slide["content"]
                    )
                # Add images
                for content in slide["content"]:
                    if isinstance(content, dict) and "image" in content:
                        pptSlide.Shapes.AddPicture(
                            FileName=content["image"],
                            LinkToFile=False,
                            SaveWithDocument=True,
                            Left=100,
                            Top=100,
                            Width=400,
                            Height=300,
                        )
            # Save presentation
            pptPres.SaveAs(output_path)
            print(f"Presentation saved at: {output_path}")
        except Exception as e:
            print(f"Error creating presentation: {e}")
        finally:
            pptPres.Close()
            self.pptApp.Quit()
