from application.commands.oauth import ProcessOAuthCallbackCommand

from domain.interfaces.oauth_client import IOAuthClient
from domain.value_objects.auth_token import AuthToken


class ProcessOAuthCallbackUseCase:
    def __init__(self, oauth_client: IOAuthClient):
        self._oauth_client = oauth_client

    async def execute(self, command: ProcessOAuthCallbackCommand) -> AuthToken:
        token_response = await self._oauth_client.get_token(command.auth_code)

        token = AuthToken(
            access_token=token_response.get("access_token"),
            expires_in=token_response.get("expires_in"),
        )

        # TODO отправлять рэббитом инфу.

        return token
