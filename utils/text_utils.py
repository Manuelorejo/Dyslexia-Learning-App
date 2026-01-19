def split_sentences(text: str, max_sentences=6):
    sentences = [
        s.strip() for s in text.replace("\n", ".").split(".")
        if len(s.strip()) > 3
    ]
    return sentences[:max_sentences]
