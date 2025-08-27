'''
Класс Processor
Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.
Класс Processor имеет один статический метод:
    process() — метод, который принимает в качестве аргумента произвольный объект,
    преобразует его в зависимости от его типа и возвращает полученный результат.
    Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
        Аргумент переданного типа не поддерживается
Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod,
    чтобы он выполнял ту же задачу.
'''
from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int | float)
    @staticmethod
    def _from_int(arg):
        return arg * 2

    @process.register(str)
    @staticmethod
    def _from_str(arg):
        return arg.upper()

    @process.register(list)
    @staticmethod
    def _from_list(arg):
        return sorted(arg)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(arg):
        return tuple(sorted(arg))


# test 1
print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))
''' 20
    10.4
    HELLO
    (1, 2, 3, 4)
    [1, 2, 3]'''
# test 2
try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)
'''Аргумент переданного типа не поддерживается'''
