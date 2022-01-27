from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin
from src.models.engine import Engine as EngineModel
from src.models.get_level_response import GetLevelResponse
from src.models.level import Level as LevelModel
from src.models.level_use_background import LevelUseBackground
from src.models.level_use_effect import LevelUseEffect
from src.models.level_use_particle import LevelUseParticle
from src.models.level_use_skin import LevelUseSkin
from src.models.sonolus_resource_locator import SonolusResourceLocator


class Announce(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "announces"
    __table_args__ = {"extend_existing": True}

    # FIXME: Remove this init and use better mypy config
    def __init__(
        self,
        name: str,
        title: str,
        title_en: str,
        artists: str,
        artists_en: str,
        author: str,
        author_en: str,
        description: str,
        description_en: str,
        public: bool,
        created_time: int,
        updated_time: int,
        cover_hash: str,
        bgm_hash: str,
        data_hash: str,
        user_id: int,
    ) -> None:
        self.name = name
        self.title = title
        self.title_en = title_en
        self.artists = artists
        self.artists_en = artists_en
        self.author = author
        self.author_en = author_en
        self.description = description
        self.description_en = description_en
        self.public = public
        self.created_time = created_time
        self.updated_time = updated_time
        self.cover_hash = cover_hash
        self.bgm_hash = bgm_hash
        self.data_hash = data_hash
        self.user_id = user_id
        super().__init__()

    def toLevelItem(self) -> LevelModel:
        return LevelModel(
            name=self.name,
            version=1,
            rating=1,
            engine=EngineModel(
                version=1,
                name="Info",
                title="Info",
                subtitle="Info",
                author="Info",
                createdTime=0,
                updatedTime=0,
                userId="announce",
                description="",
            ),
            useSkin=LevelUseSkin(useDefault=True),
            useBackground=LevelUseBackground(useDefault=True),
            useEffect=LevelUseEffect(useDefault=True),
            useParticle=LevelUseParticle(useDefault=True),
            title=self.title,
            artists=self.artists,
            author=self.author,
            cover=SonolusResourceLocator(
                type="LevelCover", hash="", url=self.cover_hash
            ),
            bgm=SonolusResourceLocator(type="LevelBgm", hash="", url=self.bgm_hash),
            data=SonolusResourceLocator(type="LevelData", hash="", url=self.data_hash),
            public=self.public,
            genre=[],
            userId=self.user_id,
            createdTime=1,
            updatedTime=1,
            description=self.description,
            length=1,
            bpm=1,
            notes=1,
            likes=0,
            mylists=0,
        )

    def toLevelResponse(self) -> GetLevelResponse:
        return GetLevelResponse(
            item=self.toLevelItem(),
            description=self.description,
            recommended=[],
        )

    cover_hash = Column(String(128), nullable=True)
    bgm_hash = Column(String(128), nullable=True)
    data_hash = Column(String(128), nullable=True)
    user = relationship("User", back_populates="announces", uselist=False)
