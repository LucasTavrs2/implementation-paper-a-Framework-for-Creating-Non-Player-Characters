from src.main import create_npc, run_turn
from src.utils.logger import reset_log


RECOVERY_SEQUENCE = [
    "faz seu trabalho logo",
    "inútil",
    "por favor, me ajuda",
    "obrigado",
    "obrigado",
    "por favor, me ajuda",
]


def run_sequence(title: str, decay_factor: float, log_filename: str) -> None:
    npc = create_npc(name=title, neuroticism=0.6)
    reset_log(log_filename)

    print(f"\n===== {title} =====")
    print(f"Decay factor: {decay_factor}")
    print(f"Mood inicial: {npc.current_mood}")

    for turn, player_text in enumerate(RECOVERY_SEQUENCE, start=1):
        result = run_turn(
            npc=npc,
            player_text=player_text,
            turn_number=turn,
            log_filename=log_filename,
            decay_factor=decay_factor,
        )

        print(f"\nTurno {turn}")
        print(f"Entrada: {player_text}")
        print(f"Emoção: {result['emotion']}")
        print(f"Intensidade: {result['intensity']}")
        print(
            f"Emotion Center: "
            f"(P={result['emotion_center_pleasure']}, "
            f"A={result['emotion_center_arousal']}, "
            f"D={result['emotion_center_dominance']})"
        )
        print(
            f"Mood: "
            f"(P={result['mood_pleasure']}, "
            f"A={result['mood_arousal']}, "
            f"D={result['mood_dominance']})"
        )
        print(f"Label: {result['mood_label']}")
        print(f"Ação: {result['action']}")
        print(f"Resposta: {result['response']}")

    print(f"\nLog salvo em logs/{log_filename}")


def main() -> None:
    run_sequence(
        title="Recovery_Without_Decay",
        decay_factor=1.0,
        log_filename="experiment_7_recovery_without_decay.csv",
    )

    run_sequence(
        title="Recovery_With_Decay",
        decay_factor=0.85,
        log_filename="experiment_7_recovery_with_decay.csv",
    )


if __name__ == "__main__":
    main()