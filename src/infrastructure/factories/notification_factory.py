"""
Implementação concreta da factory de serviços de notificação.
"""
from typing import Dict, Any

from src.domain.interfaces.notification_factory import NotificationFactory
from src.domain.interfaces.notification_service import NotificationService
from src.infrastructure.services.email_notification_service import EmailNotificationService
from src.infrastructure.services.mock_notification_service import MockNotificationService


class DefaultNotificationFactory(NotificationFactory):
    """Implementação padrão da factory de notificações"""

    def create_notification_service(
        self,
        notification_type: str,
        config: Dict[str, Any]
    ) -> NotificationService:
        """
        Cria uma instância de serviço de notificação baseado no tipo
        
        Args:
            notification_type: Tipo de serviço ('email', 'mock')
            config: Configurações do serviço
            
        Returns:
            NotificationService: Instância configurada do serviço
            
        Raises:
            ValueError: Se o tipo não for suportado
        """
        if notification_type == "email":
            return EmailNotificationService(
                smtp_host=config["smtp_host"],
                smtp_port=config["smtp_port"],
                smtp_user=config["smtp_user"],
                smtp_password=config["smtp_password"],
                default_from_email=config["default_from_email"]
            )
        elif notification_type == "mock":
            return MockNotificationService(
                should_fail=config.get("should_fail", False)
            )
        else:
            raise ValueError(f"Tipo de notificação não suportado: {notification_type}")


class NotificationFactoryWithLogging(NotificationFactory):
    """
    Decorator para factory que adiciona logging.
    Demonstra como podemos estender a factory sem modificar o código existente (OCP).
    """

    def __init__(self, factory: NotificationFactory):
        self.factory = factory

    def create_notification_service(
        self,
        notification_type: str,
        config: Dict[str, Any]
    ) -> NotificationService:
        """Cria o serviço e registra a criação"""
        print(f"Criando serviço de notificação do tipo: {notification_type}")
        service = self.factory.create_notification_service(notification_type, config)
        print(f"Serviço criado com sucesso: {service.__class__.__name__}")
        return service 