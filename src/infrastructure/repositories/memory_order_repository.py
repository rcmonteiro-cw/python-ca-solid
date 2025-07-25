"""
Implementação em memória do OrderRepository.
"""
from typing import Dict, Optional

from src.domain.interfaces.order_repository import OrderRepository
from src.domain.order import Order


class InMemoryOrderRepository(OrderRepository):
    """Implementação em memória do repositório de pedidos"""
    
    def __init__(self):
        self.orders: Dict[str, Order] = {}

    def save(self, order: Order) -> None:
        """Salva um pedido na memória"""
        self.orders[order.id] = order

    def find_by_id(self, order_id: str) -> Optional[Order]:
        """Busca um pedido por ID na memória"""
        return self.orders.get(order_id) 