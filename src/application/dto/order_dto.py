"""
DTOs para operações relacionadas a pedidos.
"""
from dataclasses import dataclass
from decimal import Decimal
from typing import List

from src.domain.entities.order import Order, OrderItem


@dataclass
class OrderItemInput:
    """DTO para entrada de item do pedido"""
    product_id: str
    quantity: int
    price: Decimal


@dataclass
class CreateOrderInput:
    """DTO para criação de pedido"""
    items: List[OrderItemInput]


@dataclass
class OrderItemOutput:
    """DTO para saída de item do pedido"""
    product_id: str
    quantity: int
    price: Decimal

    @classmethod
    def from_entity(cls, item: OrderItem) -> "OrderItemOutput":
        """Cria um DTO a partir de uma entidade"""
        return cls(
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )


@dataclass
class OrderOutput:
    """DTO para saída de pedido"""
    id: str
    items: List[OrderItemOutput]
    total: Decimal

    @classmethod
    def from_entity(cls, order: Order) -> "OrderOutput":
        """Cria um DTO a partir de uma entidade"""
        return cls(
            id=order.id,
            items=[OrderItemOutput.from_entity(item) for item in order.items],
            total=order.total
        ) 