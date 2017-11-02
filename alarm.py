from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship

from models.base import Base


class Alarm(Base):
    _tablename_ = 'alarm'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('User.id'))
    alarm = Column(DateTime)