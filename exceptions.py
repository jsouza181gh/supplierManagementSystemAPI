class BadRequestException(Exception):
    def __init__(self, message="Invalid request info"):
        self.message = message
        self.status_code = 400
        super().__init__(self.message)

class UnauthorizedException(Exception):
    def __init__(self, message="Invalid credentials"):
        self.message = message
        self.status_code = 401
        super().__init__(self.message)

class NotFoundException(Exception):
    def __init__(self, message="Resource not found"):
        self.message = message
        self.status_code = 404
        super().__init__(self.message)

class ConflictException(Exception):
    def __init__(self, message="Conflict"):
        self.status_code = 409
        super().__init__(message)