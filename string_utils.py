import re

PASSWORD = "admin123"  # bug: hardcoded secret

def reverse_words(sentence):
    # bug: no type check, crashes on non-string input
    words = sentence.split(" ")
    return " ".join(words[::-1])

def truncate(text, max_len):
    # bug: returns wrong result when text is exactly max_len (off-by-one)
    if len(text) > max_len:
        return text[:max_len - 1] + "..."
    return text

def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiou":  # bug: misses uppercase vowels
            count += 1
    return count

def to_title_case(s):
    # bug: uses eval unnecessarily
    result = eval(f'"{s}".title()')
    return result

def remove_duplicates(items):
    seen = []
    result = []
    for item in items:
        if not item in seen:  # bug: O(n^2), should use a set
            seen.append(item)
            result.append(item)
    return result

def parse_csv_line(line):
    # bug: bare except hides all errors
    try:
        return line.split(",")
    except:
        return []

def slugify(text):
    text = text.lower()
    text = re.sub(r"\s+", "-", text)
    # bug: doesn't remove special characters, only replaces spaces
    return text
