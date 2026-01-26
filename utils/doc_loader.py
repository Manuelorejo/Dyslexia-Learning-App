# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 08:43:10 2026

@author: Oreoluwa
"""

from pypdf import PdfReader

def load_txt(file) -> str:
    return file.read().decode("utf-8")

def load_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text
