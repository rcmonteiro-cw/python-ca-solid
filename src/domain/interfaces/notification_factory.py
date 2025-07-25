"""
Interface para factory de serviços de notificação.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any

from src.domain.interfaces.notification_service import NotificationService


class NotificationFactory(ABC):
    """Interface para factory de serviços de notificação"""

    @abstractmethod
    def create_notification_service(
        self,
        notification_type: str,
        config: Dict[str, Any]
    ) -> NotificationService:
        """
        Cria uma instância de serviço de notificação
        
        Args:
            notification_type: Tipo de serviço de notificação ('email', 'sms', etc)
            config: Configurações específicas do serviço
            
        Returns:
            NotificationService: Instância do serviço de notificação
            
        Raises:
            ValueError: Se o tipo de notificação não for suportado
        """
        pass 