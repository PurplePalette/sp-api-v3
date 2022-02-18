from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.db import Base
from src.database.mixins import TimeMixin
from src.models.engine import Engine as EngineModel
from src.models.get_level_response import GetLevelResponse
from src.models.level import Level as LevelModel
from src.models.level_use_background import LevelUseBackground
from src.models.level_use_effect import LevelUseEffect
from src.models.level_use_particle import LevelUseParticle
from src.models.level_use_skin import LevelUseSkin
from src.models.sonolus_resource_locator import SonolusResourceLocator


class Announce(TimeMixin, Base):  # type: ignore
    __tablename__ = "announces"
    __table_args__ = {"extend_existing": True}

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
    rating = Column(Integer)
    public = Column(Boolean(), default=False, server_default="0")
    cover = Column(String(128), nullable=False)
    bgm = Column(String(128), nullable=False)
    preview = Column(String(128), nullable=False)
    userId = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="announces", uselist=False)

    def toLevelItem(self) -> LevelModel:
        return LevelModel(
            name=self.name,
            version=1,
            rating=self.rating,
            engine=EngineModel(
                version=1,
                name="Info",
                title="Info",
                titleEn="Info",
                subtitle="Info",
                subtitleEn="Info",
                author="Info",
                authorEn="Info",
                createdTime=0,
                updatedTime=0,
                userId="announce",
                description="",
                descriptionEn="",
            ),
            useSkin=LevelUseSkin(useDefault=True),
            useBackground=LevelUseBackground(useDefault=True),
            useEffect=LevelUseEffect(useDefault=True),
            useParticle=LevelUseParticle(useDefault=True),
            title=self.title,
            titleEn=self.titleEn,
            artists=self.subtitle,
            artistsEn=self.subtitleEn,
            author=self.author,
            authorEn=self.authorEn,
            cover=SonolusResourceLocator(type="LevelCover", hash="", url=self.cover),
            bgm=SonolusResourceLocator(type="LevelBgm", hash="", url=self.bgm),
            preview=SonolusResourceLocator(type="LevelPreview", hash="", url=self.bgm),
            data=SonolusResourceLocator(type="LevelData", hash="", url=""),
            public=self.public,
            genre=[],
            userId=self.userId,
            createdTime=1,
            updatedTime=1,
            description=self.description,
            descriptionEn=self.descriptionEn,
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
