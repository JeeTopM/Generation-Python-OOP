"""
Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия.
При создании экземпляра класс должен принимать один аргумент:
    temperature — температура в градусах по шкале Цельсия
Класс Temperature должен иметь один метод экземпляра:
    to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта

Класс Temperature должен иметь один метод класса:
    from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта
        и возвращающий экземпляр класса Temperature, созданный на основе переданной температуры
Экземпляр класса Temperature должен иметь следующее неформальное строковое представление:
    <температура в градусах по шкале Цельсия с округлением до двух знаков после запятой>°C
Также экземпляр класса Temperature должен поддерживать приведение к типам bool, int и float:
    при приведении к типу bool значением экземпляра класса Temperature должно являться значение True,
        если его температура выше нуля, или False в противном случае
    при приведении к типу int значением экземпляра класса Temperature должна являться его температура
        в виде целого числа с отброшенной дробной частью
    при приведении к типу float значением экземпляра класса Temperature должна являться его температура
        в виде вещественного числа
"""


class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    def __str__(self):
        return str(round(self.temperature, 2)) + '°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

    @classmethod
    def from_fahrenheit(cls, val):
        cel = (5 / 9) * (val - 32)
        return cls(cel)


if __name__ == '__main__':
    # 1
    t = Temperature(5.5)
    print(t)  # 5.5°C
    print(int(t))  # 5
    print(float(t))  # 5.5
    print(t.to_fahrenheit())  # 41.9

    # 2
    t1 = Temperature(1)
    t2 = Temperature(0)
    t3 = Temperature(-1)
    print(bool(t1))  # True
    print(bool(t2))  # False
    print(bool(t3))  # False

    # 3
    t = Temperature.from_fahrenheit(41)
    print(t)  # 5.0°C
    print(int(t))  # 5
    print(float(t))  # 5.0
    print(t.to_fahrenheit())  # 41.0

    # 4
    t = Temperature.from_fahrenheit(-459.67)
    print(t)  # -273.15°C
    print(bool(t))  # False
    print(int(t))  # -273
    print(f'{float(t):.2f}')  # -273.15
    print(f'{t.to_fahrenheit():.2f}')  # -459.67
