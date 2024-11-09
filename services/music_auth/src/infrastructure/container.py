from dependency_injector import containers, providers

from infrastructure.config import ConfigurationContainer
from infrastructure.oauth.yandex_client import YandexOAuthClient


class Container(containers.DeclarativeContainer):
    config = providers.Container(ConfigurationContainer)

    oauth_client = providers.Singleton(YandexOAuthClient, config=config.oauth_config)
