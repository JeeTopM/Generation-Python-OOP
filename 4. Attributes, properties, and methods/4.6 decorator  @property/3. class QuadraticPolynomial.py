"""
Класс QuadraticPolynomial

Квадратный трехчлен – это многочлен вида ax2+bx+c, где a ≠ 0.
Значение переменной x, при котором квадратный трехчлен обращается в ноль, называют его корнем.
Квадратный трехчлен может иметь один корень, два корня или вовсе не иметь корней.
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена

Класс QuadraticPolynomial должен иметь четыре свойства:
    x1 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена
    x2 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена
    view — свойство, доступное только для чтения
    coefficients — свойство, доступное для чтения и записи
"""
import math


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @property
    def x1(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return (-self.b - math.sqrt(d)) / (2 * self.a) if d >= 0 else None

    @property
    def x2(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return (-self.b + math.sqrt(d)) / (2 * self.a) if d >= 0 else None

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, coeffs):
        self.a, self.b, self.c = coeffs


# test 1
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)  # 1
print(polynom.b)  # 2
print(polynom.c)  # -3

# test 2
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)  # -3.0
print(polynom.x2)  # 1.0
