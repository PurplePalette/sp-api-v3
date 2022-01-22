from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class TimeMixin(object):
    created_time = Column(DateTime)
    updated_time = Column(DateTime)
