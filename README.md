# Mocky — Markdown to PowerPoint Generator

Mocky converts Markdown files into PowerPoint presentations (`.pptx`). It scans an `input_files/` folder for Markdown, parses it into a slide model, downloads any referenced images, and then generates a `.pptx` using Windows PowerPoint automation.

> Note: PPT generation uses Win32 COM automation (`pywin32`) and therefore works on Windows with Microsoft PowerPoint installed.

---

## What it does

1. **Scans** `input_files/` for `*.md` files.
2. **Parses** the chosen Markdown file into:
   - `presentation_title` (first `#`/H1)
   - `slides` (each `##`/H2 becomes a new slide)
3. **Downloads images** referenced by Markdown image tags (converted to HTML `<img src=...>`).
4. **Generates** a PowerPoint file in `presentations/`.

---

## Repository contents

- `main.py`
  - CLI loop to choose a Markdown file
  - Calls parser + PPT generator
- `markdown_parser.py`
  - Markdown → internal slide structure
- `file_manager.py`
  - Directory scan
  - Image download helper
- `ppt_generator.py`
  - Creates `.pptx` using `win32com.client`
- `dynamic_ppt_generator.py`
  - Example script that builds a hard-coded presentation (demo)
- `automation.py`
  - Another example script using COM to build a presentation (demo)
- `test_main.py`
  - Unit tests for `main.py`
- `.gitignore`

---

## Input format (Markdown)

Mocky’s parser treats:

- `# <title>` (first H1) → presentation title
- `## <slide title>` → starts a new slide
- Content supported for slide content:
  - Paragraphs
  - Lists (ul/ol)
  - Images (`![alt](image_url_or_path)`) → captured as `{ "image": <src> }`
  - Links (`[text](url)`) → captured as `{ "link": <href> }`

### Example

```md
# My Presentation

## Slide 1
This is slide 1 text.

![Example image](https://example.com/image.jpg)

## Slide 2
- Bullet A
- Bullet B

More text.
```

---

## Images

If your Markdown contains an image like:

```md
![any text](https://some-domain.com/cat.png)
```

Mocky will:
- Download it via `requests.get(url, stream=True)`
- Save it to the output directory (the `output_dir` passed from `main.py`, i.e. `presentations/`)
- Update the internal slide model so the PPT generator can embed the downloaded file.

If an image download fails, the code prints an error and continues.

---

## How to run

### 1) Create folders

The program expects these folders:
- `input_files/` (place your `*.md` files here)
- `presentations/` (output folder for generated `*.pptx`)

`main.py` will create them if missing.

### 2) Install dependencies

```bash
pip install markdown beautifulsoup4 requests pywin32
```

### 3) Run

```bash
python main.py
```

Then:
- Choose a file by typing the displayed letter (a-z), or `0` to exit.
- The resulting file will be saved as:
  - `presentations/<presentation_title>.pptx`

---

## Notes / limitations (based on current implementation)

- **Windows-only PPT generation**: requires PowerPoint installed and COM accessible.
- **Slide text placeholder behavior**:
  - `ppt_generator.py` joins `slide["content"]` items into a single text block.
  - If content items are dicts (e.g., images/links), it currently formats them as `(<first_dict_key>)` rather than using real link/image text.
- **Layout & positioning**:
  - Uses hardcoded placeholder layouts and fixed image position/size (`Left=100, Top=100, Width=400, Height=300`).

---

## Testing

Run unit tests:

```bash
python -m unittest test_main.py
```

---

## Example workflow

1. Put `my_slides.md` in `input_files/`
2. Run `python main.py`
3. Select `my_slides.md`
4. Open `presentations/<title>.pptx`

