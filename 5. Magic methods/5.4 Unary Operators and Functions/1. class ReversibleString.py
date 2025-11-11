"""
Класс ReversibleString

Реализуйте класс ReversibleString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
    string — значение строки
Экземпляр класса ReversibleString должен иметь следующее неформальное строковое представление:
    <значение строки>

Также экземпляр класса ReversibleString должен поддерживать унарный оператор -,
результатом которого должен являться новый экземпляр класса ReversibleString со значением строки в обратном порядке.
"""
class ReversibleString:
    def __init__(self, string):
        self.string = string

# test
string = ReversibleString('python')
print(string) # python
print(-string) # nohtyp

