from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2
