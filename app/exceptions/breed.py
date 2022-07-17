class ExistingBreedException(Exception):
    """Throw if breed already exists."""

    def __init__(self, breed):
        self.detail = f"Breed {breed} already exists"


class UnExistingBreedException(Exception):
    """Throw if breed with id doesn't exist."""

    def __init__(self, id):
        self.detail = f"Breed with id {id} doesn't exist"


class EmptyBreedTable(Exception):
    """Throw if breed table is empty."""

    def __init__(self):
        self.detail = "Breed table is empty"
