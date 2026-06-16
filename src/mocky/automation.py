import os
import comtypes.client

def create_presentation():
    # Define file paths
    folder_path = "C:\\presentation"
    presentation_path = os.path.join(folder_path, "DynamicPresentation.pptx")
    image_path = os.path.join(folder_path, "Image.jpg")
    
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Initialize PowerPoint application
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = True
    
    # Create a new presentation
    presentation = powerpoint.Presentations.Add()
    
    # Slide 1: Title Slide
    slide1 = presentation.Slides.Add(1, 1)  # ppLayoutTitle
    slide1.Shapes[0].TextFrame.TextRange.Text = "Welcome to the Presentation"
    slide1.Shapes[1].TextFrame.TextRange.Text = "Created Dynamically Using Python"
    slide1.SlideShowTransition.EntryEffect = 6  # ppEffectBoxIn
    slide1.SlideShowTransition.Duration = 2
    
    # Slide 2: Content Slide with Animations
    slide2 = presentation.Slides.Add(2, 2)  # ppLayoutText
    slide2.Shapes[0].TextFrame.TextRange.Text = "Key Features"
    slide2.Shapes[1].TextFrame.TextRange.Text = (
        "1. Automated Slide Creation\n"
        "2. Dynamic Animations\n"
        "3. Custom Transitions"
    )
    slide2.Shapes[1].AnimationSettings.EntryEffect = 8  # ppEffectFlyFromLeft
    
    # Slide 3: Image Slide
    slide3 = presentation.Slides.Add(3, 12)  # ppLayoutBlank
    if os.path.exists(image_path):
        slide3.Shapes.AddPicture(FileName=image_path, LinkToFile=False, SaveWithDocument=True, Left=100, Top=100, Width=400, Height=300)
        slide3.Shapes[0].AnimationSettings.EntryEffect = 15  # ppEffectFade
    else:
        print(f"Image not found at {image_path}. Skipping image addition.")
    
    # Apply Transitions to All Slides
    for slide in presentation.Slides:
        slide.SlideShowTransition.EntryEffect = 14  # ppEffectWipeRight
        slide.SlideShowTransition.Duration = 1
    
    # Save the presentation
    presentation.SaveAs(presentation_path)
    print(f"Presentation saved at: {presentation_path}")
    
    # Close the application
    powerpoint.Quit()

# Run the function
create_presentation()
