from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class TimeMixin(object):  # type: ignore
    createdTime = Column(Integer)
    updatedTime = Column(Integer)
