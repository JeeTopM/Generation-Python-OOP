'''
Требовалось реализовать класс Item, описывающий предмет.
При создании экземпляра класс должен был принимать три аргумента в следующем порядке:
    name — название предмета
    price — цена предмета в рублях
    quantity — количество предметов
Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной буквы,
    а при обращении к атрибуту total — произведение цены предмета на его количество.
Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.
'''


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, 'name').title()
        return object.__getattribute__(self, name)


if __name__ == '__main__':
    fruit = Item('banana', 15, 5)
    print(fruit.price)  # 15
    print(fruit.quantity)  # 5

    fruit = Item('banana', 15, 5)
    print(fruit.name)  # Banana
    print(fruit.total)  # 75

    course = Item('pygen', 3900, 2)
    print(course.name)  # Pygen
    print(course.price)  # 3900
    print(course.quantity)  # 2
    print(course.total)  # 7800
