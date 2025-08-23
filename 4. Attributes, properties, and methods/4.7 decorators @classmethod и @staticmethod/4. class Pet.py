"""
Класс Pet

Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:
    name — имя домашнего животного
Экземпляр класса Pet должен иметь один атрибут:
    name — имя домашнего животного
Класс Pet должен иметь три метода класса:
    first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet.
        Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
    last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet.
        Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
    num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet
"""


class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        if cls.pets:
            return cls.pets[0]
        return None

    @classmethod
    def last_pet(cls):
        if cls.pets:
            return cls.pets[-1]
        return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)


# test 1
print(Pet.first_pet())  # None
print(Pet.last_pet())  # None
print(Pet.num_of_pets())  # 0x

# test 2
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)  # Ratchet
print(Pet.last_pet().name)  # Rivet
print(Pet.num_of_pets())  # 3

# test 3
pet = Pet('Кемаль')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())