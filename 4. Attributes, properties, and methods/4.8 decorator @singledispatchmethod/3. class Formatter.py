"""
Класс Formatter

Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Formatter должен иметь один статический метод:
    format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict
    и выводящий информацию о переданном объекте в формате, зависящем от его типа.
    Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
        Аргумент переданного типа не поддерживается
"""
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register
    @staticmethod
    def format_int(data: int):
        print(f'Целое число: {data}')

    @format.register
    @staticmethod
    def format_int(data: float):
        print(f'Вещественное число: {data}')

    @format.register
    @staticmethod
    def format_int(data: tuple):
        print(f'Элементы кортежа: {", ".join(str(x) for x in data)}')

    @format.register
    @staticmethod
    def format_int(data: list):
        print(f'Элементы списка: {", ".join(str(x) for x in data)}')

    @format.register
    @staticmethod
    def format_int(data: dict):
        print(f'Пары словаря: {", ".join(str(x) for x in data.items())}')


# test 1
Formatter.format(1337)  # Целое число: 1337

Formatter.format(20.77)  # Вещественное число: 20.77

# test 2
Formatter.format([10, 20, 30, 40, 50])  # Элементы списка: 10, 20, 30, 40, 50
Formatter.format(([1, 3], [2, 4, 6]))  # Элементы кортежа: [1, 3], [2, 4, 6]

# test 3
Formatter.format({'Cuphead': 1, 'Mugman': 3})  # Пары словаря: ('Cuphead', 1), ('Mugman', 3)
Formatter.format({1: 'one', 2: 'two'})  # Пары словаря: (1, 'one'), (2, 'two')
Formatter.format({1: True, 0: False})  # Пары словаря: (1, True), (0, False)

# test 4
try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
# Аргумент переданного типа не поддерживается
