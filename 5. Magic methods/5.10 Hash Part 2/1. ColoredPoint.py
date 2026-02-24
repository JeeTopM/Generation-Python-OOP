'''
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    x — координата точки по оси x
    y — координата точки по оси y
    color — цвет точки
Класс ColoredPoint должен иметь три свойства:
    x — свойство, доступное только для чтения, возвращающее координату точки по оси x
    y — свойство, доступное только для чтения, возвращающее координату точки по оси y
    color — свойство, доступное только для чтения, возвращающее цвет точки
Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:
    ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения с помощью операторов == и !=.
Две цветные точки считаются равными, если их цвета и координаты по обеим осям совпадают.
Наконец, при передаче экземпляра класса ColoredPoint в функцию hash() должно возвращаться его хеш-значение,
    вычисленное с помощью функции hash() на основе кортежа,
    первым элементом которого является координата точки по оси x,
    вторым — координата точки по оси y,
    третьим — цвет точки.
'''
class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @property
    def _fields(self):
        return self._x, self._y, self._color

    def __repr__(self):
        return "ColoredPoint({}, {}, '{}')".format(*self._fields)

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

if __name__ == '__main__':
    # test 1
    point1 = ColoredPoint(1, 2, 'white')
    point2 = ColoredPoint(1, 2, 'white')
    point3 = ColoredPoint(3, 4, 'black')
    print(point1 == point2)  # True
    print(hash(point1) == hash(point2))  # True
    print(point1 == point3)  # False
    print(hash(point1) == hash(point3))  # False

    # test 2
    points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}
    print(points)  # {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

    # test 3
    point = ColoredPoint(1, 2, 'white')
    try:
        point.color = 'black'
    except AttributeError as e:
        print('Error')  # Error
