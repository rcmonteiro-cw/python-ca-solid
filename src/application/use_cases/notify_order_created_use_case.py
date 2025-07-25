"""
Use case para notificar sobre a criação de um pedido.
"""
from dataclasses import dataclass
from decimal import Decimal

from src.domain.interfaces.use_case import UseCase, Response
from src.domain.interfaces.notification_service import (
    NotificationService,
    NotificationRecipient,
    NotificationContent,
    NotificationType,
    NotificationResult
)
from src.domain.entities.order import Order


@dataclass
class NotifyOrderCreatedInput:
    """DTO de entrada para notificação de pedido criado"""
    order: Order
    customer_email: str
    customer_name: str


class NotifyOrderCreatedUseCase(UseCase[NotifyOrderCreatedInput, NotificationResult]):
    """Use case para notificar sobre a criação de um pedido"""

    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def execute(self, request: NotifyOrderCreatedInput) -> Response[NotificationResult]:
        """Executa o use case"""
        try:
            # Cria o destinatário
            recipient = NotificationRecipient(
                identifier=request.customer_email,
                type=NotificationType.EMAIL,
                name=request.customer_name
            )

            # Formata o valor total
            total = request.order.total
            if isinstance(total, Decimal):
                formatted_total = f"R$ {total:.2f}"
            else:
                formatted_total = str(total)

            # Cria o conteúdo da notificação
            content = NotificationContent(
                subject=f"Pedido {request.order.id} criado com sucesso!",
                body=f"""
Olá {request.customer_name},

Seu pedido foi criado com sucesso!

Número do pedido: {request.order.id}
Total: {formatted_total}

Itens do pedido:
{self._format_order_items(request.order)}

Obrigado por sua compra!
                """.strip()
            )

            # Envia a notificação
            result = self.notification_service.send_notification(recipient, content)

            return Response(
                success=result.success,
                data=result,
                error=result.error_message
            )

        except Exception as e:
            return Response(
                success=False,
                error=f"Erro ao enviar notificação: {str(e)}"
            )

    def _format_order_items(self, order: Order) -> str:
        """Formata os itens do pedido para exibição"""
        items_text = []
        for item in order.items:
            price = (
                f"R$ {item.price:.2f}"
                if isinstance(item.price, Decimal)
                else str(item.price)
            )
            items_text.append(
                f"- {item.product_id}: {item.quantity}x {price}"
            )
        return "\n".join(items_text) 