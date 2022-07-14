from enum import Enum


class BreedSize(Enum):
    """Model size enum of breeds table"""
    small = 'small'
    medium = 'medium'
    large = 'large'
    extra_large = 'extra_large'


class BreedEnergyLevel(Enum):
    """Model energy_level enum of breeds table"""
    low = 'low'
    moderate = 'moderate'
    high = 'high'
