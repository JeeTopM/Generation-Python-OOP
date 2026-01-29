"""
Реализуйте класс RaiseTo, экземпляры которого позволяют возводить числа в фиксированную степень.
    При создании экземпляра класс должен принимать один аргумент:
        degree — показатель степени
Экземпляр класса RaiseTo должен являться вызываемым объектом и принимать один аргумент:
    x — число
Экземпляр класса RaiseTo должен возвращать значение x в степени degree.
"""


class RaiseTo:
    pass


if __name__ == '__main__':
    # Test 1
    raise_to_two = RaiseTo(2)

    print(raise_to_two(2))  # 4
    print(raise_to_two(3))  # 9
    print(raise_to_two(4))  # 16

    # Test 2
    raise_to_three = RaiseTo(3)
    raise_to_four = RaiseTo(4)

    print(raise_to_three(3))  # 27
    print(raise_to_four(2))  # 16
