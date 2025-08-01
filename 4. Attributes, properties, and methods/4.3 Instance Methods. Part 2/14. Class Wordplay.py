"""
Класс Wordplay

Будем называть словом любую последовательность из одной или более латинских букв.
Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра класс должен принимать один аргумент:
    words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым
Экземпляр класса Wordplay должен иметь один атрибут:
    words — список, содержащий набор слов
Класс Wordplay должен иметь четыре метода экземпляра:
    add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор.
                 Если слово уже есть в наборе, метод ничего не должен делать
    words_with_length() — метод, принимающий в качестве аргумента натуральное число n
                          и возвращающий список слов из набора, длина которых равна n
    only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий список всех слов из набора,
             которые включают в себя только переданные буквы
    avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий список всех слов из набора,
             которые не содержат ни одну из этих букв
"""


class Wordplay:
    def __init__(self, words=[]):
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, lenght):
        return [word for word in self.words if len(word) == lenght]

    def only(self, *args):
        data = args
        return [word for word in self.words if all((char) in data for char in word)]

    def avoid(self, *args):
        data = args
        return [word for word in self.words if not any((char) in data for char in word)]


# 1
wordplay = Wordplay()
print(wordplay.words_with_length(1))  # []
print(wordplay.only("a", "b", "c"))  # []
print(wordplay.avoid("a", "b", "c"))  # []

# 2
wordplay = Wordplay()
print(wordplay.words)  # []
wordplay.add_word("bee")
wordplay.add_word("geek")
print(wordplay.words)  # ['bee', 'geek']

# 3
wordplay = Wordplay(["bee", "geek", "cool", "stepik"])
wordplay.add_word("python")
print(wordplay.words_with_length(4))  # ['geek', 'cool']

# 4
wordplay = Wordplay(["o", "to", "otto", "top", "t"])
print(wordplay.only("o", "t"))  # ['o', 'to', 'otto', 't']
