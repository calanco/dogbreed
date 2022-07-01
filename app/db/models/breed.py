from app.db.database import Base
from sqlalchemy import Column, Integer, String


class Breed(Base):
    __tablename__ = "breeds"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String, unique=True, nullable=False)
    size = Column(String, nullable=True)
    energy_level = Column(String, nullable=True)
    image_link = Column(String, nullable=True)
