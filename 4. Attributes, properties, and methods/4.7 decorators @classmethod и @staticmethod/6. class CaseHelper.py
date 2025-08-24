"""
Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case.
При создании экземпляра класс не должен принимать никаких аргументов.
Класс CaseHelper должен иметь четыре статических метода:
    is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True,
        если переданная строка записана в стиле Snake Case, или False в противном случае
    is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True,
        если переданная строка записана в стиле Upper Camel Case, или False в противном случае
    to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case,
        записывает ее в стиле Snake Case и возвращает полученный результат
    to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case,
        записывает ее в стиле Upper Camel Case и возвращает полученный результат
"""


class CaseHelper:
    @staticmethod
    def is_snake(text):
        for char in text:
            if char.isupper() or char in ' -':
                return False
        return True

    @staticmethod
    def is_upper_camel(text):
        for char in text:
            if char.islower() or char in ' -_':
                return False
            return True

    @staticmethod
    def to_snake(text):
        return ''.join('_' + char.lower() if char.isupper() else char for char in text).lstrip('_')

    @staticmethod
    def to_upper_camel(text):
        return text.title().replace('_', '')


print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))
print(CaseHelper.to_snake('Beegeek'))  # beegeek
print(CaseHelper.to_snake('BeeGeek'))  # bee_geek
print(CaseHelper.to_upper_camel('beegeek'))  # Beegeek
print(CaseHelper.to_upper_camel('bee_geek'))  # BeeGeek
