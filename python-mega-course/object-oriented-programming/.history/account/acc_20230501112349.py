class Account:
    
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):
        self.balance=self.balance + amount

account = Account("account\\balance.txt")
print(account.balance)

