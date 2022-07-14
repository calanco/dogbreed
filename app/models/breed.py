from app.database import Base
from sqlalchemy import Column, Integer, String, Enum
from app.models.enums import BreedSize, BreedEnergyLevel


class Breed(Base):
    __tablename__ = "breeds"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String, unique=True, nullable=False)
    size = Column(Enum(BreedSize), nullable=True)
    energy_level = Column(Enum(BreedEnergyLevel), nullable=True)
    image_link = Column(String, nullable=True)
