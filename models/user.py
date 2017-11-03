from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from models.base import Base
from models.image import Image
from models.video import Video
from models.audio import Audio
from models.settings import Settings


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    email = Column(String(30))
    images = relationship("Image")
    videos = relationship("Video")
    audios = relationship("Audio")
    settings = relationship("Settings")

    def __init__(self, name, email):
        self.name = name
        self.email = email
