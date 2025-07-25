"""
Controller para operações de pedido.
"""
from dataclasses import asdict
from decimal import Decimal
from typing import List

from src.application.dto.order_dto import CreateOrderInput, OrderItemInput
from src.application.use_cases.create_order_use_case import CreateOrderUseCase
from src.domain.payment import CreditCardProcessor
from src.infrastructure.repositories.memory_order_repository import InMemoryOrderRepository


class OrderController:
    """Controller para operações de pedido"""

    def __init__(self):
        # Inicializa o repositório e o processador de pagamento
        self.order_repository = InMemoryOrderRepository()
        self.payment_processor = CreditCardProcessor()
        
        # Inicializa os use cases
        self.create_order_use_case = CreateOrderUseCase(
            self.order_repository,
            self.payment_processor
        )

    def create_order(self, items: List[dict]) -> dict:
        """
        Cria um novo pedido
        
        Args:
            items: Lista de itens do pedido no formato:
                  [{"product_id": "1", "quantity": 2, "price": "10.00"}, ...]
            
        Returns:
            dict: Resposta do use case
        """
        # Converte os itens para DTOs
        order_items = [
            OrderItemInput(
                product_id=item["product_id"],
                quantity=item["quantity"],
                price=Decimal(item["price"])
            )
            for item in items
        ]
        
        # Cria o DTO de entrada
        input_dto = CreateOrderInput(items=order_items)
        
        # Executa o use case
        response = self.create_order_use_case.execute(input_dto)
        
        # Converte a resposta para dict
        if response.success and response.data:
            return {
                "success": True,
                "data": asdict(response.data)
            }
        else:
            return {
                "success": False,
                "error": response.error
            } 