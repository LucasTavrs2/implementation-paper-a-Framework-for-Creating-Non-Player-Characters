from dataclasses import dataclass


@dataclass(frozen=True)
class Stimulus:
    text: str
    category: str