"""
Класс Rectangle

Реализуйте класс Rectangle, описывающий прямоугольник.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    length — длина прямоугольника
    width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:
    length — длина прямоугольника
    width — ширина прямоугольника
Класс Rectangle должен иметь два свойства:
    perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
    area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)

# 1
rectangle = Rectangle(4, 5)
print(rectangle.length) # 4
print(rectangle.width) # 5
print(rectangle.perimeter) # 18
print(rectangle.area) # 20

print()
# 2
rectangle = Rectangle(4, 5)
rectangle.length = 2
rectangle.width = 3
print(rectangle.length) # 2
print(rectangle.width) # 3
print(rectangle.perimeter) # 10
print(rectangle.area)# 6

