'''
Класс IPAddress
IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете или локальной сети.
IP-адреса представляют собой набор из четырех целых чисел, разделенных точками. Например, 192.158.1.38.
Каждое число в наборе принадлежит интервалу от 0 до 255.
Таким образом, полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.
Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра класс должен принимать один аргумент:
    ipaddress — IP-адрес, представленный в одном из следующих вариантов:
        1. строка из четырех целых чисел, разделенных точками
        2. список или кортеж из четырех целых чисел
Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:
    IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:
    <IP-адрес в виде четырех целых чисел, разделенных точками>
'''
from functools import singledispatchmethod

class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list | tuple)
    def _(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

# 1
ip = IPAddress('8.8.1.1')
print(str(ip))  # 8.8.1.1
print(repr(ip))  # IPAddress('8.8.1.1')

# 2
ip = IPAddress([1, 1, 10, 10])
print(str(ip))  # 1.1.10.10
print(repr(ip))  # IPAddress('1.1.10.10')

# 3
ip = IPAddress((1, 1, 11, 11))
print(str(ip))  # 1.1.11.11
print(repr(ip))  # IPAddress('1.1.11.11')
