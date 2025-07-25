"""
Interface para o repositório de usuários.
"""
from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.user import User


class UserRepository(ABC):
    """Interface para operações de repositório de usuários"""
    
    @abstractmethod
    def save(self, user: User) -> None:
        """Salva um usuário"""
        pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> Optional[User]:
        """Busca um usuário por ID"""
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        """Retorna todos os usuários"""
        pass

    @abstractmethod
    def delete(self, user_id: str) -> None:
        """Remove um usuário"""
        pass 