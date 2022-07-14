from pydantic import BaseModel
from typing import Optional
from app.models.enums import BreedSize, BreedEnergyLevel


class RequestBreed(BaseModel):
    """Model breed requests of user."""
    name: str
    size: Optional[BreedSize] = None
    energy_level: Optional[BreedEnergyLevel] = None
    image_link: Optional[str] = None
