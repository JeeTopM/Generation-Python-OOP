'''
Класс Rectangle
Вам доступен класс Rectangle, описывающий прямоугольник. При создании экземпляра класс принимает два аргумента в следующем порядке:
    length — длина прямоугольника
    width — ширина прямоугольника
Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:
    Rectangle(<длина прямоугольника>, <ширина прямоугольника>)
'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


# 1
rectangle = Rectangle(1, 2)
print(str(rectangle))  # Rectangle(1, 2)
print(repr(rectangle))  # Rectangle(1, 2)

# 2
rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)
print(rectangle1)  # Rectangle(1, 2)
print(repr(rectangle2))  # Rectangle(3, 4)
