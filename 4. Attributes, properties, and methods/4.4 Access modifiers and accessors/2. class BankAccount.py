"""
Класс BankAccount

Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен принимать один аргумент:
    balance — баланс счета, по умолчанию имеет значение 0
Экземпляр класса BankAccount должен иметь один атрибут:
    _balance — баланс счета
"""


class BankAccount:
    def __init__(self, balance=0):
        self._balane = balance

    def get_balance(self):
        """— метод, возвращающий актуальный баланс счета"""
        pass

    def deposit():
        """— метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount"""
        pass

    def withdraw():
        """— метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount.
        Если amount превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением:
        На счете недостаточно средств"""
        pass

    def transfer():
        """— метод, принимающий в качестве аргументов банковский счет account и число amount. Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount. Если amount превышает количество средств на балансе текущего счета, должно быть возбуждено исключение ValueError с сообщением:
        На счете недостаточно средств"""
        pass


# 1
account = BankAccount()

print(account.get_balance())  # 0
account.deposit(100)
print(account.get_balance())  # 100
account.withdraw(50)
print(account.get_balance())  # 50
