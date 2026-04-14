"""
Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший).
При создании экземпляра класс не должен принимать никаких аргументов.

Класс DevelopmentTeam должен иметь два метода экземпляра:
add_junior() — метод, принимающий произвольное количество позиционных аргументов, 
    каждый из которых является именем разработчика,и добавляющий их в число junior-разработчиков
add_senior() — метод, принимающий произвольное количество позиционных аргументов, 
    каждый из которых является именем разработчика, и добавляющий их в число senior-разработчиков

Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его junior-разработчики, 
    а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:
        (<имя разработчика>, 'junior')
         
    в то время как senior-разработчики — в виде кортежей:
        (<имя разработчика>, 'senior')
"""

class DevelopmentTeam:
    def __init__(self):
        self._seniors = []
        self._juniors = []
        
    def add_junior(self, *juniors):
        self._juniors.extend(juniors)
        
    def add_senior(self, *seniors):
        self._seniors.extend(seniors)
        
    def __iter__(self):
        for junior in self._juniors:
            yield (junior, 'junior')
        for senior in self._seniors:
            yield (senior, 'senior')


if __name__ == "__main__":
    # test 1
    beegeek = DevelopmentTeam()
    beegeek.add_junior('Timur')
    beegeek.add_junior('Arthur', 'Valery')
    beegeek.add_senior('Gvido')
    print(*beegeek, sep='\n') # ('Timur', 'junior') ('Arthur', 'junior') ('Valery', 'junior') ('Gvido', 'senior')


    # test 2
    beegeek = DevelopmentTeam()
    print(len(list(beegeek))) # 0

    # test 3
    beegeek = DevelopmentTeam()
    beegeek.add_junior('Timur')
    beegeek.add_junior('Arthur', 'Valery')
    print(*beegeek, sep='\n') # ('Timur', 'junior') ('Arthur', 'junior') ('Valery', 'junior')