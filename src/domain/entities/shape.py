"""
Este módulo demonstra o Liskov Substitution Principle (LSP).
As classes derivadas podem ser usadas em qualquer lugar onde a classe base é esperada.
"""
from abc import ABC, abstractmethod
import math
from typing import Protocol


class Shape(Protocol):
    """Protocolo para formas geométricas"""
    
    def area(self) -> float:
        """Calcula a área da forma"""
        pass

    def perimeter(self) -> float:
        """Calcula o perímetro da forma"""
        pass


class Rectangle:
    """Implementação de um retângulo"""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calcula a área do retângulo"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calcula o perímetro do retângulo"""
        return 2 * (self.width + self.height)


class Square:
    """Implementação de um quadrado"""
    
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        """Calcula a área do quadrado"""
        return self.side ** 2

    def perimeter(self) -> float:
        """Calcula o perímetro do quadrado"""
        return 4 * self.side


class Circle:
    """Implementação de um círculo"""
    
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Calcula a área do círculo"""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Calcula o perímetro do círculo"""
        return 2 * math.pi * self.radius


def print_shape_info(shape: Shape) -> None:
    """
    Função que demonstra o LSP - pode receber qualquer forma
    que implemente o protocolo Shape
    """
    print(f"Área: {shape.area():.2f}")
    print(f"Perímetro: {shape.perimeter():.2f}") 