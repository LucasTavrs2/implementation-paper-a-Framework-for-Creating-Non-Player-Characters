from src.data.scenarios import PLAYER_CHOICES
from src.main import create_npc, run_turn
from src.utils.logger import reset_log


def main() -> None:
    print("=== Experiment 3: Emotion Response Grid ===")

    log_filename = "experiment_3_emotion_response_grid.csv"
    reset_log(log_filename)

    neuroticism_values = [0.1, 0.5, 0.8]

    for neuroticism in neuroticism_values:
        print(f"\n===== Neuroticism = {neuroticism:.2f} =====")

        for i, player_text in enumerate(PLAYER_CHOICES, start=1):
            npc = create_npc(name=f"NPC_N{neuroticism:.2f}", neuroticism=neuroticism)

            result = run_turn(
                npc=npc,
                player_text=player_text,
                turn_number=i,
                log_filename=log_filename,
            )

            print(f"\nEntrada: {player_text}")
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