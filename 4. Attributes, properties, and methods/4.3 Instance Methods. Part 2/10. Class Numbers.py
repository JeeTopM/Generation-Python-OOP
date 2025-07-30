"""
Класс Numbers

Реализуйте класс Numbers, описывающий изначально пустой расширяемый набор целых чисел.
При создании экземпляра класс не должен принимать никаких аргументов.
Класс Numbers должен иметь три метода экземпляра:
    add_number() — метод, принимающий в качестве аргумента целое число и добавляющий его в набор
    get_even() — метод, возвращающий список всех четных чисел из набора
    get_odd() — метод, возвращающий список всех нечетных чисел из набора
"""


class Numbers:
    def __init__(self):
        self.list = []

    def add_number(self, num):
        self.list.append(num)

    def get_even(self):
        even = [n for n in self.list if n % 2 == 0]
        return even

    def get_odd(self):
        odd = [n for n in self.list if n % 2 != 0]
        return odd


# 1
numbers = Numbers()
print(numbers.get_even())  # []
print(numbers.get_odd())  # []

# 2
numbers = Numbers()
numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)
print(numbers.get_even())  # [2, 4]
print(numbers.get_odd())  # [3, 1]

# 3
numbers = Numbers()
numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)
print(numbers.get_even())  # []
print(numbers.get_odd())  # [1, 3, 1]
