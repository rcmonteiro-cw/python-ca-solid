"""
Use case para listar usuários.
"""
from dataclasses import dataclass

from src.application.dto.user_dto import ListUsersOutput
from src.domain.interfaces.use_case import UseCase, Response
from src.domain.interfaces.user_repository import UserRepository


@dataclass
class ListUsersInput:
    """DTO vazio para entrada do use case de listar usuários"""
    pass


class ListUsersUseCase(UseCase[ListUsersInput, ListUsersOutput]):
    """Use case para listar todos os usuários"""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, request: ListUsersInput) -> Response[ListUsersOutput]:
        """Executa o use case de listar usuários"""
        try:
            # Busca todos os usuários
            users = self.user_repository.find_all()

            # Retorna o DTO de saída
            return Response(
                success=True,
                data=ListUsersOutput.from_entities(users)
            )

        except Exception as e:
            return Response(
                success=False,
                error=str(e)
            ) 