"""
Implementação mock do serviço de notificação para testes.
"""
from typing import List, ClassVar

from src.domain.interfaces.notification_service import (
    NotificationService,
    NotificationRecipient,
    NotificationContent,
    NotificationResult
)


class MockNotificationService(NotificationService):
    """Implementação mock do serviço de notificação para testes"""

    # Variável de classe para manter o estado entre instâncias
    _notifications_sent: ClassVar[List[tuple[NotificationRecipient, NotificationContent]]] = []

    def __init__(self, should_fail: bool = False):
        self.should_fail = should_fail

    def send_notification(
        self,
        recipient: NotificationRecipient,
        content: NotificationContent
    ) -> NotificationResult:
        """Simula o envio de uma notificação"""
        self._notifications_sent.append((recipient, content))

        if self.should_fail:
            return NotificationResult(
                success=False,
                recipient=recipient,
                error_message="Falha simulada no envio"
            )

        return NotificationResult(
            success=True,
            recipient=recipient,
            external_id=f"mock_{len(self._notifications_sent)}"
        )

    def send_bulk_notifications(
        self,
        recipients: List[NotificationRecipient],
        content: NotificationContent
    ) -> List[NotificationResult]:
        """Simula o envio de múltiplas notificações"""
        return [
            self.send_notification(recipient, content)
            for recipient in recipients
        ]

    @classmethod
    def get_notifications_sent(cls) -> List[tuple[NotificationRecipient, NotificationContent]]:
        """Retorna a lista de notificações enviadas"""
        return cls._notifications_sent

    @classmethod
    def clear_notifications(cls) -> None:
        """Limpa a lista de notificações enviadas"""
        cls._notifications_sent.clear() 