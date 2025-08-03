"""
 Класс User

Реализуйте класс User, описывающий интернет-пользователя.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя пользователя.
Если name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
age — возраст пользователя.
Если age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст

Экземпляр класса User должен иметь два атрибута:
_name — имя пользователя
_age — возраст пользователя
"""


class User:
    def __init__(self, name, age):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError("Некорректное имя")

        if isinstance(age, int) and 0 <= age < 110:
            self._age = age
        else:
            raise ValueError("Некорректный возраст")

    def get_name(self):
        """метод, возвращающий имя пользователя"""
        return self._name

    def set_name(self, new_name):
        """метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name.
        Если new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
        Некорректное имя"""
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Некорректное имя")

    def get_age(self):
        """метод, возвращающий возраст пользователя"""
        return self._age

    def set_age(self, new_age):
        """метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age.
        Если new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
        Некорректный возраст"""
        if isinstance(new_age, int) and 0 <= new_age <= 110:
            self._age = new_age
        else:
            raise ValueError("Некорректный возраст")


# 1
user = User("Гвидо", 67)

print(user.get_name())  # Гвидо
print(user.get_age())  # 67

# 2
user = User("Гвидо", 67)

user.set_name("Тимур")
user.set_age(30)

print(user.get_name())  # Тимур
print(user.get_age())  # 30

# TEST_3:
user = User("Меган", 37)
invalid_names = (-1, True, "", [], "123456", "Меган906090")
for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)

# 6
invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50)
for age in invalid_ages:
    try:
        user = User('Меган', age)
    except ValueError as e:
        print(e)