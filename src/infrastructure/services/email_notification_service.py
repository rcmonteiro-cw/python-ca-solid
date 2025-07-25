"""
Implementação do serviço de notificação por email.
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

from src.domain.interfaces.notification_service import (
    NotificationService,
    NotificationRecipient,
    NotificationContent,
    NotificationResult,
    NotificationType
)


class EmailNotificationService(NotificationService):
    """Implementação do serviço de notificação via SMTP"""

    def __init__(
        self,
        smtp_host: str,
        smtp_port: int,
        smtp_user: str,
        smtp_password: str,
        default_from_email: str
    ):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.default_from_email = default_from_email

    def _create_email_message(
        self,
        recipient: NotificationRecipient,
        content: NotificationContent
    ) -> MIMEMultipart:
        """Cria a mensagem de email"""
        message = MIMEMultipart()
        message["From"] = self.default_from_email
        message["To"] = recipient.identifier
        message["Subject"] = content.subject

        # Se houver template, poderia processar aqui
        body = content.body
        if content.template_id and content.template_data:
            # Aqui você poderia usar um sistema de templates como Jinja2
            pass

        message.attach(MIMEText(body, "plain"))
        return message

    def send_notification(
        self,
        recipient: NotificationRecipient,
        content: NotificationContent
    ) -> NotificationResult:
        """Envia um email para um destinatário"""
        if recipient.type != NotificationType.EMAIL:
            return NotificationResult(
                success=False,
                recipient=recipient,
                error_message="Tipo de notificação inválido para este serviço"
            )

        try:
            message = self._create_email_message(recipient, content)

            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(message)

            return NotificationResult(
                success=True,
                recipient=recipient,
                external_id=f"email_{recipient.identifier}"
            )

        except Exception as e:
            return NotificationResult(
                success=False,
                recipient=recipient,
                error_message=str(e)
            )

    def send_bulk_notifications(
        self,
        recipients: List[NotificationRecipient],
        content: NotificationContent
    ) -> List[NotificationResult]:
        """Envia emails para múltiplos destinatários"""
        results = []
        
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)

            for recipient in recipients:
                if recipient.type != NotificationType.EMAIL:
                    results.append(
                        NotificationResult(
                            success=False,
                            recipient=recipient,
                            error_message="Tipo de notificação inválido para este serviço"
                        )
                    )
                    continue

                try:
                    message = self._create_email_message(recipient, content)
                    server.send_message(message)

                    results.append(
                        NotificationResult(
                            success=True,
                            recipient=recipient,
                            external_id=f"email_{recipient.identifier}"
                        )
                    )

                except Exception as e:
                    results.append(
                        NotificationResult(
                            success=False,
                            recipient=recipient,
                            error_message=str(e)
                        )
                    )

        return results 