"""
Interface para o repositório de pedidos.
"""
from typing import Protocol, Optional

from src.domain.entities.order import Order


class OrderRepository(Protocol):
    """Interface para repositório de pedidos"""
    
    def save(self, order: Order) -> None:
        """Salva um pedido"""
        pass

    def find_by_id(self, order_id: str) -> Optional[Order]:
        """Busca um pedido por ID"""
        pass 