from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.config import EFFECT_VERSION
from src.cruds.utils.funcs import create_srl
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin
from src.models import EffectReqResp


class Effect(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "effects"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    thumbnail = Column(String(128))
    data = Column(String(128))
    engines = relationship("Engine", back_populates="effect")
    levels = relationship("Level", back_populates="effect")
    user = relationship("User", back_populates="effects", uselist=False)

    def toItem(
        self, withEngines: bool = False, withLevels: bool = False
    ) -> EffectReqResp:
        return EffectReqResp(
            id=self.id,
            thumbnail=create_srl("EffectThumbnail", self.thumbnail),
            data=create_srl("EffectData", self.data),
            engines=[engine.toItem() for engine in self.engines] if withEngines else [],
            levels=[level.toItem() for level in self.levels] if withLevels else [],
            user=self.user.toItem(),
            name=self.name,
            version=EFFECT_VERSION,
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
