"""
Класс Circle

Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
    radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:
    radius — радиус круга
    diameter — диаметр круга
    area — площадь круга
"""

# Код:
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.area = pi * self.radius**2


# тест 1
circle = Circle(1)
print(circle.radius)  # 1
# тест 2
circle = Circle(5)
print(circle.radius)  # 5
print(circle.diameter)  # 10
print(circle.area)  # 78.53981633974483
