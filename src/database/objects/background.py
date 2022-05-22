from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.config import BACKGROUND_VERSION
from src.cruds.utils.funcs import create_srl, prefix_name
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin
from src.models.background import Background as BackgroundReqResp


class Background(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "backgrounds"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    thumbnail = Column(String(128))
    data = Column(String(128))
    image = Column(String(128))
    configuration = Column(String(128))
    engines = relationship("Engine", back_populates="background")
    levels = relationship("Level", back_populates="background")
    user = relationship("User", back_populates="backgrounds", uselist=False)

    def toItem(
        self, withEngines: bool = False, withLevels: bool = False
    ) -> BackgroundReqResp:
        return BackgroundReqResp(
            id=self.id,
            thumbnail=create_srl("BackgroundThumbnail", self.thumbnail),
            data=create_srl("BackgroundData", self.data),
            image=create_srl("BackgroundImage", self.image),
            configuration=create_srl("BackgroundImage", self.configuration),
            engines=[engine.toItem() for engine in self.engines] if withEngines else [],
            levels=[level.toItem() for level in self.levels] if withLevels else [],
            user=self.user.toItem(),
            name=prefix_name(self.name),
            version=BACKGROUND_VERSION,
            title=self.title,
            titleEn=self.titleEn,
            subtitle=self.subtitle,
            subtitleEn=self.subtitleEn,
            author=self.author,
            authorEn=self.authorEn,
            public=self.public,
            userId=self.userId,
            description=self.description,
            descriptionEn=self.descriptionEn,
            createdTime=self.createdTime,
            updatedTime=self.updatedTime,
        )
