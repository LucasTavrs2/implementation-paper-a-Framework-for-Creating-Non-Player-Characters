from dataclasses import dataclass, asdict


@dataclass
class PAD:
    pleasure: float = 0.0
    arousal: float = 0.0
    dominance: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        return (
            f"(P={self.pleasure:.2f}, "
            f"A={self.arousal:.2f}, "
            f"D={self.dominance:.2f})"
        )