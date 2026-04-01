import unicodedata

from src.data.scenarios import INPUT_TO_CATEGORY
from src.models.stimulus import Stimulus


def _strip_accents(text: str) -> str:
    return "".join(
        char
        for char in unicodedata.normalize("NFD", text)
        if unicodedata.category(char) != "Mn"
    )


def normalize_text(text: str) -> str:
    text = text.strip().lower()
    text = " ".join(text.split())
    return text


def appraise(text: str) -> Stimulus:
    normalized = normalize_text(text)
    normalized_no_accents = _strip_accents(normalized)

    if normalized in INPUT_TO_CATEGORY:
        return Stimulus(text=normalized, category=INPUT_TO_CATEGORY[normalized])

    if normalized_no_accents in INPUT_TO_CATEGORY:
        return Stimulus(
            text=normalized,
            category=INPUT_TO_CATEGORY[normalized_no_accents],
        )

    if "obrigad" in normalized_no_accents:
        category = "thanks"
    elif "inutil" in normalized_no_accents:
        category = "insult"
    elif "trabalho" in normalized_no_accents or "logo" in normalized_no_accents:
        category = "help_rude"
    elif "ajuda" in normalized_no_accents or "por favor" in normalized_no_accents:
        category = "help_polite"
    else:
        category = "help_polite"

    return Stimulus(text=normalized, category=category)