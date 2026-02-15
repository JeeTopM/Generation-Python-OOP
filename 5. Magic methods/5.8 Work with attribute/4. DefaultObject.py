'''
Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default,
    имеющий значение по умолчанию None, а после произвольное количество именованных аргументов. Аргументы,
    передаваемые после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.
При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default.
'''


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        # self.__dict__.update(kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattr__(self, attr):
        return self.default


if __name__ == '__main__':
    # 1
    god = DefaultObject(name='Ares', mythology='greek')
    print(god.name)  # Ares
    print(god.mythology)  # greek
    print(god.age)  # None

    # 2
    god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')
    print(god.name)  # Tyr
    print(god.mythology)  # scandinavian
    print(god.age)  # 0
