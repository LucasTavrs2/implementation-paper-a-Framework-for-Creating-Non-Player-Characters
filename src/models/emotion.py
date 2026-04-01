from dataclasses import dataclass
from src.models.pad import PAD


@dataclass(frozen=True)
class Emotion:
    name: str
    pad_delta: PAD
    valence: str  # "positive" ou "negative"
    base_intensity: float