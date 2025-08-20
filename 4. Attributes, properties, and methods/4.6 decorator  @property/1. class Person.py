"""
Класс Person

Вам доступен класс Person, описывающий человека. При создании экземпляра класс принимает два аргумента в следующем порядке:
    name — имя человека
    surname — фамилия человека
Экземпляр класса Person имеет два атрибута:
    name — имя человека
    surname — фамилия человека
Класс Person имеет одно свойство:
    fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
        <имя> <фамилия>
Реализуйте свойство fullname класса Person с помощью декоратора @property.
"""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()

# test 1
person = Person('Mike', 'Pondsmith')

print(person.name)
print(person.surname)
print(person.fullname)

# test 2
person = Person('Mike', 'Pondsmith')

person.name = 'Troy'
print(person.fullname)

# test 3
person = Person('Mike', 'Pondsmith')

person.surname = 'Baker'
print(person.fullname)

# test 4
person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)