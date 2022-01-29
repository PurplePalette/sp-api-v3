from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_mixin, declared_attr


@declarative_mixin
class SonolusDataMixin(object):  # type: ignore
    __tablename__ = "dummy"

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
    public = Column(Boolean(), default=False, server_default="0")
    isDeleted = Column(Boolean(), default=False, server_default="0")

    @declared_attr
    def userId(cls) -> Column:
        return Column(Integer, ForeignKey("users.id"))
