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


def main() -> None:
    print("=== Experiment 6: Recovery Curve ===")

    log_filename = "experiment_6_recovery_curve.csv"
    reset_log(log_filename)

    npc = create_npc(name="RecoveryNPC", neuroticism=0.6)

    print(f"\nMood inicial: {npc.current_mood}")

    for turn, player_text in enumerate(RECOVERY_SEQUENCE, start=1):
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


if __name__ == "__main__":
    main()