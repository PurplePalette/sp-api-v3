from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, func, select
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from src.config import LEVEL_VERSION
from src.cruds.utils.funcs import create_srl, prefix_name
from src.database.db import Base
from src.database.mixins import SonolusDataMixin, TimeMixin
from src.database.objects.favorite import Favorite
from src.database.objects.like import Like
from src.database.objects.pickup import Pickup  # noqa: F401
from src.models.level import Level as LevelReqResp
from src.models.level_use_background import LevelUseBackground
from src.models.level_use_effect import LevelUseEffect
from src.models.level_use_particle import LevelUseParticle
from src.models.level_use_skin import LevelUseSkin


class Level(SonolusDataMixin, TimeMixin, Base):  # type: ignore
    __tablename__ = "levels"
    __table_args__ = {"extend_existing": True}

    class Config:
        orm_mode = True

    rating = Column(Integer)
    bpm = Column(Integer)
    notes = Column(Integer)
    length = Column(Integer)
    cover = Column(String(128))
    bgm = Column(String(128))
    data = Column(String(128))
    sus = Column(String(128))
    engineId = Column(Integer, ForeignKey("engines.id"))
    backgroundId = Column(Integer, ForeignKey("backgrounds.id"))
    effectId = Column(Integer, ForeignKey("effects.id"))
    particleId = Column(Integer, ForeignKey("particles.id"))
    skinId = Column(Integer, ForeignKey("skins.id"))
    genreId = Column(Integer, ForeignKey("genres.id"))
    background = relationship("Background", back_populates="levels", uselist=False)
    engine = relationship("Engine", back_populates="levels", uselist=False)
    effect = relationship("Effect", back_populates="levels", uselist=False)
    particle = relationship("Particle", back_populates="levels", uselist=False)
    skin = relationship("Skin", back_populates="levels", uselist=False)
    genre = relationship("Genre", back_populates="levels")
    likes = relationship("Like", back_populates="level")
    favorites = relationship("Favorite", back_populates="level")
    votes = relationship("Vote", back_populates="level")
    pickup = relationship("Pickup", back_populates="level", uselist=False)
    user = relationship("User", back_populates="levels", uselist=False)
    publicSus = Column(Boolean(), default=False, server_default="0")

    def toItem(self) -> LevelReqResp:
        return LevelReqResp(
            name=prefix_name(self.name),
            version=LEVEL_VERSION,
            rating=self.rating,
            engine=self.engine.toItem(),
            useSkin=LevelUseSkin(
                useDefault=not bool(self.skin),
                item=self.skin.toItem() if self.skin else None,
            ),
            useBackground=LevelUseBackground(
                useDefault=not bool(self.background),
                item=self.background.toItem() if self.background else None,
            ),
            useEffect=LevelUseEffect(
                useDefault=not bool(self.effect),
                item=self.effect.toItem() if self.effect else None,
            ),
            useParticle=LevelUseParticle(
                useDefault=not bool(self.particle),
                item=self.particle.toItem() if self.particle else None,
            ),
            title=self.title,
            titleEn=self.titleEn,
            artists=self.subtitle,
            artistsEn=self.subtitleEn,
            author=self.author,
            authorEn=self.authorEn,
            cover=create_srl("LevelCover", self.cover),
            bgm=create_srl("LevelBgm", self.bgm),
            preview=create_srl("LevelPreview", self.bgm),
            data=create_srl("LevelData", self.data),
            public=self.public,
            createdTime=self.createdTime,
            updatedTime=self.updatedTime,
            description=self.description,
            descriptionEn=self.descriptionEn,
            length=self.length,
            bpm=self.bpm,
            notes=self.notes,
            genre=self.genre.name,
            userId=self.userId,
            likes=self.num_likes,
            mylists=self.num_favorites,
        )

    @hybrid_property
    def num_favorites(self) -> int:
        return len(self.favorites)

    @num_favorites.expression
    def _num_favorites_expression(cls) -> select:
        return select([func.count(Favorite.id)]).where(Favorite.levelId == cls.id)

    @hybrid_property
    def num_likes(self) -> int:
        return len(self.likes)

    @num_likes.expression
    def _num_likes_expression(cls) -> select:
        return select([func.count(Like.id)]).where(Like.levelId == cls.id)
