class ArrangeException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class SystemError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class ValidationException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class ReturnAPIException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors 