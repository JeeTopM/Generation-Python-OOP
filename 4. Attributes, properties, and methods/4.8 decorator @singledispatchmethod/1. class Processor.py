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


class Processor:
    @staticmethod
    def process(data):
        if isinstance(data, (int, float)):
            return data * 2
        elif isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return sorted(data)
        elif isinstance(data, tuple):
            return tuple(sorted(data))
        raise TypeError('Аргумент переданного типа не поддерживается')
