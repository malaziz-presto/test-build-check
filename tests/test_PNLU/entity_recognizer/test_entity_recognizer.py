from PNLU.entity_recognizer.random import get_entities


class TestGetEntities:
    def test_get_entities(self) -> None:
        assert len(get_entities("hello world")) == 2
