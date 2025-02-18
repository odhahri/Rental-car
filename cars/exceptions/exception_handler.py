# exceptions.py
from rest_framework import status

class CarServiceException(Exception):
    def __init__(self, message="An error occurred.", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class CarNotFoundException(CarServiceException):
    def __init__(self, message="Car not found.", status_code=status.HTTP_404_NOT_FOUND):
        super().__init__(message, status_code)

class BlobNotFoundException(CarServiceException):
    def __init__(self, message="Blob not found.", status_code=status.HTTP_404_NOT_FOUND):
        super().__init__(message, status_code)

class ValidationException(CarServiceException):
    def __init__(self, message="Invalid input.", status_code=status.HTTP_400_BAD_REQUEST):
        super().__init__(message, status_code)