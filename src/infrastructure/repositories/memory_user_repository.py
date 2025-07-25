"""
Implementação em memória do UserRepository.
"""
from typing import Dict, List, Optional

from src.domain.entities.user import User
from src.domain.interfaces.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    """Implementação em memória do repositório de usuários"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}

    def save(self, user: User) -> None:
        """Salva um usuário na memória"""
        self.users[user.id] = user

    def find_by_id(self, user_id: str) -> Optional[User]:
        """Busca um usuário por ID na memória"""
        return self.users.get(user_id)

    def find_all(self) -> List[User]:
        """Retorna todos os usuários"""
        return list(self.users.values())

    def delete(self, user_id: str) -> None:
        """Remove um usuário da memória"""
        if user_id in self.users:
            del self.users[user_id] 