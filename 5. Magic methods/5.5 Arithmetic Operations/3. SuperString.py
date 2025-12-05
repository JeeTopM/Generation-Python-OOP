"""
Класс SuperString

Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
    string — значение строки
Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:
    <значение строки>
Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +,
    результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.
Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево
    и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:
        результатом умножения должен являться новый экземпляр класса SuperString,
            представляющий исходную строку, умноженную на n.
        результатом деления должен являться новый экземпляр класса SuperString,
            представляющий строку из первых m символов исходной строки,
            где m — длина исходной строки, поделенная нацело на n
        результатом побитового сдвига влево должен являться новый экземпляр класса SuperString,
            представляющий исходную строку без последних n символов. Если n больше или равно длине исходной строки,
            результатом должен являться экземпляр класса SuperString, представляющий пустую строку
        результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString,
            представляющий исходную строку без первых n символов. Если n больше или равно длине исходной строки,
            результатом должен являться экземпляр класса SuperString, представляющий пустую строку

Операция умножения должна быть выполнима независимо от порядка операндов,
    то есть должна быть возможность умножить как строку на число, так и число на строку.
"""


class SuperString:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f'SuperString({self.string})'

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            n = len(self.string) // other
            return SuperString(self.string[:n])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if (length := len(self.string)) <= other:
                return SuperString('')
            else:
                return SuperString(self.string[0:length - other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if len(self.string) <= other:
                return SuperString('')
            else:
                return SuperString(self.string[other:])
        return NotImplemented


if __name__ == '__main__':
    # 1
    s1 = SuperString('bee')
    s2 = SuperString('geek')

    print(s1 + s2)  # beegeek
    print(s2 + s1)  # geekbee

    # 2
    s = SuperString('beegeek')

    print(s * 2)  # beegeekbeegeek
    print(3 * s)  # beegeekbeegeekbeegeek
    print(s / 3)  # be

    # 3
    s = SuperString('beegeek')

    print(s << 4)  # bee
    print(s >> 3)  # geek
