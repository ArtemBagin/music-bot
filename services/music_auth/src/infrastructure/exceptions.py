class InfrastructureError(Exception):
    """Базовый класс для ошибок инфраструктурного слоя"""

    pass


class OAuthError(InfrastructureError):
    """Ошибка при работе с OAuth"""

    pass
