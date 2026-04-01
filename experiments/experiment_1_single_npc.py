from src.data.scenarios import NEGATIVE_SEQUENCE, POSITIVE_SEQUENCE
from src.main import create_npc, run_turn
from src.utils.logger import reset_log


def run_sequence(title: str, sequence: list, log_filename: str) -> None:
    npc = create_npc(name="Companion", neuroticism=0.6)
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
        print(f"Intensidade: {result['intensity']}")
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
        title="Sequência Positiva",
        sequence=POSITIVE_SEQUENCE,
        log_filename="experiment_1_positive.csv",
    )

    run_sequence(
        title="Sequência Negativa",
        sequence=NEGATIVE_SEQUENCE,
        log_filename="experiment_1_negative.csv",
    )


if __name__ == "__main__":
    main()