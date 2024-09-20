class Account:
    def __init__(self, number, name, initial_amount=1000):
        self.__number = number
        self.__name = name
        self.__balance = initial_amount
    def __repr__(self):
        return f'[number={self.__number}, name={self.__name}, balance={self.__balance}]'
    def __str__(self):
        return self.__repr__()
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print("No enough balance")
            return
        self.__balance -= amount

akhila_ac = Account(name='akhi',number='132456789012',initial_amount=3000)
print(akhila_ac)
akhila_ac.deposit(20000)
print(akhila_ac)
akhila_ac.deposit(1000)
print(akhila_ac)
akhila_ac.withdraw(500)
print(akhila_ac)
#print(akhila_ac.__dict__)    
#print(akhila_ac.__balance)
akhila_ac.withdraw(20000)
print(akhila_ac)