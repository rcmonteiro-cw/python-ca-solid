"""
Testes para a factory de notificação.
"""
from decimal import Decimal
import pytest

from src.domain.entities.order import Order, OrderItem
from src.infrastructure.config.notification_config import NotificationConfig
from src.application.use_cases.notify_order_created_use_case import (
    NotifyOrderCreatedUseCase,
    NotifyOrderCreatedInput
)
from src.infrastructure.services.mock_notification_service import MockNotificationService


@pytest.fixture(autouse=True)
def clear_notifications():
    """Limpa as notificações antes de cada teste"""
    MockNotificationService.clear_notifications()
    yield


def test_create_email_notification_service():
    """Testa a criação do serviço de email"""
    # Cria a factory com logging
    factory = NotificationConfig.create_factory(with_logging=True)
    
    # Obtém a configuração de email
    config = NotificationConfig.get_email_config()
    
    # Cria o serviço
    service = factory.create_notification_service("email", config)
    
    # Verifica o tipo do serviço
    assert service.__class__.__name__ == "EmailNotificationService"


def test_create_mock_notification_service():
    """Testa a criação do serviço mock"""
    # Cria a factory
    factory = NotificationConfig.create_factory()
    
    # Obtém a configuração mock
    config = NotificationConfig.get_mock_config()
    
    # Cria o serviço
    service = factory.create_notification_service("mock", config)
    
    # Verifica o tipo do serviço
    assert service.__class__.__name__ == "MockNotificationService"


def test_invalid_notification_type():
    """Testa a criação de um tipo inválido de serviço"""
    factory = NotificationConfig.create_factory()
    
    with pytest.raises(ValueError, match="Tipo de notificação não suportado"):
        factory.create_notification_service("invalid", {})


def test_notify_order_with_different_services():
    """Testa o use case com diferentes tipos de serviço"""
    # Cria a factory com logging
    factory = NotificationConfig.create_factory(with_logging=True)
    
    # Cria um pedido de teste
    order = Order(
        id="123",
        items=[
            OrderItem(
                product_id="prod1",
                quantity=2,
                price=Decimal("10.50")
            )
        ],
        total=Decimal("21.00")
    )

    # Testa com serviço mock
    mock_use_case = NotifyOrderCreatedUseCase(
        notification_factory=factory,
        notification_config=NotificationConfig.get_mock_config()
    )
    
    mock_response = mock_use_case.execute(
        NotifyOrderCreatedInput(
            order=order,
            customer_email="customer@example.com",
            customer_name="John Doe",
            notification_type="mock"
        )
    )
    assert mock_response.success is True
    
    # Verifica se a notificação foi enviada
    notifications = MockNotificationService.get_notifications_sent()
    assert len(notifications) == 1
    assert notifications[0][0].identifier == "customer@example.com" 