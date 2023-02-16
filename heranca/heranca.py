# Crie a classe Polygon com um construtor que recebe “sides: List[float]” e um método “display_sides() -> List[float]”.
# Crie também a classe Triangle que herda o Polygon e implementa o “find_area() -> float”.
from typing import List
from math import sqrt


class Polygon:
    def __init__(self, sides: List[float]):
        self.sides = sides

    def display_sides(self) -> List[float]:
        try:
            if len(self.sides) == 3:
                return self.sides
            else:
                raise Exception("Por favor, digite apenas 3 lados.")
        except Exception as error:
            return error


class Triangle(Polygon):
    def find_area(self) -> float:
        a, b, c = self.sides
        semiperimeter = (a + b + c) / 2
        area = sqrt(semiperimeter * (semiperimeter - a) *
                    (semiperimeter - b) * (semiperimeter - c))
        return f"A área do triangulo é: {round(area, 2)}"


poligono = Polygon([2, 3, 4, 5])
poligono_display = poligono.display_sides()
area_triangulo = Triangle([2, 3, 4]).find_area()

print(area_triangulo)
