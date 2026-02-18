'''
Реализуйте класс Const. При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс Const должен разрешать устанавливать атрибуты своим экземплярам и получать их значения,
    но не разрешать изменять значения этих атрибутов, а также удалять их.
    При попытке изменить значение атрибута должно возбуждаться исключение AttributeError с текстом:
        Изменение значения атрибута невозможно
    При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:
        Удаление атрибута невозможно
'''


class Const:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __setattr__(self, k, v):
        if hasattr(self, k):
            raise AttributeError('Изменение значения атрибута невозможно')
        return super().__setattr__(k, v)

    def __delattr__(self, k):
        if hasattr(self, k):
            raise AttributeError('Удаление атрибута невозможно')

if __name__ == '__main__':
    # 1
    videogame = Const(name='Cuphead')

    videogame.developer = 'Studio MDHR'
    print(videogame.name)  # Cuphead
    print(videogame.developer)  # Studio MDHR

    # 2
    videogame = Const(name='Disco Elysium')
    try:
        videogame.name = 'Half-Life: Alyx'
    except AttributeError as e:
        print(e)  # Изменение значения атрибута невозможно

    # 3
    videogame = Const(name='The Last of Us')
    try:
        del videogame.name
    except AttributeError as e:
        print(e)  # Удаление атрибута невозможно
