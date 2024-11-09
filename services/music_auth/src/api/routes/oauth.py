from api.dependencies.oauth import get_oauth_use_case
from application.commands.oauth import ProcessOAuthCallbackCommand
from fastapi import APIRouter, Depends, Query

from domain.value_objects.music_service import MusicService

router = APIRouter(tags=["oauth"])


@router.get("/")
async def oauth_callback(
    code: str = Query(..., description="Authorization code from OAuth provider"),
    oauth_use_case=Depends(get_oauth_use_case),
):
    """
    Обработка callback от OAuth провайдера
    """
    token = await oauth_use_case.execute(
        ProcessOAuthCallbackCommand(
            auth_code=code,
            service=MusicService.YANDEX,  # TODO Пока только яндекс сделал так
        )
    )
    return token
