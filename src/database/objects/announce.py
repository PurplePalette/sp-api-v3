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
        titleEn: str,
        artists: str,
        artistsEn: str,
        author: str,
        authorEn: str,
        description: str,
        descriptionEn: str,
        public: bool,
        createdTime: int,
        updatedTime: int,
        coverHash: str,
        bgmHash: str,
        dataHash: str,
        userId: int,
    ) -> None:
        self.name = name
        self.title = title
        self.titleEn = titleEn
        self.artists = artists
        self.artistsEn = artistsEn
        self.author = author
        self.authorEn = authorEn
        self.description = description
        self.descriptionEn = descriptionEn
        self.public = public
        self.createdTime = createdTime
        self.updatedTime = updatedTime
        self.coverHash = coverHash
        self.bgmHash = bgmHash
        self.dataHash = dataHash
        self.userId = userId
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
                type="LevelCover", hash="", url=self.coverHash
            ),
            bgm=SonolusResourceLocator(type="LevelBgm", hash="", url=self.bgmHash),
            data=SonolusResourceLocator(type="LevelData", hash="", url=self.dataHash),
            public=self.public,
            genre=[],
            userId=self.userId,
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

    coverHash = Column(String(128), nullable=True)
    bgmHash = Column(String(128), nullable=True)
    dataHash = Column(String(128), nullable=True)
    user = relationship("User", back_populates="announces", uselist=False)
