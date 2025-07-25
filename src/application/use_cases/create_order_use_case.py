"""
Use case para criação de pedidos.
"""
import uuid
from decimal import Decimal

from src.application.dto.order_dto import CreateOrderInput, OrderOutput
from src.domain.interfaces.order_repository import OrderRepository
from src.domain.interfaces.use_case import UseCase, Response
from src.domain.entities.order import Order, OrderItem
from src.domain.entities.payment import PaymentProcessor, PaymentInfo


class CreateOrderUseCase(UseCase[CreateOrderInput, OrderOutput]):
    """Use case para criar um novo pedido"""

    def __init__(
        self,
        order_repository: OrderRepository,
        payment_processor: PaymentProcessor
    ):
        self.order_repository = order_repository
        self.payment_processor = payment_processor

    def execute(self, request: CreateOrderInput) -> Response[OrderOutput]:
        """Executa o use case de criação de pedido"""
        try:
            # Converte os DTOs de entrada em entidades
            order_items = [
                OrderItem(
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=item.price
                )
                for item in request.items
            ]

            # Cria o pedido
            order = Order(
                id=str(uuid.uuid4()),
                items=order_items,
                total=Decimal(0)
            )

            # Calcula o total e valida o pedido
            order.calculate_total()
            order.validate()

            # Processa o pagamento
            payment = PaymentInfo(
                amount=order.total,
                currency="BRL",
                description=f"Pedido {order.id}"
            )

            if not self.payment_processor.process_payment(payment):
                return Response(
                    success=False,
                    error="Falha no processamento do pagamento"
                )

            # Salva o pedido
            self.order_repository.save(order)

            # Retorna o DTO de saída
            return Response(
                success=True,
                data=OrderOutput.from_entity(order)
            )

        except ValueError as e:
            return Response(
                success=False,
                error=str(e)
            )
        except Exception as e:
            return Response(
                success=False,
                error=f"Erro ao criar pedido: {str(e)}"
            ) 