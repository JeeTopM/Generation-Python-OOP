"""
Класс Time

Реализуйте класс Time, описывающий время на цифровых часах.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
    minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час
Экземпляр класса Time должен иметь следующее неформальное строковое представление:
    <количество часов в формате HH>:<количество минут в формате MM>
Также экземпляры класса Time должны поддерживать между собой операцию сложения с помощью операторов + и +=:
    результатом сложения с помощью оператора + должен являться новый экземпляр класса Time,
        количество часов которого равно сумме часов исходных экземпляров класса Time,
        количество минут — сумме минут исходных экземпляров класса Time
    результатом сложения с помощью оператора += должен являться левый экземпляр класса Time,
        количество часов которого увеличено на количество часов правого экземпляра класса Time,
        количество минут — на количество минут правого экземпляра класса Time
"""
class Time:
    def __init__(self, hours, minutes):
        total_minutes = hours * 60 + minutes
        self.hours = (total_minutes // 60) % 24
        self.minutes = total_minutes % 60

    def __repr__(self):
        return f"Time({self.hours}, {self.minutes})"

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            temp = Time(self.hours + other.hours, self.minutes + other.minutes)
            self.hours = temp.hours
            self.minutes = temp.minutes
            return self
        return NotImplemented

if __name__ == '__main__':
    # 1
    time1 = Time(2, 30)
    time2 = Time(3, 10)

    print(time1 + time2) # 05:40
    print(time2 + time1) # 05:40

    # 2
    time1 = Time(2, 30)
    time2 = Time(3, 10)

    time1 += time2

    print(time1) # 05:40
    print(time2) # 03:10

    # 3
    time1 = Time(25, 20)
    time2 = Time(10, 130)

    print(time1) # 01:20
    print(time2) # 12:10

    # 4
    t1 = Time(15, 50)
    t2 = Time(2, 20)
    print(t1 + t2)

    t1 += Time(2, 20)
    print(t1)

    # 5
    t = Time(40, 80)
    print(t.__add__([]))
    print(t.__iadd__('bee'))