
import threading
from common.shared.keycloak.helpers.KeycloakHandler import KeycloakHandler
from common.shared.serializers.user_kek_serializer import KekUserLoginSerializer, KekUserRegisterSerializer

class IdentificationService:
    keycloak_handler = KeycloakHandler()

    def signin(self, request):
        user_signin_serializer = KekUserLoginSerializer(data=request.data)
        user_signin_serializer.is_valid(raise_exception=True)
        user_credentials = user_signin_serializer.validated_data
        try :
            signin_res = self.keycloak_handler.get_user_token(user_credentials)
            return signin_res
        except Exception as e:
            raise e

        

    def signout(self, request):
        refresh_token = request.data.get('refresh_token')
        self.keycloak_handler.logout_user(refresh_token)
        return None

    def signup(self, request):
        serializer = KekUserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        user_roles = user_data.pop("roles", None)
        try:
            # Create the user in Keycloak
            user_id = self.keycloak_handler.create_user_and_assign_roles(user_data, user_roles)
            
            # Send password reset email
            email_thread = threading.Thread(target=self.keycloak_handler.send_password_reset_mail, args=(user_id,))
            email_thread.start()
            
            return user_id
        except Exception as e:
            raise e

    def connected_user(self,request):
        try:
            user_info = self.keycloak_handler.get_user_info(request.data['access_token'])
            return user_info
        except Exception as e:
            raise e