from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_mixin, declared_attr


@declarative_mixin
class SonolusDataMixin(object):  # type: ignore
    __tablename__ = "dummy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    title = Column(String(128))
    title_en = Column(String(128))
    artists = Column(String(128))
    artists_en = Column(String(128))
    author = Column(String(128))
    author_en = Column(String(128))
    description = Column(String(512))
    description_en = Column(String(512))
    public = Column(Boolean(), default=False, server_default="0")

    @declared_attr
    def user_id(cls) -> Column:
        return Column(Integer, ForeignKey("users.id"))
