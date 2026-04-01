from src.data.emotions import EMOTIONS
from src.data.scenarios import CATEGORY_TO_EMOTION
from src.models.emotion import Emotion
from src.models.stimulus import Stimulus


def emotion_from_stimulus(stimulus: Stimulus) -> Emotion:
    emotion_name = CATEGORY_TO_EMOTION.get(stimulus.category, "satisfaction")
    return EMOTIONS[emotion_name]