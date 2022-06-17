from src.config import PREFIX
from src.cruds.utils.funcs import remove_prefix


def test_remove_prefix() -> None:
    assert remove_prefix(PREFIX + "announce_name_example") == "announce_name_example"


def test_remove_prefix_without_prefix() -> None:
    assert remove_prefix("announce_name_example") == "announce_name_example"
