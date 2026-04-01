from src.models.emotion import Emotion
from src.models.pad import PAD


EMOTIONS = {
    "pride": Emotion(
        name="pride",
        pad_delta=PAD(0.25, 0.10, 0.15),
        valence="positive",
        base_intensity=0.60,
    ),
    "satisfaction": Emotion(
        name="satisfaction",
        pad_delta=PAD(0.30, 0.05, 0.10),
        valence="positive",
        base_intensity=0.55,
    ),
    "resentment": Emotion(
        name="resentment",
        pad_delta=PAD(-0.25, 0.20, -0.05),
        valence="negative",
        base_intensity=0.65,
    ),
    "reproach": Emotion(
        name="reproach",
        pad_delta=PAD(-0.35, 0.30, 0.05),
        valence="negative",
        base_intensity=0.75,
    ),
}