from app.db.database import Base
from sqlalchemy import Column, Integer, String, Enum
from app.db.models.enums import BreedSize, BreedEnergylevel


class Breed(Base):
    __tablename__ = "breeds"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String, unique=True, nullable=False)
    size = Column(Enum(BreedSize), nullable=True)
    energy_level = Column(Enum(BreedEnergylevel), nullable=True)
    image_link = Column(String, nullable=True)
