class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=float(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):
        self.balance=self.balance + amount
    
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    type="checking"

    def __init__(self, filepath):
        Account.__init__(self, filepath)
    
    def transfer(self, amount, fee):
        self.balance = self.balance - amount - (amount*(1+fee))
        self.balance = round(self.balance, ndigits=2)

transfer_fee = 0.015654
checking = Checking("account\\balance.txt")
checking.transfer(10, transfer_fee)
print("$", checking.balance)
checking.commit()