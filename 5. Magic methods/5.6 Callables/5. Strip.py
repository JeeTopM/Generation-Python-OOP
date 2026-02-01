"""
Реализуйте класс Strip, экземпляры которого позволяют удалять из начала и конца строки определенные символы.
    При создании экземпляра класс должен принимать один аргумент:
        chars — строка, в которой перечислены удаляемые символы
Экземпляр класса Strip должен являться вызываемым объектом и принимать один аргумент:
    string — строка
Экземпляр класса Strip должен удалять из начала и конца строки string все символы,
    перечисленные в chars, и возвращать полученный результат.
"""


class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)


if __name__ == '__main__':
    # test 1
    strip = Strip('!? ')

    print(strip('     ?beegeek!'))  # beegeek
    print(strip('!bee?geek!'))  # bee?geek

    # test 2
    strip = Strip('.,+-')

    print(strip('     --++beegeek++--'))  # --++beegeek
    print(strip('-bee...geek-'))  # bee...geek
    print(strip('-+,.b-e-e-g-e-e-k-+,.'))  # b-e-e-g-e-e-k
