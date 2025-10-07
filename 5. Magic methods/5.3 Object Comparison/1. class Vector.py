'''
Класс Vector
Реализуйте класс Vector, описывающий вектор на плоскости.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    x — координата вектора по оси x
    y — координата вектора по оси y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:
    Vector(<координата x>, <координата y>)
Также экземпляры класса Vector должны поддерживать операции сравнения с помощью операторов == и!=.
Два вектора считаются равными, если их координаты по обеим осям совпадают.
Методы, реализующие операции сравнения, должны уметь сравнивать как два вектора между собой,
так и вектор с кортежем из двух чисел, представляющих координаты x и y.
'''


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

# 1
a = Vector(1, 2)
b = Vector(1, 2)
print(a == b)  # True
print(a != b)  # False

# 2
a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)
print(a == pair1)  # True
print(a == pair2)  # False
print(a == pair3)  # False
print(a == pair4)  # False
print(a == pair5)  # False
