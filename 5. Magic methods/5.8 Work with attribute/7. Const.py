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
    ...


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
