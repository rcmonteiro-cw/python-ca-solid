"""
Testes para os use cases de usuário.
"""
import pytest

from src.presentation.controllers.user_controller import UserController


def test_create_user_success():
    """Testa a criação de um usuário com sucesso"""
    controller = UserController()
    
    # Cria um usuário
    response = controller.create_user(
        name="John Doe",
        email="john@example.com"
    )
    
    # Verifica o sucesso
    assert response["success"] is True
    assert response["data"]["name"] == "John Doe"
    assert response["data"]["email"] == "john@example.com"


def test_create_user_invalid_email():
    """Testa a criação de um usuário com email inválido"""
    controller = UserController()
    
    # Tenta criar um usuário com email inválido
    response = controller.create_user(
        name="John Doe",
        email="invalid-email"
    )
    
    # Verifica a falha
    assert response["success"] is False
    assert "Email inválido" in response["error"]


def test_list_users():
    """Testa a listagem de usuários"""
    controller = UserController()
    
    # Cria alguns usuários
    controller.create_user("John Doe", "john@example.com")
    controller.create_user("Jane Doe", "jane@example.com")
    
    # Lista os usuários
    response = controller.list_users()
    
    # Verifica o sucesso
    assert response["success"] is True
    assert len(response["data"]["users"]) == 2
    
    # Verifica os dados dos usuários
    users = response["data"]["users"]
    assert any(user["name"] == "John Doe" for user in users)
    assert any(user["name"] == "Jane Doe" for user in users) 