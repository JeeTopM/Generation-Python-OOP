"""
Класс Gun
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь один метод экземпляра:
shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf,
                                при третьем — pif, при четвертом — paf, и так далее
"""


class Gun:
    def __init__(self):
        self.cnt = 0

    def shoot(self):
        self.cnt += 1
        if self.cnt % 2 == 0:
            print("paf")
        else:
            print("pif")


# 1
gun = Gun()
gun.shoot()  # pif
# 2
gun = Gun()
gun.shoot()  # pif
gun.shoot()  # paf
gun.shoot()  # pif
gun.shoot()  # paf
