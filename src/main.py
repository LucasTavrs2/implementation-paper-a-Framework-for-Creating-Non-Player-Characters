from src.data.reactions import REACTIONS
from src.data.scenarios import PLAYER_CHOICES
from src.engines.appraisal_engine import appraise
from src.engines.e_selector import select_action
from src.engines.emotion_adder import emotion_from_stimulus
from src.engines.emotion_center import compute_intensity, update_emotion_center
from src.engines.mood_engine import initialize_mood, mood_label, update_mood
from src.models.npc_state import NPCState
from src.models.pad import PAD
from src.models.personality import Personality
from src.utils.logger import append_turn_log, reset_log


def create_npc(name: str, neuroticism: float) -> NPCState:
    personality = Personality(neuroticism=max(0.0, min(1.0, neuroticism)))
    initial_mood = initialize_mood(personality)

    return NPCState(
        name=name,
        personality=personality,
        current_mood=initial_mood,
        emotion_center=PAD(),
    )


def run_turn(
    npc: NPCState,
    player_text: str,
    turn_number: int,
    log_filename: str = None,
    decay_factor: float = 1.0,
) -> dict:
    stimulus = appraise(player_text)
    emotion = emotion_from_stimulus(stimulus)
    intensity = compute_intensity(emotion, npc.personality)

    npc.emotion_center = update_emotion_center(
        current_center=npc.emotion_center,
        emotion=emotion,
        intensity=intensity,
        decay_factor=decay_factor,
    )

    npc.current_mood = update_mood(
        current_mood=npc.current_mood,
        emotion_center=npc.emotion_center,
    )

    action = select_action(npc.current_mood)
    response = REACTIONS[action]

    npc.last_emotion = emotion.name
    npc.last_action = action

    row = {
        "turn": turn_number,
        "npc_name": npc.name,
        "neuroticism": round(npc.personality.neuroticism, 4),
        "player_text": player_text,
        "stimulus_category": stimulus.category,
        "emotion": emotion.name,
        "emotion_valence": emotion.valence,
        "intensity": round(intensity, 4),
        "emotion_center_pleasure": round(npc.emotion_center.pleasure, 4),
        "emotion_center_arousal": round(npc.emotion_center.arousal, 4),
        "emotion_center_dominance": round(npc.emotion_center.dominance, 4),
        "mood_pleasure": round(npc.current_mood.pleasure, 4),
        "mood_arousal": round(npc.current_mood.arousal, 4),
        "mood_dominance": round(npc.current_mood.dominance, 4),
        "mood_label": mood_label(npc.current_mood),
        "action": action,
        "response": response,
    }

    if log_filename:
        append_turn_log(log_filename, row)

    return row


def print_choices() -> None:
    print("\nEscolha uma fala para o jogador:")
    for index, option in enumerate(PLAYER_CHOICES, start=1):
        print(f"{index}. {option}")
    print("0. sair")


def main() -> None:
    print("=== NPC Afetivo - MVP Textual ===")

    neuroticism_raw = input(
        "Defina o neuroticism do NPC (0.0 a 1.0) [padrão 0.7]: "
    ).strip()

    if neuroticism_raw == "":
        neuroticism = 0.7
    else:
        neuroticism = float(neuroticism_raw)

    npc = create_npc(name="Companion", neuroticism=neuroticism)
    log_filename = "interactive_session.csv"
    reset_log(log_filename)

    print(f"\nNPC criado: {npc.name}")
    print(f"Neuroticism: {npc.personality.neuroticism:.2f}")
    print(f"Mood inicial: {npc.current_mood}")

    turn = 1

    while True:
        print_choices()
        choice = input("\nDigite o número da opção ou uma frase: ").strip()

        if choice in {"0", "sair", "exit"}:
            print("\nEncerrando simulação.")
            break

        if choice.isdigit() and 1 <= int(choice) <= len(PLAYER_CHOICES):
            player_text = PLAYER_CHOICES[int(choice) - 1]
        else:
            player_text = choice

        result = run_turn(
            npc=npc,
            player_text=player_text,
            turn_number=turn,
            log_filename=log_filename,
        )

        print("\n--- Resultado do turno ---")
        print(f"Jogador: {player_text}")
        print(f"Emoção: {result['emotion']} ({result['emotion_valence']})")
        print(f"Intensidade: {result['intensity']}")
        print(
            "Emotion Center: "
            f"(P={result['emotion_center_pleasure']}, "
            f"A={result['emotion_center_arousal']}, "
            f"D={result['emotion_center_dominance']})"
        )
        print(
            "Mood atual: "
            f"(P={result['mood_pleasure']}, "
            f"A={result['mood_arousal']}, "
            f"D={result['mood_dominance']})"
        )
        print(f"Label do mood: {result['mood_label']}")
        print(f"Ação: {result['action']}")
        print(f"NPC: {result['response']}")

        turn += 1

    print(f"\nLogs salvos em: logs/{log_filename}")


if __name__ == "__main__":
    main()