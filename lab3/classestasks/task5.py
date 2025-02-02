#Create a bank account class that has
# attributes owner, balance and two methods 
# deposit and withdraw. Withdrawals may not 
# exceed the available balance. Instantiate your 
# class, make several deposits and withdrawals, and 
# test to make sure the account can't be overdrawn.

#class Account:
#   pass

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")

acc = Account("John", 100)
acc.deposit(50)  
acc.withdraw(30)  
acc.withdraw(200)  
