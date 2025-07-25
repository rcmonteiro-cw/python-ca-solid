"""
Controller para operações de usuário.
"""
from dataclasses import asdict

from src.application.dto.user_dto import CreateUserInput
from src.application.use_cases.create_user_use_case import CreateUserUseCase
from src.application.use_cases.list_users_use_case import ListUsersUseCase, ListUsersInput
from src.infrastructure.repositories.memory_user_repository import InMemoryUserRepository


class UserController:
    """Controller para operações de usuário"""

    def __init__(self):
        # Inicializa o repositório
        self.user_repository = InMemoryUserRepository()
        
        # Inicializa os use cases
        self.create_user_use_case = CreateUserUseCase(self.user_repository)
        self.list_users_use_case = ListUsersUseCase(self.user_repository)

    def create_user(self, name: str, email: str) -> dict:
        """
        Cria um novo usuário
        
        Args:
            name: Nome do usuário
            email: Email do usuário
            
        Returns:
            dict: Resposta do use case
        """
        # Cria o DTO de entrada
        input_dto = CreateUserInput(name=name, email=email)
        
        # Executa o use case
        response = self.create_user_use_case.execute(input_dto)
        
        # Converte a resposta para dict
        if response.success and response.data:
            return {
                "success": True,
                "data": asdict(response.data)
            }
        else:
            return {
                "success": False,
                "error": response.error
            }

    def list_users(self) -> dict:
        """
        Lista todos os usuários
        
        Returns:
            dict: Lista de usuários
        """
        # Executa o use case
        response = self.list_users_use_case.execute(ListUsersInput())
        
        # Converte a resposta para dict
        if response.success and response.data:
            return {
                "success": True,
                "data": {
                    "users": [asdict(user) for user in response.data.users]
                }
            }
        else:
            return {
                "success": False,
                "error": response.error
            } 