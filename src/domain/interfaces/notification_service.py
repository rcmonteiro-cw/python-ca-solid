"""
Interface para serviços de notificação.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class NotificationType(Enum):
    """Tipos de notificação suportados"""
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"


@dataclass
class NotificationRecipient:
    """Destinatário da notificação"""
    identifier: str  # Email, número de telefone, device token, etc.
    type: NotificationType
    name: Optional[str] = None


@dataclass
class NotificationContent:
    """Conteúdo da notificação"""
    subject: str
    body: str
    template_id: Optional[str] = None
    template_data: Optional[dict] = None


@dataclass
class NotificationResult:
    """Resultado do envio da notificação"""
    success: bool
    recipient: NotificationRecipient
    error_message: Optional[str] = None
    external_id: Optional[str] = None


class NotificationService(ABC):
    """Interface base para serviços de notificação"""

    @abstractmethod
    def send_notification(
        self,
        recipient: NotificationRecipient,
        content: NotificationContent
    ) -> NotificationResult:
        """
        Envia uma notificação para um destinatário
        
        Args:
            recipient: Destinatário da notificação
            content: Conteúdo da notificação
            
        Returns:
            NotificationResult: Resultado do envio
        """
        pass

    @abstractmethod
    def send_bulk_notifications(
        self,
        recipients: List[NotificationRecipient],
        content: NotificationContent
    ) -> List[NotificationResult]:
        """
        Envia uma notificação para múltiplos destinatários
        
        Args:
            recipients: Lista de destinatários
            content: Conteúdo da notificação
            
        Returns:
            List[NotificationResult]: Lista com os resultados dos envios
        """
        pass 