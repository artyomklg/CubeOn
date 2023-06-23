from keycloak import KeycloakOpenID, KeycloakAdmin


from ..config import settings


class KeycloakService():
    def __init__(self):
        self._idp = KeycloakOpenID(
            server_url=f'{settings.KEYCLOAK_URL}/auth/',
            realm_name=settings.KEYCLOAK_REALM,
            client_id=settings.KEYCLOAK_CLIENT,
            client_secret_key=settings.KEYCLOAK_CLIENT_SECRET
        )

        self._admin = KeycloakAdmin(
            server_url=f'{settings.KEYCLOAK_URL}/auth/',
            username=settings.KEYCLOAK_USER,
            password=settings.KEYCLOAK_PASSWORD,
            client_secret_key=settings.KEYCLOAK_ADMIN_SECRET
        )

    async def auth(self, username, password):
        return await self._idp.token(username=username, password=password)
