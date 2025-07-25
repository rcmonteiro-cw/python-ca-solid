"""
DTOs para operações relacionadas a usuários.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.domain.entities.user import User


@dataclass
class CreateUserInput:
    """DTO para criação de usuário"""
    name: str
    email: str


@dataclass
class UserOutput:
    """DTO para saída de dados do usuário"""
    id: str
    name: str
    email: str
    created_at: datetime

    @classmethod
    def from_entity(cls, user: User) -> "UserOutput":
        """Cria um DTO a partir de uma entidade"""
        return cls(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at
        )


@dataclass
class ListUsersOutput:
    """DTO para listar usuários"""
    users: List[UserOutput]

    @classmethod
    def from_entities(cls, users: List[User]) -> "ListUsersOutput":
        """Cria um DTO a partir de uma lista de entidades"""
        return cls(
            users=[UserOutput.from_entity(user) for user in users]
        ) 