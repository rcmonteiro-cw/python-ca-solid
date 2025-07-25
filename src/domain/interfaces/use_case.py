"""
Interface base para todos os use cases da aplicação.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")


@dataclass
class Response(Generic[OutputType]):
    """Classe base para respostas dos use cases"""
    success: bool
    data: OutputType | None = None
    error: str | None = None


class UseCase(Generic[InputType, OutputType], ABC):
    """Interface base para todos os use cases"""
    
    @abstractmethod
    def execute(self, request: InputType) -> Response[OutputType]:
        """Executa o use case"""
        pass 