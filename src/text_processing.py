from __future__ import annotations

import html
import os
import re
from typing import List

import docx2txt
from PyPDF2 import PdfReader


def extract_text(file) -> str:
    ext = os.path.splitext(file.name)[1].lower()

    if ext == ".pdf":
        text_parts: List[str] = []
        reader = PdfReader(file)
        for page in reader.pages:
            text_parts.append(page.extract_text() or "")
        return "\n".join(text_parts).strip()

    if ext == ".docx":
        return (docx2txt.process(file) or "").strip()

    if ext == ".txt":
        try:
            return file.read().decode("utf-8").strip()
        except UnicodeDecodeError:
            file.seek(0)
            return file.read().decode("latin-1", errors="ignore").strip()

    raise ValueError("Unsupported file format. Please upload PDF, DOCX, or TXT.")


def normalize_whitespace(text: str) -> str:
    text = html.unescape(text or "")
    text = re.sub(r"\r\n|\r", "\n", text)
    text = re.sub(r"[\t\xa0]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_text(text: str) -> str:
    text = normalize_whitespace(text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s\+\#\-\./]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
