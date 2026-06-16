import re


def reverse_words(sentence: str) -> str:
    """Return the words of sentence in reversed order."""
    if not isinstance(sentence, str):
        raise TypeError(f"Expected str, got {type(sentence).__name__}")
    return " ".join(sentence.split(" ")[::-1])


def truncate(text: str, max_len: int) -> str:
    """Return text truncated to max_len characters with '...' appended if shortened."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."


def count_vowels(s: str) -> int:
    """Return the count of vowels (a, e, i, o, u) in s, case-insensitive."""
    return sum(1 for ch in s.lower() if ch in "aeiou")


def to_title_case(s: str) -> str:
    """Return s converted to title case."""
    return s.title()


def remove_duplicates(items: list) -> list:
    """Return items with duplicates removed, preserving original order."""
    seen: set = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def parse_csv_line(line: str) -> list[str]:
    """Split a CSV line by comma and return the fields."""
    try:
        return line.split(",")
    except AttributeError as exc:
        raise TypeError(f"Expected str, got {type(line).__name__}") from exc


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9-]", "", text)
    return text
