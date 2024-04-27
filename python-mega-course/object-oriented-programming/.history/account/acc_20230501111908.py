class Account:
    
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        with open

account=Account("account\\balance.txt")
print(account.balance)
