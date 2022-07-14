class ExistingBreedException(Exception):
    def __init__(self, breed):
        self.status_code = 409
        self.detail = f"Breed {breed} already exists"


class UnExistingBreedException(Exception):
    def __init__(self, id):
        self.status_code = 404
        self.detail = f"Breed with id {id} doesn't exist"
