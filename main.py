import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def ocr_pdf(pdf_path, lang="eng"):
    pages = convert_from_path(pdf_path)
    text_content = []

    for i, page in enumerate(pages):
        # Convert page into text
        text = pytesseract.image_to_string(page, lang=lang)
        text_content.append(text)

    return "\n".join(text_content)

# Example:
if __name__ == "__main__":
    source_file = "contrato.pdf"
    source_extension = source_file.split(".")[-1]

    extracted_text = ocr_pdf(source_file, lang="por")  # "eng" for en-US
    print(extracted_text)

    with open(source_file.replace(source_extension, "md"), "w", encoding="utf-8") as f:
        f.write(extracted_text)