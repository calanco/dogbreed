class ExistingBreedException(Exception):
    def __init__(self, breed):
        self.status_code = 409
        self.detail = f"Breed {breed} already exists"
