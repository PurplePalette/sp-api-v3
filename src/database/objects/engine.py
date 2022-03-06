from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config import ENGINE_VERSION
from src.cruds.utils.funcs import create_srl
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin
from src.models import EngineReqResp


class Engine(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "engines"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    thumbnail = Column(String(128))
    data = Column(String(128))
    configuration = Column(String(128))
    backgroundId = Column(Integer, ForeignKey("backgrounds.id"))
    effectId = Column(Integer, ForeignKey("effects.id"))
    particleId = Column(Integer, ForeignKey("particles.id"))
    skinId = Column(Integer, ForeignKey("skins.id"))
    background = relationship("Background", back_populates="engines", uselist=False)
    effect = relationship("Effect", back_populates="engines", uselist=False)
    particle = relationship("Particle", back_populates="engines", uselist=False)
    skin = relationship("Skin", back_populates="engines", uselist=False)
    levels = relationship("Level", back_populates="engine")
    user = relationship("User", back_populates="engines", uselist=False)

    def toItem(self, withLevels: bool = False) -> EngineReqResp:
        return EngineReqResp(
            id=self.id,
            thumbnail=create_srl("EngineThumbnail", self.thumbnail),
            data=create_srl("EngineData", self.data),
            configuration=create_srl("EngineConfiguration", self.configuration),
            background=self.background.toItem(),
            effect=self.effect.toItem(),
            particle=self.particle.toItem(),
            skin=self.skin.toItem(),
            levels=[level.toItem() for level in self.levels] if withLevels else [],
            user=self.user.toItem(),
            name=self.name,
            version=ENGINE_VERSION,
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
