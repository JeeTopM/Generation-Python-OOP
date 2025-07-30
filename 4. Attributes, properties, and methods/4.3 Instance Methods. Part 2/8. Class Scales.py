"""
Класс Scales

Реализуйте класс Scales, описывающий весы с двумя чашами. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Scales должен иметь три метода экземпляра:
add_right() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на правую чашу весов этот груз
add_left() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на левую чашу весов этот груз
get_result() — метод, возвращающий строку Весы в равновесии, если массы грузов на чашах совпадают,
               Правая чаша тяжелее — если правая чаша тяжелее, Левая чаша тяжелее — если левая чаша тяжелее
"""


class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n

    def get_result(self):
        if self.left > self.right:
            return "Левая чаша тяжелее"
        elif self.right > self.left:
            return "Правая чаша тяжелее"
        return "Весы в равновесии"


# 1
scales = Scales()
scales.add_right(1)
scales.add_right(1)
scales.add_left(2)
print(scales.get_result())
# Весы в равновесии

# 2
scales = Scales()
scales.add_right(1)
scales.add_left(2)
print(scales.get_result())
# Левая чаша тяжелее

# 3
scales = Scales()
scales.add_right(2)
scales.add_left(1)
print(scales.get_result())
# Правая чаша тяжелее
