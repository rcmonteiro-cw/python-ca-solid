"""
Este módulo demonstra o Open/Closed Principle (OCP).
Novas formas de pagamento podem ser adicionadas sem modificar o código existente.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PaymentInfo:
    """Informações do pagamento"""
    amount: Decimal
    currency: str
    description: str


class PaymentProcessor(ABC):
    """Interface base para processadores de pagamento"""
    
    @abstractmethod
    def process_payment(self, payment: PaymentInfo) -> bool:
        """Processa um pagamento"""
        pass


class CreditCardProcessor(PaymentProcessor):
    """Processador de pagamentos com cartão de crédito"""
    
    def process_payment(self, payment: PaymentInfo) -> bool:
        """Processa pagamento com cartão de crédito"""
        print(f"Processando pagamento com cartão de crédito: {payment}")
        return True


class PayPalProcessor(PaymentProcessor):
    """Processador de pagamentos com PayPal"""
    
    def process_payment(self, payment: PaymentInfo) -> bool:
        """Processa pagamento com PayPal"""
        print(f"Processando pagamento com PayPal: {payment}")
        return True


class PixProcessor(PaymentProcessor):
    """Processador de pagamentos com Pix"""
    
    def process_payment(self, payment: PaymentInfo) -> bool:
        """Processa pagamento com Pix"""
        print(f"Processando pagamento com Pix: {payment}")
        return True 