from src.models.pad import PAD
from src.models.personality import Personality
from src.utils.clamp import clamp


def initialize_mood(personality: Personality) -> PAD:
    n = max(0.0, min(1.0, personality.neuroticism))

    return PAD(
        pleasure=clamp(-0.08 * n),
        arousal=clamp(0.08 + (0.12 * n)),
        dominance=clamp(-0.05 * n),
    )


def update_mood(current_mood: PAD, emotion_center: PAD, alpha: float = 0.35) -> PAD:
    return PAD(
        pleasure=clamp(
            ((1 - alpha) * current_mood.pleasure) + (alpha * emotion_center.pleasure)
        ),
        arousal=clamp(
            ((1 - alpha) * current_mood.arousal) + (alpha * emotion_center.arousal)
        ),
        dominance=clamp(
            ((1 - alpha) * current_mood.dominance) + (alpha * emotion_center.dominance)
        ),
    )


def mood_label(mood: PAD) -> str:
    if mood.pleasure >= 0.05:
        return "cooperative"

    if mood.pleasure <= -0.12 and mood.arousal >= 0.18:
        return "hostile"

    if mood.dominance <= -0.10:
        return "anxious"

    return "neutral"