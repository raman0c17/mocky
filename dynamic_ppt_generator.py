import os
import win32com.client as win32

def create_dynamic_presentation():
    # PowerPoint Slide Layout Constants
    ppLayoutTitle = 1
    ppLayoutText = 2
    ppLayoutBlank = 12

    # Correct Animation/Transition Effects Constants from Documentation
    ppEffectNone = 0          # No effect
    ppEffectCut = 257         # Cut transition
    ppEffectWipeRight = 2819  # Correct value for Wipe Right transition

    # Set up file paths
    folder_path = r"C:\presentation"
    image_path = os.path.join(folder_path, "Image.jpg")
    save_path = os.path.join(folder_path, "DynamicPresentation.pptx")

    # Ensure the output folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Launch PowerPoint application
    print("Launching PowerPoint...")
    pptApp = win32.Dispatch("PowerPoint.Application")
    pptApp.Visible = True

    # Create a new presentation
    print("Creating new presentation...")
    pptPres = pptApp.Presentations.Add()

    try:
        # --- Slide 1: Title Slide ---
        print("Adding Slide 1...")
        pptSlide = pptPres.Slides.Add(1, ppLayoutTitle)
        pptSlide.Shapes[0].TextFrame.TextRange.Text = "Welcome to the Presentation"
        pptSlide.Shapes[1].TextFrame.TextRange.Text = "Created Dynamically Using Python"
        pptSlide.SlideShowTransition.EntryEffect = ppEffectCut
        pptSlide.SlideShowTransition.Duration = 2

        # --- Slide 2: Content Slide ---
        print("Adding Slide 2...")
        pptSlide = pptPres.Slides.Add(2, ppLayoutText)
        pptSlide.Shapes[0].TextFrame.TextRange.Text = "Key Features"
        pptSlide.Shapes[1].TextFrame.TextRange.Text = (
            "1. Automated Slide Creation\n"
            "2. Dynamic Animations\n"
            "3. Custom Transitions"
        )
        pptSlide.SlideShowTransition.EntryEffect = ppEffectNone

        # --- Slide 3: Blank Slide with an Image ---
        print("Adding Slide 3...")
        pptSlide = pptPres.Slides.Add(3, ppLayoutBlank)
        if os.path.exists(image_path):
            shape = pptSlide.Shapes.AddPicture(
                FileName=image_path,
                LinkToFile=False,
                SaveWithDocument=True,
                Left=100,
                Top=100,
                Width=400,
                Height=300
            )
            shape.AnimationSettings.EntryEffect = ppEffectNone
        else:
            print(f"Warning: Image not found at {image_path}. Skipping image slide.")

        # --- Apply Transitions to All Slides ---
        print("Applying transitions to all slides...")
        slide_count = pptPres.Slides.Count
        for i in range(1, slide_count + 1):
            slide = pptPres.Slides.Item(i)
            try:
                print(f"Setting transition for slide {i}...")
                slide.SlideShowTransition.EntryEffect = ppEffectWipeRight
                slide.SlideShowTransition.Duration = 1
            except Exception as e:
                print(f"Failed to apply transition on Slide {i}: {e}")
                # Fallback to a safer transition
                slide.SlideShowTransition.EntryEffect = ppEffectNone

        # --- Save the Presentation ---
        print(f"Saving presentation to {save_path}...")
        pptPres.SaveAs(save_path)
        print(f"Presentation saved successfully at {save_path}.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up: Close the presentation and quit PowerPoint
        print("Closing PowerPoint...")
        pptPres.Close()
        pptApp.Quit()

if __name__ == "__main__":
    create_dynamic_presentation()
