from src.config import LEVEL_VERSION
from src.cruds.utils.funcs import create_srl
from src.models.engine import Engine as EngineModel
from src.models.level import Level as LevelModel
from src.models.level_use_background import LevelUseBackground
from src.models.level_use_effect import LevelUseEffect
from src.models.level_use_particle import LevelUseParticle
from src.models.level_use_skin import LevelUseSkin
from src.models.sonolus_resource_locator import SonolusResourceLocator


def create_tile(
    name: str,
    title: str,
    titleEn: str,
    subtitle: str,
    subtitleEn: str,
    author: str,
    authorEn: str,
    description: str,
    descriptionEn: str,
    rating: int,
    cover: str,
    bgm: str,
    localization: str,
) -> LevelModel:
    return LevelModel(
        name=name,
        version=LEVEL_VERSION,
        rating=rating,
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
        title=title if localization == "ja" else titleEn,
        titleEn="dummy",
        artists=subtitle if localization == "ja" else subtitleEn,
        artistsEn="dummy",
        author=author if localization == "ja" else authorEn,
        authorEn="dummy",
        cover=create_srl("LevelCover", cover),
        bgm=create_srl("LevelBgm", bgm),
        preview=create_srl("LevelPreview", bgm),
        data=SonolusResourceLocator(type="LevelData", hash="", url=""),
        public=True,
        genre="general",
        userId="server",
        createdTime=1,
        updatedTime=1,
        description=description,
        descriptionEn=descriptionEn,
        length=1,
        bpm=1,
        notes=1,
        likes=0,
        mylists=0,
    )
