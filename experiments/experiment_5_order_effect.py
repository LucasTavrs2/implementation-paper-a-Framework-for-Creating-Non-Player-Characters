from src.main import create_npc, run_turn
from src.utils.logger import reset_log


SEQUENCE_A = [
    "por favor, me ajuda",
    "obrigado",
    "faz seu trabalho logo",
    "inútil",
]

SEQUENCE_B = [
    "faz seu trabalho logo",
    "inútil",
    "por favor, me ajuda",
    "obrigado",
]


def run_sequence(title: str, sequence: list[str], log_filename: str) -> None:
    npc = create_npc(name=title, neuroticism=0.5)
    reset_log(log_filename)

    print(f"\n===== {title} =====")
    print(f"Mood inicial: {npc.current_mood}")

    for turn, player_text in enumerate(sequence, start=1):
        result = run_turn(
            npc=npc,
            player_text=player_text,
            turn_number=turn,
            log_filename=log_filename,
        )

        print(f"\nTurno {turn}")
        print(f"Entrada: {player_text}")
        print(f"Emoção: {result['emotion']}")
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
        title="Positive_Then_Negative",
        sequence=SEQUENCE_A,
        log_filename="experiment_5_positive_then_negative.csv",
    )

    run_sequence(
        title="Negative_Then_Positive",
        sequence=SEQUENCE_B,
        log_filename="experiment_5_negative_then_positive.csv",
    )


if __name__ == "__main__":
    main()