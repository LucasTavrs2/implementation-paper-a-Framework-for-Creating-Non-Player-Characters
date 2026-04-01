from src.models.emotion import Emotion
from src.models.pad import PAD
from src.models.personality import Personality
from src.utils.clamp import clamp


def compute_intensity(emotion: Emotion, personality: Personality) -> float:
    intensity = emotion.base_intensity
    neuroticism = max(0.0, min(1.0, personality.neuroticism))

    if emotion.valence == "negative":
        intensity *= 1.0 + (0.60 * neuroticism)
    else:
        intensity *= 1.0 - (0.15 * neuroticism)

    return max(0.0, min(1.0, intensity))


def apply_decay(current_center: PAD, decay_factor: float = 1.0) -> PAD:
    decay_factor = max(0.0, min(1.0, decay_factor))

    return PAD(
        pleasure=clamp(current_center.pleasure * decay_factor),
        arousal=clamp(current_center.arousal * decay_factor),
        dominance=clamp(current_center.dominance * decay_factor),
    )


def update_emotion_center(
    current_center: PAD,
    emotion: Emotion,
    intensity: float,
    decay_factor: float = 1.0,
) -> PAD:
    decayed_center = apply_decay(current_center, decay_factor)

    return PAD(
        pleasure=clamp(
            decayed_center.pleasure + (emotion.pad_delta.pleasure * intensity)
        ),
        arousal=clamp(
            decayed_center.arousal + (emotion.pad_delta.arousal * intensity)
        ),
        dominance=clamp(
            decayed_center.dominance + (emotion.pad_delta.dominance * intensity)
        ),
    )