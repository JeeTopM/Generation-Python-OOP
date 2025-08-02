"""
Класс Circle

Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
radius — радиус круга

Экземпляр класса Circle должен иметь три атрибута:
_radius — радиус круга
_diameter — диаметр круга
_area — площадь круга
"""

from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * self._radius
        self._area = pi * pow(self._radius, 2)

    def get_radius(self):
        """метод, возвращающий радиус круга"""
        return self._radius

    def get_diameter(self):
        """метод, возвращающий диаметр круга"""
        return self._diameter

    def get_area(self):
        """метод, возвращающий площадь круга"""
        return self._area


# 1
circle = Circle(1)
print(circle.get_radius())  # 1
print(circle.get_diameter())  # 2
print(round(circle.get_area()))  # 3

# 2
circle = Circle(5)
print(circle.get_radius())  # 5
print(circle.get_diameter())  # 10
print(round(circle.get_area()))  # 79
