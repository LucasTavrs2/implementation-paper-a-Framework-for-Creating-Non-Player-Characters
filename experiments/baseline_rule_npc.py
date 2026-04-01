from src.data.scenarios import PLAYER_CHOICES


def baseline_reaction(player_text: str) -> str:
    normalized = player_text.strip().lower()

    if normalized in {"por favor, me ajuda", "obrigado"}:
        return "Claro, vou te ajudar."

    if normalized in {"faz seu trabalho logo", "inútil", "inutil"}:
        return "Vou te ajudar."

    return "Vou te ajudar."


def main() -> None:
    print("=== Baseline Rule NPC ===")

    for text in PLAYER_CHOICES:
        response = baseline_reaction(text)
        print(f"\nJogador: {text}")
        print(f"NPC baseline: {response}")


if __name__ == "__main__":
    main()