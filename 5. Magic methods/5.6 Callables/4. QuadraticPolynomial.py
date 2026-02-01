"""
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
    При создании экземпляра класс должен принимать три аргумента в следующем порядке:
        a — коэффициент a квадратного трехчлена
        b — коэффициент b квадратного трехчлена
        c — коэффициент c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен являться вызываемым объектом и принимать один аргумент:
    x  — число
Экземпляр класса QuadraticPolynomial должен возвращать значение выражения
    ax2+bx+c, где a,b и c — коэффициенты квадратного трехчлена.
"""


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


if __name__ == '__main__':
    func = QuadraticPolynomial(1, 2, 1)

    print(func(1))  # 4
    print(func(2))  # 9

    func = QuadraticPolynomial(1, 3, 4)

    print(func(1))  # 8
    print(func(2))  # 14
