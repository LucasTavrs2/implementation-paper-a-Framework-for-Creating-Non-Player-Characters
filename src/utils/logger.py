import csv
from pathlib import Path


LOGS_DIR = Path("logs")

FIELDNAMES = [
    "turn",
    "npc_name",
    "neuroticism",
    "player_text",
    "stimulus_category",
    "emotion",
    "emotion_valence",
    "intensity",
    "emotion_center_pleasure",
    "emotion_center_arousal",
    "emotion_center_dominance",
    "mood_pleasure",
    "mood_arousal",
    "mood_dominance",
    "mood_label",
    "action",
    "response",
]


def ensure_logs_dir() -> None:
    LOGS_DIR.mkdir(exist_ok=True)


def reset_log(filename: str) -> None:
    ensure_logs_dir()
    path = LOGS_DIR / filename
    if path.exists():
        path.unlink()


def append_turn_log(filename: str, row: dict) -> None:
    ensure_logs_dir()
    path = LOGS_DIR / filename
    file_exists = path.exists()

    with path.open("a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)