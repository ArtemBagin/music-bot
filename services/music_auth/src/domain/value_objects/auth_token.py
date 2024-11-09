from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class AuthToken:
    access_token: str
    expires_in: datetime | None = None

    def is_expired(self) -> bool:
        """Проверка срока действия токена"""
        if not self.expires_in:
            return False
        return datetime.now(UTC) > self.expires_in

    def __str__(self) -> str:
        return f"AuthToken(expires_in={self.expires_in})"
