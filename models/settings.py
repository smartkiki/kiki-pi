from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from models.base import Base


class Settings(Base):
    __tablename__ = 'setting'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('user.id'))
    calendar = Column(Boolean)
    weather = Column(Boolean)
    alarm = Column(Boolean)
    spotify = Column(Boolean)

    def __init__(self, parent_id):
        self.calendar = False
        self.weather = False
        self.alarm = False
        self.spotify = False
        self.parent_id = parent_id
