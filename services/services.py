import replicate

def generate_image(sentence: str):
    prompt = f"""
Simple flat illustration for a children's learning book.
Minimal background.
Clear subject.
No text.
Scene: {sentence}
"""

    output = replicate.run(
        "stability-ai/sdxl",
        input={
            "prompt": prompt,
            "width": 768,
            "height": 768,
            "num_outputs": 1
        }
    )

    return output[0]  # image URL
