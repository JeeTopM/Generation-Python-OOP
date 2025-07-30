"""
Класс Vector

Реализуйте класс Vector, описывающий вектор на плоскости.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    x — координата вектора по оси x, по умолчанию имеет значение 0
    y — координата вектора по оси y, по умолчанию имеет значение 0
Экземпляр класса Vector должен иметь два атрибута:
    x — координата вектора по оси x
    y — координата вектора по оси y
Класс Vector должен иметь один метод экземпляра:
    abs() — метод, возвращающий модуль вектора
"""

from math import sqrt


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))


# 1
vector = Vector()
print(vector.x, vector.y)  # 0 0
print(vector.abs())  # 0.0

# 2
vector = Vector(3, 4)
print(vector.x, vector.y)  # 3 4
print(vector.abs())  # 5.0
