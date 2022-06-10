from typing import Callable, List

from src.cruds.extras.upload import ACCEPT_TYPES


class DummyFile:
    def __init__(self, data: bytes, content_type: str, filename: str) -> None:
        self.data = data
        self.content_type = content_type
        self.filename = filename

    async def read(self) -> bytes:
        return self.data


class DummyBackgroundTasks:
    def __init__(self) -> None:
        self.tasks: List[Callable] = []

    def add_task(self, func: Callable) -> None:
        self.tasks.append(func)


ACCEPT_MAP = {t.srl_name: t.content_type for t in ACCEPT_TYPES}
