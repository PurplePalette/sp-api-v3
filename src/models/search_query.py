from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.database.objects.user import User

"""
独自定義のクエリEnum
"""


class SearchStatus(str, Enum):
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

    PLAYED = "played"
    UNPLAYED = "unplayed"
    LIKED = "liked"
    MYLISTED = "mylisted"
    TESTING = "testing"
    ANY = "any"


class SearchGenre(str, Enum):
    """
    SearchQueryEnum

    VOCALOID
    JPOP
    ANIME
    GENERAL
    ANY
    """

    VOCALOID = "vocaloid"
    JPOP = "jpop"
    ANIME = "anime"
    GENERAL = "general"
    ANY = "any"


class SearchSort(str, Enum):
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

    UPDATED_TIME = "updated_time"
    CREATED_TIME = "created_time"
    LIKES = "likes"
    MYLISTS = "mylists"
    RATING = "rating"
    NOTES = "notes"
    BPM = "bpm"


class SearchOrder(str, Enum):
    """
    SearchQueryEnum

    ASC
    DESC
    """

    ASC = "asc"
    DESC = "desc"


class SearchLength(str, Enum):
    """
    SearchQueryEnum

    SHORT
    LONG
    VERY_SHORT
    VERY_LONG
    ANY
    """

    SHORT = "short"
    LONG = "long"
    VERY_SHORT = "very_short"
    VERY_LONG = "very_long"
    ANY = "any"


@dataclass
class SearchQueries:
    keywords: str
    author: str
    sort: SearchSort
    order: SearchOrder
    status: SearchStatus
    random: int
    rating_min: Optional[int]
    rating_max: Optional[int]
    genre: Optional[SearchGenre]
    length: Optional[SearchLength]
    user: Optional[User]
