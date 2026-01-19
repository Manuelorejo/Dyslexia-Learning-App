# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 09:12:19 2026

@author: Oreoluwa
"""

import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key= api_key)

def simplify_text(text: str) -> str:
    prompt = f"""
Rewrite the following text for a child with dyslexia.

Rules:
- Use very simple words
- Use short sentences
- Keep the meaning
- One idea per sentence

Text:
{text}
"""


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

