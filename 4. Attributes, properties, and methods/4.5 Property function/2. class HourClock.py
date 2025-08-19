"""
Класс HourClock
Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой.
При создании экземпляра класс должен принимать один аргумент:
hours — количество часов. Если hours не является целым числом, принадлежащим диапазону [1; 12],
        должно быть возбуждено исключение ValueError с текстом:
        Некорректное время
Класс HourClock должен иметь одно свойство:
hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов.
При изменении свойство должно проверять, что новое значение является целым числом, принадлежащим диапазону [1; 12],
        в противном случае должно быть возбуждено исключение ValueError с текстом:
        Некорректное время
"""


class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if isinstance(hours, int) and 0 < hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)


# test 1
time = HourClock(7)
print(time.hours)  # 7
time.hours = 9
print(time.hours)  # 9

# test 2
time = HourClock(7)
try:
    time.hours = 15
except ValueError as e:
    print(e)
# Некорректное время

# test 3
try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)
# Некорректное время
