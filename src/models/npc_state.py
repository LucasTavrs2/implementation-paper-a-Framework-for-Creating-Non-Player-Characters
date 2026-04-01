from dataclasses import dataclass, field
from typing import Optional

from src.models.pad import PAD
from src.models.personality import Personality


@dataclass
class NPCState:
    name: str
    personality: Personality
    current_mood: PAD = field(default_factory=PAD)
    emotion_center: PAD = field(default_factory=PAD)
    last_emotion: Optional[str] = None
    last_action: Optional[str] = None