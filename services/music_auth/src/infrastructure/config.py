from dependency_injector import containers, providers
from pydantic_settings import BaseSettings, SettingsConfigDict

from domain.value_objects.oauth_config import OAuthConfig


class Settings(BaseSettings):
    """Все настройки приложения"""

    YANDEX_OAUTH_CLIENT_ID: str
    YANDEX_OAUTH_CLIENT_SECRET: str
    YANDEX_OAUTH_BASE_URL: str = "https://oauth.yandex.ru"

    RABBITMQ_URL: str
    RABBITMQ_EXCHANGE: str
    RABBITMQ_QUEUE: str

    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )


class ConfigurationContainer(containers.DeclarativeContainer):
    """Контейнер конфигурации"""

    settings = providers.Singleton(Settings)

    oauth_config = providers.Singleton(
        OAuthConfig,
        client_id=settings.provided.YANDEX_OAUTH_CLIENT_ID,
        client_secret=settings.provided.YANDEX_OAUTH_CLIENT_SECRET,
        oauth_base_url=settings.provided.YANDEX_OAUTH_BASE_URL,
    )

    rabbit_config = providers.Singleton(
        lambda settings: {
            "url": settings.RABBITMQ_URL,
            "exchange": settings.RABBITMQ_EXCHANGE,
            "queue": settings.RABBITMQ_QUEUE,
        },
        settings=settings,
    )
