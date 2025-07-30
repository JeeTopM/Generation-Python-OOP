"""
Класс Gun
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь три метода экземпляра:
shoot() — метод, при первом вызове которого выводится строка pif,
                 при втором — paf, при третьем — pif, при четвертом — paf, и так далее
shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля
"""


class Gun:
    def __init__(self):
        self.cnt = 0

    def shoot(self):
        if self.cnt % 2 == 0:
            print("pif")
        else:
            print("paf")
        self.cnt += 1

    def shots_count(self):
        return self.cnt

    def shots_reset(self):
        self.cnt = 0


# 1
gun = Gun()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
"""
0
pif
1
paf
2
"""

# 2
gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())

"""
pif
paf
2
0
pif
1
"""
