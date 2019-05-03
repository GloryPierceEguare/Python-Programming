class BankAccount():
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insuficient funds")

x = BankAccount("125c",2000)
x.withdraw(200)

print(x.balance)