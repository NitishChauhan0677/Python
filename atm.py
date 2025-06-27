class ATM(object):
    def __init__(self,balance=0):
        self.balance = balance
        print("ATM object is created")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit amount: ", amount)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient")
        else:
            self.balance = self.balance - amount
            print("Withdraw amount: ", amount)

    def mniStatement(self):
        print("current Balance: ", self.balance)
    
x = ATM()
x.deposit(10000)
x.withdraw(5000)
x.mniStatement()

