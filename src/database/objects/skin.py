from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.config import SKIN_VERSION
from src.cruds.utils.funcs import create_srl, prefix_name
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin
from src.models import SkinReqResp


class Skin(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "skins"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    thumbnail = Column(String(128))
    data = Column(String(128))
    texture = Column(String(128))
    engines = relationship("Engine", back_populates="skin")
    levels = relationship("Level", back_populates="skin")
    user = relationship("User", back_populates="skins", uselist=False)

    def toItem(
        self, withEngines: bool = False, withLevels: bool = False
    ) -> SkinReqResp:
        return SkinReqResp(
            id=self.id,
            thumbnail=create_srl("SkinThumbnail", self.thumbnail),
            data=create_srl("SkinData", self.data),
            texture=create_srl("SkinTexture", self.texture),
            engines=[engine.toItem() for engine in self.engines] if withEngines else [],
            levels=[level.toItem() for level in self.levels] if withLevels else [],
            user=self.user.toItem(),
            name=prefix_name(self.name),
            version=SKIN_VERSION,
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
