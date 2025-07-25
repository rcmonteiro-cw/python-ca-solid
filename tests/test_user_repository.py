"""
Testes para o repositório de usuários.
"""
from datetime import datetime
import pytest

from src.domain.entities.user import User
from src.infrastructure.repositories.memory_user_repository import InMemoryUserRepository


def test_create_user():
    """Testa a criação de um usuário válido"""
    user = User(
        id="1",
        name="John Doe",
        email="john@example.com",
        created_at=datetime.now()
    )
    assert user.name == "John Doe"
    assert user.email == "john@example.com"


def test_invalid_user_email():
    """Testa a criação de um usuário com email inválido"""
    with pytest.raises(ValueError, match="Email inválido"):
        User(
            id="1",
            name="John Doe",
            email="invalid-email",
            created_at=datetime.now()
        )


def test_user_repository():
    """Testa as operações do repositório de usuários"""
    repo = InMemoryUserRepository()
    
    # Cria um usuário
    user = User(
        id="1",
        name="John Doe",
        email="john@example.com",
        created_at=datetime.now()
    )
    
    # Salva o usuário
    repo.save(user)
    
    # Busca o usuário
    found_user = repo.find_by_id("1")
    assert found_user is not None
    assert found_user.name == "John Doe"
    
    # Lista todos os usuários
    all_users = repo.find_all()
    assert len(all_users) == 1
    assert all_users[0].id == "1"
    
    # Remove o usuário
    repo.delete("1")
    assert repo.find_by_id("1") is None 