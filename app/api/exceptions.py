class ExistingBreedException(Exception):
    """Throw if breed already exists."""
    def __init__(self, breed):
        self.status_code = 409
        self.detail = f"Breed {breed} already exists"


class UnExistingBreedException(Exception):
    """Throw if breed with id doesn't exist."""
    def __init__(self, id):
        self.status_code = 404
        self.detail = f"Breed with id {id} doesn't exist"
