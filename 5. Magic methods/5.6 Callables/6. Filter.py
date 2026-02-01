"""
Реализуйте класс Filter, описывающий объект для фильтрации элементов итерируемых объектов.
    При создании экземпляра класс должен принимать один аргумент:
        predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Экземпляр класса Filter должен являться вызываемым объектом и принимать один аргумент:
    iterable — итерируемый объект
Экземпляр класса Filter должен возвращать список, элементами которого являются элементы итерируемого объекта iterable,
    для которых функция predicate вернула значение True.
"""


class Filter:
    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))

if __name__ == '__main__':
    # test 1
    leave_even = Filter(lambda x: x % 2 == 0)
    numbers = [1, 2, 3, 4, 5, 6]

    print(leave_even(numbers))  # [2, 4, 6]
    # test 2
    more_than_five = Filter(lambda x: x > 5)
    numbers = [13, 1, 4, 10, 10, 7]

    print(more_than_five(numbers))  # [13, 10, 10, 7]
