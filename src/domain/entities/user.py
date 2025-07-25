"""
Este módulo demonstra o Single Responsibility Principle (SRP).
Cada classe tem uma única responsabilidade.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    """Entidade User - responsável apenas por manter os dados do usuário"""
    id: str
    name: str
    email: str
    created_at: datetime

    def __post_init__(self):
        self.validate()

    def validate(self) -> None:
        """Valida os dados do usuário"""
        if not self.name:
            raise ValueError("Nome do usuário não pode estar vazio")
        if not self.email or "@" not in self.email:
            raise ValueError("Email inválido") 