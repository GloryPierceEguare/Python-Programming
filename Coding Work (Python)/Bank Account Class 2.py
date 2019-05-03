class BankAccount():
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def deposit(self,amount):
        self.balance += amount

    def printbalance(self):
        print(self.account, "€", self.balance, "\n")


class CurrentAccount(BankAccount):
    def __init__(self, account, balance):
        BankAccount.__init__(self, account, balance)

    def withdraw(self, amount):
        self.balance -= amount

        if self.balance < 0:
            print("You are now in debt!")


class SavingsAccount(BankAccount):
    def __init__(self, account, balance):
        BankAccount.__init__(self, account, balance)

    def interest(self, amount):
        self.balance *= amount


#Main
x = BankAccount("Bank Account:", 2000)
a = int(input("Enter the amount of money to withdraw from Bank Account: €"))
x.withdraw(a)
x.printbalance()

y = CurrentAccount("Current Account:", 200)
y.withdraw(300)
y.printbalance()

z = SavingsAccount("Savings Account:", 100)
c = int(input("Enter the amount of money to deposit into Savings Account: €"))
z.deposit(c)
z.interest(1.5)
z.printbalance()