from abc import ABC, abstractmethod
from typing import Any, Dict


class IOAuthClient(ABC):
    @abstractmethod
    async def get_token(self, auth_code: str) -> Dict[str, Any]:
        """Получение токена по коду авторизации"""
        pass
