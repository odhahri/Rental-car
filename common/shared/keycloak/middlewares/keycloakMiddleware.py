
from django.utils.deprecation import MiddlewareMixin

from app_localtion_car_ssr_project import settings
class keycloakMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self._server_url = settings.KEYCLOAK_CONFIG["KEYCLOAK_SERVER_URL"]
        self._username = settings.KEYCLOAK_CONFIG["KEYCLOACK_ADMIN_USERNAME"]
        self._password = settings.KEYCLOAK_CONFIG["KEYCLOAK_ADMIN_PASSWORD"]
        self._client_id = settings.KEYCLOAK_CONFIG["KEYCLOAK_CLIENT_ID"]
        self._client_secret_key = settings.KEYCLOAK_CONFIG.get('KEYCLOAK_CLIENT_SECRET_KEY', None)
        self._realm_name = settings.KEYCLOAK_CONFIG['KEYCLOAK_REALM']
        self._public_key = settings.KEYCLOAK_CONFIG['KEYCLOAK_CLIENT_PUBLIC_KEY']

    