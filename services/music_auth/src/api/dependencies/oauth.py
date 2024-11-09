from application.use_cases.process_oauth import ProcessOAuthCallbackUseCase
from fastapi import Depends

from infrastructure.container import Container

container = Container()


async def get_oauth_client():
    return container.oauth_client()


async def get_oauth_use_case(oauth_client=Depends(get_oauth_client)):
    return ProcessOAuthCallbackUseCase(oauth_client=oauth_client)
