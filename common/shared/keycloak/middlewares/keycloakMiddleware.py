
import ast
from http import HTTPStatus
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from keycloak import KeycloakError, KeycloakOpenID
from rest_framework.exceptions import PermissionDenied, NotAuthenticated

from app_localtion_car_ssr_project import settings
from common.shared.keycloak.helpers.by_pass_permissions import FilterByPassPermissions

class keycloakMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        """
        :param get_response:
        """
        super().__init__(get_response)
        self.config = settings.KEYCLOAK_CONFIG

        # Read configurations
        try:
            self.server_url = self.config['KEYCLOAK_SERVER_URL']
            self.client_id = self.config['KEYCLOAK_CLIENT_ID']
            self.realm = self.config['KEYCLOAK_REALM']
        except KeyError as e:
            raise Exception(
                "KEYCLOAK_SERVER_URL, KEYCLOAK_CLIENT_ID or KEYCLOAK_REALM not found.")

        self.client_secret_key = self.config.get(
            'KEYCLOAK_CLIENT_SECRET_KEY', None)
        self.client_public_key = self.config.get(
            'KEYCLOAK_CLIENT_PUBLIC_KEY', None)
        self.default_access = self.config.get(
            'KEYCLOAK_DEFAULT_ACCESS', "DENY")
        self.method_validate_token = self.config.get(
            'KEYCLOAK_METHOD_VALIDATE_TOKEN', "INTROSPECT")
        self.keycloak_authorization_config = self.config.get(
            'KEYCLOAK_AUTHORIZATION_CONFIG', None)

        # Create Keycloak instance
        self.keycloak = KeycloakOpenID(server_url=self.server_url,
                                       client_id=self.client_id,
                                       realm_name=self.realm,
                                       client_secret_key=self.client_secret_key)

        # Django
        self.get_response = get_response

    def __call__(self, request):
        """
        :param request:
        :return:
        """
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Validate only the token introspect.
        :param request: django request
        :param view_func:
        :param view_args: view args
        :param view_kwargs: view kwargs
        :return:
        """
        # check for guest permissions before requesting from keycloak
        if FilterByPassPermissions.isGuest(request):
            return None
        # extract scopes and resource from the view_class
        try:
            view_scopes = view_func.cls.keycloak_resources_scopes['scopes']
            resource = view_func.cls.keycloak_resources_scopes['resource']
        except AttributeError as e:
            # bad request response
                        return JsonResponse({"state": 'no scopes was passed from the view func', "detail": PermissionDenied.default_detail},
                                status=HTTPStatus.BAD_REQUEST)
        # check if the token is present in the request headers before moving forward
        if 'HTTP_AUTHORIZATION' not in request.META:
            return JsonResponse({"detail": NotAuthenticated.default_detail},
                                status=NotAuthenticated.status_code)
        # parse the token from the request header
        auth_header = request.META.get('HTTP_AUTHORIZATION').split()
        token = auth_header[1] if len(auth_header) == 2 else auth_header[0]
        # Get default scope if method is not defined.
        required_scope = view_scopes.get(request.method, None) \
            if view_scopes.get(request.method, None) else view_scopes.get('DEFAULT', None)

        # DEFAULT scope not found and DEFAULT_ACCESS is DENY = Permissions Denied 403
        if not required_scope and self.default_access == 'DENY':
            return JsonResponse({"state": 'no required_scope was passed from the view func', "detail": PermissionDenied.default_detail},
                                status=PermissionDenied.status_code)
        # get user permissions from the token provided  with the request
        # and the scopes + resource from the view class
        try:
            user_permissions = self.keycloak.uma_permissions(
                token, permissions=resource)
        # if NotAuthorized or Not Authenticated(token invalid ) a Permission denied Response will be returned
        except KeycloakError as e:
            response = ast.literal_eval(e.response_body.decode('utf-8'))
            status_code = e.response_code
            return JsonResponse(response, status=status_code)
        # if there is a matching witth the user_permissions and the scopes/resources in the view class
        # then authorize the request and pass to the view handler function
        print(user_permissions)
        for perm in user_permissions:
            if required_scope in perm['scopes']:
                return None

        # User Permission Denied
        return JsonResponse({"detail": PermissionDenied.default_detail},
                            status=PermissionDenied.status_code)