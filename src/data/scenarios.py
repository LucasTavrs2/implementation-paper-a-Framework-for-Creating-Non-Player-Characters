PLAYER_CHOICES = [
    "por favor, me ajuda",
    "faz seu trabalho logo",
    "obrigado",
    "inútil",
]

INPUT_TO_CATEGORY = {
    "por favor, me ajuda": "help_polite",
    "faz seu trabalho logo": "help_rude",
    "obrigado": "thanks",
    "inútil": "insult",
    "inutil": "insult",
}

CATEGORY_TO_EMOTION = {
    "help_polite": "pride",
    "help_rude": "resentment",
    "thanks": "satisfaction",
    "insult": "reproach",
}

POSITIVE_SEQUENCE = [
    "por favor, me ajuda",
    "obrigado",
]

NEGATIVE_SEQUENCE = [
    "faz seu trabalho logo",
    "inútil",
]