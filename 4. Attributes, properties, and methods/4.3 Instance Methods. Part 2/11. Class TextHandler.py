"""
Класс TextHandler

Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов, разделенных пробельными символами.

Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса TextHandler должен иметь три метода:

add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
"""


class TextHandler:
    def __init__(self):
        self.words = []
        self.min_len = 0
        self.max_len = 0

    def add_words(self, text):
        for word in text.split():
            self.words.append(word)
            self.min_len = min(len(word) for word in self.words)
            self.max_len = max(len(word) for word in self.words)

    def get_shortest_words(self):
        return [word for word in self.words if len(word) == self.min_len]

    def get_longest_words(self):
        return [word for word in self.words if len(word) == self.max_len]


# 1
texthandler = TextHandler()
print(texthandler.get_shortest_words())  # []
print(texthandler.get_longest_words())  # []

# 2
texthandler = TextHandler()
texthandler.add_words("do not be sorry")
texthandler.add_words("be")
texthandler.add_words("better")
print(texthandler.get_shortest_words())  # ['do', 'be', 'be']
print(texthandler.get_longest_words())  # ['better']


# 3
texthandler = TextHandler()
texthandler.add_words("The world will hold my trial for your sins")
texthandler.add_words("Never meant to see the sky never meant to live")
print(texthandler.get_shortest_words())  # ['my', 'to', 'to']
print(
    texthandler.get_longest_words()
)  # ['world', 'trial', 'Never', 'meant', 'never', 'meant']
