from dataclasses import dataclass
import math
from typing import TypeVar, Generic, Sequence

from fastapi_pagination import Page


T = TypeVar("T")


@dataclass
class SonolusPage(Generic[T]):
    pageCount: int
    total: int
    items: Sequence[T]


def toSonolusPage(page: Page) -> SonolusPage:
    return SonolusPage(
        pageCount=math.ceil(page.total / page.size), total=page.total, items=page.items
    )
