"""
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена
Класс QuadraticPolynomial должен иметь два метода класса:
    from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c,
        которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса QuadraticPolynomial,
        созданный на основе переданных коэффициентов
    from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты a, b и c
        квадратного трехчлена, записанные через пробел. Метод должен возвращать экземпляр класса QuadraticPolynomial,
        созданный на основе переданных коэффициентов, предварительно преобразованных в экземпляры класса float
"""
from os.path import split


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string):
        res = (float(i) for i in string.split())
        return cls.from_iterable(res)


# test 1
polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)  # 1
print(polynom.b)  # -5
print(polynom.c)  # 6

# test 2
polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)  # 2
print(polynom.b)  # 13
print(polynom.c)  # -1

# test 3
polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)  # -1.5
print(polynom.b)  # 4.0
print(polynom.c)  # 14.8
print(polynom.a + polynom.b + polynom.c)  # 17.3
