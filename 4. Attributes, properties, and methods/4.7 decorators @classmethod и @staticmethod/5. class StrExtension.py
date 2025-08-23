"""
Класс StrExtension
Реализуйте класс StrExtension, описывающий набор функций для работы со строками.
При создании экземпляра класс не должен принимать никаких аргументов.
Класс StrExtension должен иметь три статических метода:
    remove_vowels() — метод, который принимает в качестве аргумента строку,
        удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат
    leave_alpha() — метод, который принимает в качестве аргумента строку,
        удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат
    replace_all() — метод, который принимает три строковых аргумента string, chars и char,
        заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.
"""
class StrExtension:
    @staticmethod
    def remove_vowels(string):
        return ''.join(i for i in string if i not in 'aeiouyAEIOUY')

    @staticmethod
    def leave_alpha(string):
        return ''.join(i for i in string if i.isalpha())

    @staticmethod
    def replace_all(string, chars, char):
        return ''.join(char if i in chars else i for i in string)


# test 1
print(StrExtension.remove_vowels('Python'))  # Pthn
print(StrExtension.remove_vowels('Stepik'))  # Stpk

# test 2
print(StrExtension.leave_alpha('Python111'))  # Python
print(StrExtension.leave_alpha('__Stepik__()'))  # Stepik

# test 3
print(StrExtension.replace_all('Python', 'Ptn', '-'))  # -y-ho-
print(StrExtension.replace_all('Stepik', 'stk', '#'))  # S#epi#
