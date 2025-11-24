BAD_WORDS = {'badword1','badword2'}

def contains_bad_word(text: str) -> bool:
    if not text: return False
    t = text.lower()
    return any(w in t for w in BAD_WORDS)
