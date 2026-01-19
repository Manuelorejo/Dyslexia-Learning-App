# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 09:18:29 2026

@author: Oreoluwa
"""

import os
from dotenv import load_dotenv
import replicate


load_dotenv()
token = os.getenv("REPLICATE_API_KEY")



SDXL_MODEL = "google/imagen-3"



def generate_image(sentence: str):
    prompt = f"""
Simple flat illustration for a children's learning book.
Minimal background.
Clear subject.
No text.
Scene: {sentence}
"""

    client = replicate.Client(api_token=token)

    file_output = client.run(
        SDXL_MODEL,
        input={
            "prompt": prompt,
            "width": 768,
            "height": 768,
            "num_outputs": 1
        }
    )

    return file_output.url





