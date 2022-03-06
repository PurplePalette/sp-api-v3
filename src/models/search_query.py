from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.database.objects.user import User

"""
独自定義のクエリEnum
"""


class SearchStatus(int, Enum):
    """
    SearchQueryEnum

    UPDATED_TIME: The time when the object was updated.
    CREATED_TIME: The time when the object was created.
    LIKES: The count of object's likes.
    MYLISTS: The count of object's favorites.
    RATING: The difficulty of levels.
    NOTES: The notes of levels.
    BPM: The BPM of levels.
    """

    ANY = 0
    TESTING = 1
    PLAYED = 2
    UNPLAYED = 3
    LIKED = 4
    MYLISTED = 5


class SearchGenre(int, Enum):
    """
    SearchQueryEnum

    ANY
    GENERAL
    JPOP
    ANIME
    VOCALOID
    ORIGINAL
    INSTRUMENTAL
    """

    ANY = 0
    GENERAL = 1
    JPOP = 2
    ANIME = 3
    VOCALOID = 4
    ORIGINAL = 5
    INSTRUMENTAL = 6


class SearchSort(int, Enum):
    """
    SearchQueryEnum

    UPDATED_TIME: The time when the object was updated.
    CREATED_TIME: The time when the object was created.
    LIKES: The count of object's likes.
    MYLISTS: The count of object's favorites.
    RATING: The difficulty of levels.
    NOTES: The notes of levels.
    BPM: The BPM of levels.
    """

    UPDATED_TIME = 0
    CREATED_TIME = 1
    BPM = 2
    LIKES = 3
    MYLISTS = 4
    NOTES = 5
    RATING = 6


class SearchOrder(int, Enum):
    """
    SearchQueryEnum

    ASC
    DESC
    """

    DESC = 0
    ASC = 1


class SearchLength(int, Enum):
    """
    SearchQueryEnum

    SHORT
    LONG
    VERY_SHORT
    VERY_LONG
    ANY
    """

    ANY = 0
    SHORT = 1
    LONG = 2
    VERY_SHORT = 3
    VERY_LONG = 4


@dataclass
class SearchQueries:
    localization: str
    keywords: str
    author: str
    sort: SearchSort
    order: SearchOrder
    status: SearchStatus
    random: int
    rating_min: Optional[int] = None
    rating_max: Optional[int] = None
    genre: Optional[SearchGenre] = None
    length: Optional[SearchLength] = None
    user: Optional[User] = None
