
from common.shared.keycloak.helpers.KeycloakHandler import KeycloakHandler
from common.shared.serializers.user_kek_serializer import KekUserLoginSerializer, KekUserRegisterSerializer

class IdentificatioService:
    keycloak_handler = KeycloakHandler()

    def signin(self, request):
        user_signin_serializer = KekUserLoginSerializer(data=request.data)
        user_signin_serializer.is_valid(raise_exception=True)
        user_credentials = user_signin_serializer.validated_data
        signin_res = self.keycloak_handler.get_user_token(user_credentials)
        return signin_res

    def signout(self, request):
        refresh_token = request.data.get('refresh_token')
        self.keycloak_handler.logout_user(refresh_token)
        return None

    def register_user(self, request):
        serializer = KekUserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        user_roles = user_data.pop("roles", None)
        user = self.keycloak_handler.create_user_and_assign_roles(user_data, user_roles)
        return user

