"""
Реализуйте класс Vector, описывающий вектор на плоскости.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    x — координата вектора по оси x
    y — координата вектора по оси y
Экземпляр класса Vector должен иметь следующее неформальное строковое представление:
    (<координата x>, <координата y>)
Также экземпляр класса Vector должен поддерживать приведение к типам bool, int, float и complex:
    при приведении к типу bool значением вектора должно являться значение True,
        если хотя бы одна его координата не равна нулю, или False в противном случае
    при приведении к типу int значением вектора должен являться его модуль в виде целого числа с отброшенной дробной частью
    при приведении к типу float значением вектора должен являться его модуль в виде вещественного числа
    при приведении к типу complex значением вектора должно являться комплексное число,
        вещественная часть которого равна координате вектора по оси x, мнимая часть — координате вектора по оси y
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __float__(self):
        return float((self.x ** 2 + self.y ** 2) ** 0.5)

    def __complex__(self):
        return complex(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

if __name__ == "__main__":
    # test 1
    vector = Vector(3, 4)

    print(vector)  # (3, 4)
    print(int(vector))  # 5
    print(float(vector))  # 5.0
    print(complex(vector))  # (3+4j)

    # test 2
    print(bool(Vector(1, 2)))  # True
    print(bool(Vector(1, 0)))  # True
    print(bool(Vector(0, 1)))  # True
    print(bool(Vector(0, 0)))  # False
