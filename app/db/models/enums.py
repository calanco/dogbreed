from enum import Enum


class BreedSize(Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'
    extra_large = 'extra_large'


class BreedEnergyLevel(Enum):
    low = 'low'
    moderate = 'moderate'
    high = 'high'
