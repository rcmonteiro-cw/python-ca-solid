"""
Testes para o serviço de notificação e use cases relacionados.
"""
from decimal import Decimal
import pytest

from src.application.use_cases.notify_order_created_use_case import (
    NotifyOrderCreatedUseCase,
    NotifyOrderCreatedInput
)
from src.domain.interfaces.notification_service import (
    NotificationRecipient,
    NotificationContent,
    NotificationType
)
from src.domain.entities.order import Order, OrderItem
from src.infrastructure.services.mock_notification_service import MockNotificationService


def test_mock_notification_service():
    """Testa o serviço de notificação mock"""
    service = MockNotificationService()

    # Cria uma notificação de teste
    recipient = NotificationRecipient(
        identifier="test@example.com",
        type=NotificationType.EMAIL,
        name="Test User"
    )
    content = NotificationContent(
        subject="Test Subject",
        body="Test Body"
    )

    # Envia a notificação
    result = service.send_notification(recipient, content)

    # Verifica o resultado
    assert result.success is True
    assert result.external_id == "mock_1"
    assert len(service.get_notifications_sent()) == 1

    sent_recipient, sent_content = service.get_notifications_sent()[0]
    assert sent_recipient.identifier == "test@example.com"
    assert sent_content.subject == "Test Subject"


def test_notify_order_created_use_case():
    """Testa o use case de notificação de pedido criado"""
    # Cria o serviço mock
    notification_service = MockNotificationService()
    use_case = NotifyOrderCreatedUseCase(notification_service)

    # Cria um pedido de teste
    order = Order(
        id="123",
        items=[
            OrderItem(
                product_id="prod1",
                quantity=2,
                price=Decimal("10.50")
            ),
            OrderItem(
                product_id="prod2",
                quantity=1,
                price=Decimal("15.75")
            )
        ],
        total=Decimal("36.75")
    )

    # Executa o use case
    input_dto = NotifyOrderCreatedInput(
        order=order,
        customer_email="customer@example.com",
        customer_name="John Doe"
    )
    response = use_case.execute(input_dto)

    # Verifica o resultado
    assert response.success is True
    assert response.data.success is True
    assert len(notification_service.get_notifications_sent()) == 1

    # Verifica o conteúdo da notificação
    sent_recipient, sent_content = notification_service.get_notifications_sent()[0]
    assert sent_recipient.identifier == "customer@example.com"
    assert sent_recipient.name == "John Doe"
    assert "Pedido 123 criado com sucesso!" in sent_content.subject
    assert "R$ 36.75" in sent_content.body
    assert "prod1: 2x R$ 10.50" in sent_content.body
    assert "prod2: 1x R$ 15.75" in sent_content.body


def test_notify_order_created_use_case_with_failure():
    """Testa o use case quando o serviço de notificação falha"""
    # Cria o serviço mock configurado para falhar
    notification_service = MockNotificationService(should_fail=True)
    use_case = NotifyOrderCreatedUseCase(notification_service)

    # Cria um pedido de teste
    order = Order(
        id="123",
        items=[
            OrderItem(
                product_id="prod1",
                quantity=1,
                price=Decimal("10.00")
            )
        ],
        total=Decimal("10.00")
    )

    # Executa o use case
    input_dto = NotifyOrderCreatedInput(
        order=order,
        customer_email="customer@example.com",
        customer_name="John Doe"
    )
    response = use_case.execute(input_dto)

    # Verifica o resultado
    assert response.success is False
    assert "Falha simulada no envio" in response.error
    assert len(notification_service.get_notifications_sent()) == 1 