# exceptions.py
from rest_framework import status

class IdentificationException(Exception):
    def __init__(self, message="An error occurred.", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class SignInException(IdentificationException):
    def __init__(self, message="Error occured when trying to sign in user.", status_code=status.HTTP_404_NOT_FOUND):
        super().__init__(message, status_code)

class SignUpException(IdentificationException):
    def __init__(self, message="Error occured when trying to sign up user.", status_code=status.HTTP_404_NOT_FOUND):
        super().__init__(message, status_code)

