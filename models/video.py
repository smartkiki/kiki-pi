from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from models.base import Base


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('user.id'))
    path = Column(String(100))

    def __init__(self, parent_id, path):
        self.parent_id = parent_id
        self.path = path
