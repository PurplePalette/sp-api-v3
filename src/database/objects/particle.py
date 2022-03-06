from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.config import PARTICLE_VERSION
from src.cruds.utils.funcs import create_srl
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin
from src.models import ParticleReqResp


class Particle(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "particles"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    thumbnail = Column(String(128))
    data = Column(String(128))
    texture = Column(String(128))
    engines = relationship("Engine", back_populates="particle")
    levels = relationship("Level", back_populates="particle")
    user = relationship("User", back_populates="particles", uselist=False)

    def toItem(
        self, withEngines: bool = False, withLevels: bool = False
    ) -> ParticleReqResp:
        return ParticleReqResp(
            id=self.id,
            thumbnail=create_srl("ParticleThumbnail", self.thumbnail),
            data=create_srl("ParticleData", self.data),
            texture=create_srl("ParticleTexture", self.texture),
            engines=[engine.toItem() for engine in self.engines] if withEngines else [],
            levels=[level.toItem() for level in self.levels] if withLevels else [],
            user=self.user.toItem(),
            name=self.name,
            version=PARTICLE_VERSION,
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
