from PNLU.entity_recognizer.types.entity import Entity


def get_entities(utterance: str) -> list[Entity]:
    return [Entity(token=token) for token in utterance.split()]
