import enum

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Enum
from sqlalchemy import ForeignKey

from models.base import Base


class HardwareType(enum.Enum):
    camera = 0
    microphone = 1
    speaker = 2


class Hardware(Base):
    __tablename__ = 'hardware'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('settings.id'))
    type = Column(Enum(HardwareType))
