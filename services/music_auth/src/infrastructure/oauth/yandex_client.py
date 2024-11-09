from typing import Any

import httpx

from domain.interfaces.oauth_client import IOAuthClient
from domain.value_objects.oauth_config import OAuthConfig
from domain.value_objects.token_params import TokenRequestParams
from infrastructure.exceptions import OAuthError


class YandexOAuthClient(IOAuthClient):
    def __init__(self, config: OAuthConfig):
        self.config = config
        self._headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self._token_url = f"{self.config.oauth_base_url}/token"

    async def get_token(self, auth_code: str) -> dict[str, Any]:
        token_params = TokenRequestParams.create_authorization_code_flow(
            code=auth_code,
            client_id=self.config.client_id,
            client_secret=self.config.client_secret,
        )

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self._token_url, data=vars(token_params), headers=self._headers
                )

                if response.status_code != 200:
                    error_data = (
                        response.json()
                        if response.headers.get("content-type") == "application/json"
                        else response.text
                    )
                    raise OAuthError(
                        f"Failed to get token. Status: {response.status_code}, Details: {error_data}"
                    )

                return response.json()
        except httpx.RequestError as exception:
            raise OAuthError(f"Request failed: {exception}")
        except Exception as exception:
            raise OAuthError(f"Unexpected error: {exception}")
