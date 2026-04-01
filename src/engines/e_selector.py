from src.models.pad import PAD


def select_action(mood: PAD) -> str:
    if mood.pleasure >= 0.05:
        return "ajudar_com_boa_vontade"

    if mood.pleasure <= -0.12 and mood.arousal >= 0.18:
        return "ajudar_de_forma_hostil"

    if mood.dominance <= -0.10:
        return "hesitar"

    return "ajudar_com_boa_vontade"