class Bank:
    def __init__(self):
        self.accounts = {}

    def deposit(self, name, amount):
        if name not in self.accounts:
            self.accounts[name] = 0
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name not in self.accounts:
            self.accounts[name] = 0
        self.accounts[name] -= amount

    def balance(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            return "ERROR"

    def transfer(self, sender, receiver, amount):
        self.withdraw(sender, amount)
        self.deposit(receiver, amount)

    def income(self, percent):
        for name in self.accounts:
            if self.accounts[name] > 0:
                self.accounts[name] += self.accounts[name] * percent // 100

bank = Bank()

inputs = [
    "DEPOSIT Ivanenko 100",
    "INCOME 5",
    "BALANCE Ivanenko",
    "TRANSFER Ivanenko Petrenko 50",
    "WITHDRAW Petrenko 100",
    "BALANCE Petrenko",
    "BALANCE Sydorenko"
]

for command in inputs:
    command = command.split()
    if command[0] == "DEPOSIT":
        bank.deposit(command[1], int(command[2]))
    elif command[0] == "WITHDRAW":
        bank.withdraw(command[1], int(command[2]))
    elif command[0] == "BALANCE":
        print(bank.balance(command[1]))
    elif command[0] == "TRANSFER":
        bank.transfer(command[1], command[2], int(command[3]))
    elif command[0] == "INCOME":
        bank.income(int(command[1]))
