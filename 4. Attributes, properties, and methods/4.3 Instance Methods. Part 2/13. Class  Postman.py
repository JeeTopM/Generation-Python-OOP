"""
Класс Postman

Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Postman должен иметь один атрибут:
    delivery_data — изначально пустой список адресов, по которым следует доставить письма
Экземпляр класса Postman должен иметь три метода экземпляра:
    add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру,
        и добавляющий в список адресов эти данные в виде кортежа:
        (<улица>, <дом>, <квартира>)
    get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице,
        в которые требуется доставить письма
    get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом доме,
        в которые требуется доставить письма
"""


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, home, flat):
        self.delivery_data.append((street, home, flat))

    def get_houses_for_street(self, street):
        res = [h for s, h, f in self.delivery_data if s == street]
        return list(dict.fromkeys(res))

    def get_flats_for_house(self, street, home):
        res = [f for s, h, f in self.delivery_data if s == street and h == home]
        return list(dict.fromkeys(res))


# 1
postman = Postman()

print(postman.delivery_data)  # []
print(postman.get_houses_for_street("3-я ул. Строителей"))  # []
print(postman.get_flats_for_house("3-я ул. Строителей", 25))  # []

# 2
postman = Postman()

postman.add_delivery("Советская", 151, 74)
postman.add_delivery("Советская", 151, 75)
postman.add_delivery("Советская", 90, 2)
postman.add_delivery("Советская", 151, 74)

print(postman.get_houses_for_street("Советская"))  # [151, 90]
print(postman.get_flats_for_house("Советская", 151))  # [74, 75]
