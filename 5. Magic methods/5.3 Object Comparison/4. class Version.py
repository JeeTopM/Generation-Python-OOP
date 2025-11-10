"""
Класс Version
Реализуйте класс Version, описывающий версию программного обеспечения.
При создании экземпляра класс должен принимать один аргумент:
    version — строка из трех целых чисел, разделенных точками и описывающих версию ПО.
    Например, 2.8.1. Если одно из чисел не указано, оно считается равным нулю.
    Например, версия 2 равнозначна версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0
Экземпляр класса Version должен иметь следующее формальное строковое представление:
Version('<версия ПО в виде трех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:
<версия ПО в виде трех целых чисел, разделенных точками>
Также экземпляры класса Version должны поддерживать между собой все операции сравнения
с помощью операторов ==, !=, >, <, >=, <=. Два Version объекта считаются равными,
если все три числа в их версиях совпадают.
Version объект считается больше другого Version объекта, если первое число в его версии больше.
Или если второе число в его версии больше, если первые числа совпадают.
Или если третье число в его версии больше, если первые и вторые числа совпадают.
"""
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, number):
        self.number = [int(i) for i in number.split('.')]
        while len(self.number) < 3:
            self.number.append(0)

    def __repr__(self):
        return f"Version('{".".join([str(i) for i in self.number])}')"

    def __str__(self):
        return f'{".".join([str(i) for i in self.number])}'

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.number == other.number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.number < other.number
        return NotImplemented

# test 1
print(Version('3.0.3') == Version('1.11.28')) # False
print(Version('3.0.3') < Version('1.11.28')) # False
print(Version('3.0.3') > Version('1.11.28')) # True
print(Version('3.0.3') <= Version('1.11.28')) # False
print(Version('3.0.3') >= Version('1.11.28')) # True

# test 2
print(Version('3') == Version('3.0')) # True
print(Version('3') == Version('3.0.0'))# True
print(Version('3.0') == Version('3.0.0'))# True

# test 3
versions = [Version('2'), Version('2.1'), Version('1.9.1')]
print(sorted(versions)) # [Version('1.9.1'), Version('2.0.0'), Version('2.1.0')]
print(min(versions)) # 1.9.1
print(max(versions)) # 2.1.0
