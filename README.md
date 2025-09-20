# transcript_pdf
Transcribes PDF files to Markdown files.

Works only with PDF files, including PDF files generated from scanned documents (using OCR).

## Prerequisites

```
pip install uv

uv venv .venv
source .venv/bin/activate
uv init

# tessaract for OCR recognition
brew install tesseract
brew install tesseract-lang # idiom packages (optional)
brew install poppler

uv add pdf2image pillow pytesseract

# to verify the installation
which tesseract
tesseract --version

uv pip freeze > requirements.txt

# to run
uv run python main.py

````

## Note
For an accurated result, it may requires you to define the language of your PDF file:

```
# English
ocr_pdf(pdf_path, lang="eng"): 

# Portuguese:
ocr_pdf(pdf_path, lang="por"):
```
