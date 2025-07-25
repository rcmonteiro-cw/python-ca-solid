"""
Use case para criação de usuários.
"""
import uuid
from datetime import datetime

from src.application.dto.user_dto import CreateUserInput, UserOutput
from src.domain.interfaces.use_case import UseCase, Response
from src.domain.interfaces.user_repository import UserRepository
from src.domain.entities.user import User


class CreateUserUseCase(UseCase[CreateUserInput, UserOutput]):
    """Use case para criar um novo usuário"""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, request: CreateUserInput) -> Response[UserOutput]:
        """Executa o use case de criação de usuário"""
        try:
            # Cria uma nova entidade de usuário
            user = User(
                id=str(uuid.uuid4()),
                name=request.name,
                email=request.email,
                created_at=datetime.now()
            )

            # Salva o usuário
            self.user_repository.save(user)

            # Retorna o DTO de saída
            return Response(
                success=True,
                data=UserOutput.from_entity(user)
            )

        except ValueError as e:
            return Response(
                success=False,
                error=str(e)
            ) 