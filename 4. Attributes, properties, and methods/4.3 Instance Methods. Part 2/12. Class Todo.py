"""
Класс Todo

Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Todo должен иметь один атрибут:
    things — изначально пустой список дел, которые нужно выполнить
Класс Todo должен иметь четыре метода экземпляра:
    add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа:
        (<название дела>, <приоритет>)
    get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
    get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
    get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет
"""


class Todo:
    def __init__(self):
        self.things = []
        self.low = 10**100
        self.high = 0

    def add(self, thing, priority):
        thing = (thing, priority)
        self.things.append(thing)
        if thing[1] < self.low:
            self.low = thing[1]
        if thing[1] > self.high:
            self.high = thing[1]

    def get_by_priority(self, n):
        res = [thing[0] for thing in self.things if thing[1] == n]
        return res

    def get_low_priority(self):
        res = [thing[0] for thing in self.things if thing[1] == self.low]
        return res

    def get_high_priority(self):
        res = [thing[0] for thing in self.things if thing[1] == self.high]
        return res


# 1
todo = Todo()

print(todo.things)  # []
print(todo.get_by_priority(1))  # []
print(todo.get_low_priority())  # []
print(todo.get_high_priority())  # []


# 2
todo = Todo()

todo.add("Проснуться", 3)
todo.add("Помыться", 2)
todo.add("Поесть", 2)
print(todo.get_by_priority(2))  # ['Помыться', 'Поесть']

# 3
todo = Todo()

todo.add("Ответить на вопросы", 5)
todo.add("Сделать картинки", 1)
todo.add("Доделать задачи", 4)
todo.add("Дописать конспект", 5)

print(todo.get_low_priority())  # ['Сделать картинки']
print(todo.get_high_priority())  # ['Ответить на вопросы', 'Дописать конспект']
print(todo.get_by_priority(3))  # []


"""
class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing, priority):
        self.things.append((thing, priority))

    def get_by_priority(self, priority):
        result = [t for t, p in self.things if p == priority ]
        return result

    def get_low_priority(self):
        priority = min(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)

    def get_high_priority(self):
        priority = max(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)
"""
