from keycloak import KeycloakAdmin, KeycloakError, KeycloakOpenID
from keycloak.exceptions import KeycloakGetError, KeycloakPostError, KeycloakPutError, KeycloakDeleteError, KeycloakAuthenticationError
from app_localtion_car_ssr_project import settings

class KeycloakHandler:
    def __init__(self) -> None:
        self._server_url = settings.KEYCLOAK_CONFIG["KEYCLOAK_SERVER_URL"]
        self._username = settings.KEYCLOAK_CONFIG["KEYCLOACK_ADMIN_USERNAME"]
        self._password = settings.KEYCLOAK_CONFIG["KEYCLOAK_ADMIN_PASSWORD"]
        self._client_id = settings.KEYCLOAK_CONFIG["KEYCLOAK_CLIENT_ID"]
        self._client_secret_key = settings.KEYCLOAK_CONFIG.get('KEYCLOAK_CLIENT_SECRET_KEY', None)
        self._realm_name = settings.KEYCLOAK_CONFIG['KEYCLOAK_REALM']
        self._public_key = settings.KEYCLOAK_CONFIG['KEYCLOAK_CLIENT_PUBLIC_KEY']

    def get_keycloak_admin(self) -> KeycloakAdmin:
        try:
            keycloak_admin = KeycloakAdmin(
                server_url=self._server_url,
                username=self._username,
                password=self._password,
                realm_name=self._realm_name,
                client_id=self._client_id,
                client_secret_key=self._client_secret_key,
                verify=True
            )
            return keycloak_admin
        except KeycloakAuthenticationError as e:
            raise KeycloakAuthenticationError(f"Authentication error (Function:get_keycloak_admin): {e}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_keycloak_admin): {e}")
        except Exception as e:
            raise Exception(f"Error initializing KeycloakAdmin (Function:get_keycloak_admin): {e}")

    def get_keycloak_client(self) -> KeycloakOpenID:
        try:
            keycloak_client = KeycloakOpenID(
                server_url=self._server_url,
                realm_name=self._realm_name,
                client_id=self._client_id,
                client_secret_key=self._client_secret_key,
                verify=True
            )
            return keycloak_client
        except KeycloakAuthenticationError as e:
            raise KeycloakAuthenticationError(f"Authentication error (Function:get_keycloak_client): {e}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_keycloak_client): {e}")
        except Exception as e:
            raise Exception(f"Error initializing KeycloakOpenID (Function:get_keycloak_client): {e}")

    def create_keycloak_user(self, user_data: dict):
        try:
            payload = {
                "username": user_data.get("username"),
                "email": user_data.get("email"),
                "emailVerified": False,
                "enabled": True,
                "firstName": user_data.get("first_name"),
                "lastName": user_data.get("last_name"),
                "credentials": [{
                    "type": "password",
                    "value": user_data.get("password"),
                    "hashIterations": 27500,
                    "algorithm": "pbkdf2-sha256",
                    "temporary": True
                }]
            }
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                user_id = keycloak_admin.create_user(payload=payload, exist_ok=False)
                print('this is my user id',user_id)
                return user_id
        except KeycloakPostError as e:
            raise KeycloakPostError(f"Error creating Keycloak user (Function:create_keycloak_user): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:create_keycloak_user): {e}")
        except Exception as e:
            raise Exception(f"Error creating Keycloak user (Function:create_keycloak_user): {e}")

    def delete_keycloak_user(self, user_id: str):
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                keycloak_admin.delete_user(user_id=user_id)
        except KeycloakDeleteError as e:
            raise KeycloakDeleteError(f"Error deleting Keycloak user (Function:delete_keycloak_user): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:delete_keycloak_user): {e}")
        except Exception as e:
            raise Exception(f"Error deleting Keycloak user (Function:delete_keycloak_user): {e}")

    def get_keycloak_user(self, user_id: str):
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                user = keycloak_admin.get_user(user_id=user_id)
                return user
        except KeycloakGetError as e:
            raise KeycloakGetError(f"Error retrieving Keycloak user (Function:get_keycloak_user): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_keycloak_user): {e}")
        except Exception as e:
            raise Exception(f"Error retrieving Keycloak user (Function:get_keycloak_user): {e}")

    def get_keycloak_users(self):
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                users = keycloak_admin.get_users()
                return users
        except KeycloakGetError as e:
            raise KeycloakGetError(f"Error retrieving Keycloak users (Function:get_keycloak_users): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_keycloak_users): {e}")
        except Exception as e:
            raise Exception(f"Error retrieving Keycloak users (Function:get_keycloak_users): {e}")


    def get_user_info(self, token: str):
        try:
            keycloak_client = self.get_keycloak_client()
            if keycloak_client:
                user_info = keycloak_client.userinfo(token)
                return user_info
        except KeycloakGetError as e:
            raise KeycloakGetError(f"Error retrieving user info (Function:get_user_info): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_user_info): {e}")
        except Exception as e:
            raise Exception(f"Error retrieving user info (Function:get_user_info): {e}")

    def assign_roles_to_user(self, user_id: str, roles: list):
        roles = [
    {
        "id": "3347d078-4a44-4c39-8cf4-122f756e19a7",
            "name": "agent",  # Replace with the actual role name
    },
    
]
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                keycloak_admin.assign_client_role(user_id=user_id, client_id=keycloak_admin.get_client_id(self._client_id), roles=roles)
        except KeycloakPutError as e:
            raise KeycloakPutError(f"Error assigning roles to user (Function:assign_roles_to_user): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:assign_roles_to_user): {e}")
        except Exception as e:
            raise Exception(f"Error assigning roles to user (Function:assign_roles_to_user): {e}")

    def create_user_and_assign_roles(self, user_data: dict, roles: list):
        try:
            user_id = self.create_keycloak_user(user_data=user_data)
            if user_id:
                self.assign_roles_to_user(user_id=user_id, roles=roles)
                return user_id
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:create_user_and_assign_roles): {e}")
        except Exception as e:
            raise Exception(f"Error creating user and assigning roles (Function:create_user_and_assign_roles): {e}")

    def get_roles_of_user(self, user_id: str):
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                roles = keycloak_admin.get_client_roles(user_id=user_id, client_id=self._client_id)
                return roles
        except KeycloakGetError as e:
            raise KeycloakGetError(f"Error retrieving roles of user (Function:get_roles_of_user): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_roles_of_user): {e}")
        except Exception as e:
            raise Exception(f"Error retrieving roles of user (Function:get_roles_of_user): {e}")

    def get_realm_roles(self):
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                roles = keycloak_admin.get_client_roles(client_id=keycloak_admin.get_client_id(self._client_id))
                return roles
        except KeycloakGetError as e:
            raise KeycloakGetError(f"Error retrieving realm roles (Function:get_realm_roles): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_realm_roles): {e}")
        except Exception as e:
            raise Exception(f"Error retrieving realm roles (Function:get_realm_roles): {e}")

    def get_realm_role(self, role_name: str):
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                role = keycloak_admin.get_realm_role(role_name=role_name)
                return role
        except KeycloakGetError as e:
            raise KeycloakGetError(f"Error retrieving realm role (Function:get_realm_role): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_realm_role): {e}")
        except Exception as e:
            raise Exception(f"Error retrieving realm role (Function:get_realm_role): {e}")

    def get_user_token(self, usercredentaials: dict):
        username = usercredentaials.get('username')
        password = usercredentaials.get('password')
        try:
            keycloak_client = self.get_keycloak_client()
            if keycloak_client:
                token = keycloak_client.token(username=username, password=password)
                return token
        except KeycloakAuthenticationError as e:
            raise KeycloakAuthenticationError(f"Authentication error (Function:get_user_token): {e}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_user_token): {e}")
        except Exception as e:
            raise Exception(f"Error retrieving user token (Function:get_user_token): {e}")

    def get_user_refresh_token(self, refresh_token: str):
        try:
            keycloak_client = self.get_keycloak_client()
            if keycloak_client:
                token = keycloak_client.refresh_token(refresh_token=refresh_token)
                return token
        except KeycloakAuthenticationError as e:
            raise KeycloakAuthenticationError(f"Authentication error (Function:get_user_refresh_token): {e}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:get_user_refresh_token): {e}")
        except Exception as e:
            raise Exception(f"Error refreshing user token (Function:get_user_refresh_token): {e}")


    def connect_user(self, usercredits: dict):
        try:
            keycloak_client = self.get_keycloak_client()
            if keycloak_client:
                token = keycloak_client.token(username=usercredits['username'], password=usercredits['password'])
                return token
        except KeycloakAuthenticationError as e:
            raise KeycloakAuthenticationError(f"Authentication error (Function:connect_user): {e}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:connect_user): {e}")
        except Exception as e:
            raise Exception(f"Error connecting user (Function:connect_user): {e}")
        
    def logout_user(self, refresh_token: str):
        try:
            keycloak_client = self.get_keycloak_client()
            if keycloak_client:
                keycloak_client.logout(refresh_token=refresh_token)
        except KeycloakAuthenticationError as e:
            raise KeycloakAuthenticationError(f"Authentication error (Function:logout_user): {e}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:logout_user): {e}")
        except Exception as e:
            raise Exception(f"Error logging out user (Function:logout_user): {e}")
        
    def send_password_reset_mail(self, user_id: str):
        try:
            keycloak_admin = self.get_keycloak_admin()
            if keycloak_admin:
                # Define the payload with the required action
                payload = ["UPDATE_PASSWORD"]  # Action to update password
                
                # Send the update account email
                response = keycloak_admin.send_update_account(
                    user_id=user_id,
                    payload=payload,
                    client_id=self._client_id,  # Optional: Specify the client ID
                    lifespan=3600,  # Optional: Set the link expiration time (e.g., 1 hour)
                )
                return response
        except KeycloakPostError as e:
            raise KeycloakPostError(f"Error sending password reset email (Function:send_password_reset_mail): {e.response_code} - {e.response_body}")
        except KeycloakError as e:
            raise KeycloakError(f"KeycloakError (Function:send_password_reset_mail): {e}")
        except Exception as e:
            raise Exception(f"Error sending password reset email (Function:send_password_reset_mail): {e}")