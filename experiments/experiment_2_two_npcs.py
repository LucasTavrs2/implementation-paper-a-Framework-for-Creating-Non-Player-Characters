from src.data.scenarios import NEGATIVE_SEQUENCE
from src.main import create_npc, run_turn
from src.utils.logger import reset_log


def run_for_npc(name: str, neuroticism: float, log_filename: str) -> None:
    npc = create_npc(name=name, neuroticism=neuroticism)
    reset_log(log_filename)

    print(f"\n===== {name} | neuroticism={neuroticism:.2f} =====")
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
        print(f"Resposta: {result['response']}")

    print(f"\nLog salvo em logs/{log_filename}")


def main() -> None:
    run_for_npc(
        name="NPC_High_Neuroticism",
        neuroticism=0.8,
        log_filename="experiment_2_high_neuroticism.csv",
    )

    run_for_npc(
        name="NPC_Low_Neuroticism",
        neuroticism=0.1,
        log_filename="experiment_2_low_neuroticism.csv",
    )


if __name__ == "__main__":
    main()