from rest_framework.viewsets import GenericViewSet
from common.shared.wrappers.rWrapper import ResponseWrapper
from user_identification.exceptions.exception_handler import IdentificationException
from user_identification.services.identification_service import IdentificatioService

# rest framework django view 



class UserIdentificationViewSet(GenericViewSet):

    identification_service=IdentificatioService()


    def signin(self, request):
        try:
            data = self.identification_service.signin(request)
            return ResponseWrapper(data=data, message="User signed in successfully.", success=True, status=200)
        except Exception as e:
            return ResponseWrapper(message=str(e), success=False, status=500, data=None)
    
    def signup(self, request):
        try:
            data = self.identification_service.signup(request)
            return ResponseWrapper(data=data, message="User registered successfully.", success=True, status=201)
        except IdentificationException as e:
            return ResponseWrapper(message=str(e), success=False, status=500)
    
    def logout(self, request):
        try:
            data = self.keycloak_handler.logout(request)
            return ResponseWrapper(data=data, message="User logged out successfully.", success=True, status=200)
        except IdentificationException as e:
            return ResponseWrapper(message=str(e), success=False, status=500)
    def register_user(self, request):
        try:
            data = self.identification_service.register_user(request)
            return ResponseWrapper(data=data, message="User registered successfully.", success=True, status=201)
        except IdentificationException as e:
            return ResponseWrapper(message=str(e), success=False, status=500)