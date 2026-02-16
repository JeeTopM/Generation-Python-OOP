'''
Реализуйте класс NonNegativeObject.
При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов,
    причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.
'''


class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, key, value)


if __name__ == '__main__':
    # 1
    point = NonNegativeObject(x=1, y=-2, z=0, color='black')
    print(point.x)  # 1
    print(point.y)  # 2
    print(point.z)  # 0
    print(point.color)  # black

    # 2
    point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')
    print(point.x)  # 1.5
    print(point.y)  # 2.3
    print(point.z)  # 0.0
    print(point.color)  # yellow
