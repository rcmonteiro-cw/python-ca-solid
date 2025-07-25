"""
Entidades de domínio relacionadas a pedidos.
"""
from dataclasses import dataclass
from decimal import Decimal
from typing import List


@dataclass
class OrderItem:
    """Item do pedido"""
    product_id: str
    quantity: int
    price: Decimal

    def calculate_total(self) -> Decimal:
        """Calcula o total do item"""
        return self.price * Decimal(self.quantity)


@dataclass
class Order:
    """Pedido"""
    id: str
    items: List[OrderItem]
    total: Decimal

    def calculate_total(self) -> None:
        """Calcula o total do pedido"""
        self.total = sum(item.calculate_total() for item in self.items)

    def validate(self) -> None:
        """Valida o pedido"""
        if not self.items:
            raise ValueError("Pedido deve ter pelo menos um item")
        if any(item.quantity <= 0 for item in self.items):
            raise ValueError("Quantidade de itens deve ser maior que zero")
        if any(item.price <= 0 for item in self.items):
            raise ValueError("Preço dos itens deve ser maior que zero") 