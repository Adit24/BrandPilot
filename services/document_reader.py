from io import BytesIO
from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_document(filename, file_bytes):
    ext = Path(filename).suffix.lower()

    if ext == ".pdf":
        reader = PdfReader(BytesIO(file_bytes))
        pages = []
        for number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            if text.strip():
                pages.append(f"[Page {number}]\n{text}")
        return "\n\n".join(pages)

    if ext == ".docx":
        document = Document(BytesIO(file_bytes))
        paragraphs = [
            p.text.strip()
            for p in document.paragraphs
            if p.text.strip()
        ]
        return "\n".join(paragraphs)

    if ext in (".txt", ".md"):
        return file_bytes.decode("utf-8-sig")

    raise ValueError("Unsupported file type. Upload PDF, DOCX, TXT or MD.")


def validate_document(text, max_chars=50000):
    if not text or not text.strip():
        raise ValueError("No readable text was found in this document.")

    if len(text) > max_chars:
        return text[:max_chars], True

    return text, False
