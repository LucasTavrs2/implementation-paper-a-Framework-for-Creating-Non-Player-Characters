from src.data.scenarios import NEGATIVE_SEQUENCE
from src.main import create_npc, run_turn
from src.utils.logger import reset_log


def main() -> None:
    print("=== Experiment 4: Neuroticism Sweep ===")

    log_filename = "experiment_4_neuroticism_sweep.csv"
    reset_log(log_filename)

    neuroticism_values = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

    for neuroticism in neuroticism_values:
        npc = create_npc(name=f"NPC_N{neuroticism:.2f}", neuroticism=neuroticism)

        print(f"\n===== Neuroticism = {neuroticism:.2f} =====")
        print(f"Mood inicial: {npc.current_mood}")

        for turn, player_text in enumerate(NEGATIVE_SEQUENCE, start=1):
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

    print(f"\nLog salvo em logs/{log_filename}")


if __name__ == "__main__":
    main()