# List comprehension style
def scrolling_text(text):
    return [str.upper(text[i:] + text[:i]) for i in range(len(text))]



