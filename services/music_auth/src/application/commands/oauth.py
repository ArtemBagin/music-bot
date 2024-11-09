from dataclasses import dataclass

from domain.value_objects.music_service import MusicService


@dataclass
class ProcessOAuthCallbackCommand:
    """Входные данные для обработки OAuth callback"""

    service: MusicService
    auth_code: str
