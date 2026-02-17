'''
Реализуйте класс AttrsNumberObject.
При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:
    attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент,
        включая сам атрибут attrs_num
'''


class AttrsNumberObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)
        self.attrs_num = True
        object.__setattr__(self, 'attrs_num', len(self.__dict__))

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        object.__setattr__(self, 'attrs_num', len(self.__dict__))

    def __delattr__(self, name):
        object.__delattr__(self, name)
        object.__setattr__(self, 'attrs_num', len(self.__dict__))

if __name__ == '__main__':
    # 1
    music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')
    print(music_group.attrs_num)  # 3

    # 2
    music_group = AttrsNumberObject()
    print(music_group.attrs_num)  # 1

    # 3
    music_group = AttrsNumberObject(name='Woodkid', genre='pop')
    print(music_group.attrs_num)  # 3
    music_group.country = 'France'
    print(music_group.attrs_num)  # 4

    # 4
    music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')
    print(music_group.attrs_num)  # 3
    del music_group.genre
    print(music_group.attrs_num)  # 2
