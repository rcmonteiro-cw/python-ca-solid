"""
Implementação mock do serviço de notificação para testes.
"""
from typing import List

from src.domain.interfaces.notification_service import (
    NotificationService,
    NotificationRecipient,
    NotificationContent,
    NotificationResult
)


class MockNotificationService(NotificationService):
    """Implementação mock do serviço de notificação para testes"""

    def __init__(self, should_fail: bool = False):
        self.notifications_sent: List[tuple[NotificationRecipient, NotificationContent]] = []
        self.should_fail = should_fail

    def send_notification(
        self,
        recipient: NotificationRecipient,
        content: NotificationContent
    ) -> NotificationResult:
        """Simula o envio de uma notificação"""
        self.notifications_sent.append((recipient, content))

        if self.should_fail:
            return NotificationResult(
                success=False,
                recipient=recipient,
                error_message="Falha simulada no envio"
            )

        return NotificationResult(
            success=True,
            recipient=recipient,
            external_id=f"mock_{len(self.notifications_sent)}"
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

    def get_notifications_sent(self) -> List[tuple[NotificationRecipient, NotificationContent]]:
        """Retorna a lista de notificações enviadas"""
        return self.notifications_sent 