"""
Класс BankAccount

Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен принимать один аргумент:
    balance — баланс счета, по умолчанию имеет значение 0
Экземпляр класса BankAccount должен иметь один атрибут:
    _balance — баланс счета
"""


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        """— метод, возвращающий актуальный баланс счета"""
        return self._balance

    def deposit(self, amount):
        """— метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount"""
        self._balance += amount

    def withdraw(self, amount):
        """— метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount.
        Если amount превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением:
        На счете недостаточно средств"""
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError("На счете недостаточно средств")

    def transfer(self, account, amount):
        """— метод, принимающий в качестве аргументов банковский счет account и число amount.
        Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount.
        Если amount превышает количество средств на балансе текущего счета,
        должно быть возбуждено исключение ValueError с сообщением:
        На счете недостаточно средств"""
        self.withdraw(amount)
        account.deposit(amount)
# 1
account = BankAccount()

print(account.get_balance())  # 0
account.deposit(100)
print(account.get_balance())  # 100
account.withdraw(50)
print(account.get_balance())  # 50

# 2
account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)
# На счете недостаточно средств

# 3
account1 = BankAccount(100)
account2 = BankAccount(200)

account1.transfer(account2, 50)
print(account1.get_balance())  # 50
print(account2.get_balance())  # 250
