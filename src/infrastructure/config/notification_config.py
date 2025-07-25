"""
Configuração dos serviços de notificação.
"""
from typing import Dict, Any

from src.domain.interfaces.notification_factory import NotificationFactory
from src.infrastructure.factories.notification_factory import (
    DefaultNotificationFactory,
    NotificationFactoryWithLogging
)


class NotificationConfig:
    """Configuração dos serviços de notificação"""

    @staticmethod
    def get_email_config() -> Dict[str, Any]:
        """
        Retorna a configuração para o serviço de email.
        Em um caso real, isso poderia vir de variáveis de ambiente ou arquivo de configuração.
        """
        return {
            "smtp_host": "smtp.example.com",
            "smtp_port": 587,
            "smtp_user": "user@example.com",
            "smtp_password": "password",
            "default_from_email": "notifications@example.com"
        }

    @staticmethod
    def get_mock_config() -> Dict[str, Any]:
        """Retorna a configuração para o serviço mock"""
        return {
            "should_fail": False
        }

    @staticmethod
    def create_factory(with_logging: bool = False) -> NotificationFactory:
        """
        Cria uma instância da factory de notificação
        
        Args:
            with_logging: Se True, adiciona logging à factory
            
        Returns:
            NotificationFactory: Instância configurada da factory
        """
        factory = DefaultNotificationFactory()
        
        if with_logging:
            factory = NotificationFactoryWithLogging(factory)
        
        return factory 