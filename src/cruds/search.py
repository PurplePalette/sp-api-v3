from abc import ABCMeta, abstractmethod
from typing import Any, List, Optional, TypeVar

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    false,
    func,
    select,
    true,
)
from sqlalchemy.orm import joinedload, relationship
from src.models.search_query import (
    SearchGenre,
    SearchLength,
    SearchOrder,
    SearchQueries,
    SearchSort,
    SearchStatus,
)


class Searchable(metaclass=ABCMeta):
    """名前を持つオブジェクトを表す基底クラス"""

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    title = Column(String(128))
    titleEn = Column(String(128))
    subtitle = Column(String(128))
    subtitleEn = Column(String(128))
    author = Column(String(128))
    authorEn = Column(String(128))
    description = Column(String(512))
    descriptionEn = Column(String(512))
    public = Column(Boolean(), default=False, server_default="0")
    isDeleted = Column(Boolean(), default=False, server_default="0")
    userId = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", uselist=False)
    createdTime = Column(Integer)
    updatedTime = Column(Integer)
    # 以降レベルモデルにのみ存在
    rating: Optional[Column[Integer]] = None
    genre: Optional[Column[Integer]] = None
    length: Optional[Column[Integer]] = None
    bpm: Optional[Column[Integer]] = None
    notes: Optional[Column[Integer]] = None

    @abstractmethod
    def num_favorites(cls) -> int:
        raise NotImplementedError()

    @abstractmethod
    def num_likes(cls) -> int:
        raise NotImplementedError()


T = TypeVar("T", bound=Searchable)


def buildFilter(
    obj: T,
    query: SearchQueries,
) -> List[Any]:
    """フィルタ方法を生成する"""
    filterFields = [
        obj.isDeleted == false(),
    ]
    if query.keywords:
        filterFields += [
            obj.name.contains(query.keywords),
            obj.title.contains(query.keywords),
            obj.titleEn.contains(query.keywords),
            obj.author.contains(query.author),
            obj.authorEn.contains(query.keywords),
        ]
    # Levelsエンドポイント用フィルタ
    # ジャンル
    if query.genre and obj.genre:
        if query.genre != SearchGenre.ANY:
            filterFields.append(obj.genre == query.genre)
    # 最低難易度
    if query.rating_min and obj.rating:
        filterFields.append(obj.rating >= query.rating_min)
    # 最高難易度
    if query.rating_max and obj.rating:
        filterFields.append(obj.rating <= query.rating_max)
    # 長さ
    if query.length and obj.length:
        if query.length != SearchLength.ANY:
            if query.length != SearchLength.VERY_SHORT:
                # 1分以下
                filterFields.append(obj.length < 60)
            if query.length != SearchLength.SHORT:
                # 1分以上 3分以下
                filterFields.append(obj.length > 60)
                filterFields.append(obj.length < 180)
            elif query.length != SearchLength.LONG:
                # 3分以上 5分以下
                filterFields.append(obj.length > 180)
                filterFields.append(obj.length < 300)
            elif query.length != SearchLength.VERY_LONG:
                # 5分以上
                filterFields.append(obj.length > 300)
    # テスト中が指定されていれば
    if query.status == SearchStatus.TESTING and query.user:
        filterFields.append(obj.public == false())
        filterFields.append(obj.userId == query.user.id)
    else:
        filterFields.append(obj.public == true())
    # 一応早期リターン
    if query.status == SearchStatus.ANY:
        return filterFields
    # Accountsエンドポイント用フィルタ
    if query.user:
        if query.status == SearchStatus.LIKED:
            filterFields.append(obj.id.in_(query.user.ids_likes()))
        elif query.status == SearchStatus.MYLISTED:
            filterFields.append(obj.id.in_(query.user.ids_favorites()))
        elif query.status == SearchStatus.PLAYED:
            filterFields.append(obj.id.in_(query.user.ids_played()))
        elif query.status == SearchStatus.UNPLAYED:
            filterFields.append(obj.id.not_in(query.user.ids_played()))
    return filterFields


def buildSort(obj: T, query: SearchQueries) -> Column:
    """ソート方法を生成する"""
    sortMethod = obj.updatedTime
    if query.sort == SearchSort.CREATED_TIME:
        sortMethod = obj.createdTime
    elif query.sort == SearchSort.UPDATED_TIME:
        sortMethod = obj.createdTime
    # Levelsエンドポイント用
    if query.genre:
        if query.sort == SearchSort.LIKES:
            sortMethod = obj.num_likes
        elif query.sort == SearchSort.MYLISTS:
            sortMethod = obj.num_favorites
        elif query.sort == SearchSort.RATING:
            sortMethod = obj.rating
        elif query.sort == SearchSort.BPM:
            sortMethod = obj.bpm
        elif query.sort == SearchSort.NOTES:
            sortMethod = obj.notes
    # ソート方向を指定
    if query.order == SearchOrder.ASC:
        sortMethod = sortMethod.asc()
    else:
        sortMethod = sortMethod.desc()
    return sortMethod


def buildDatabaseQuery(obj: T, query: SearchQueries, joinUser: bool = False) -> select:
    """"与えられたパラメータからクエリを組み立てる(しんどい)"""
    filter: list = buildFilter(obj, query)
    sorter: int = 0
    if query.random == 0:
        sorter = buildSort(obj, query)
    else:
        sorter = func.random()
    stmt = select(obj).filter(*filter).order_by(sorter)
    if joinUser:
        stmt = stmt.options(joinedload(obj.user))
    return stmt
