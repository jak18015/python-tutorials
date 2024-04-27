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
jacks_checking = Checking("account\\jack.txt")
jacks_checking.transfer(10, transfer_fee)
print("Jack's "+jacks_checking.type)
print("$", checking.balance)
jacks_checking.commit()

transfer_fee = 0.015654
johns_checking = Checking("account\\john.txt")
johns_checking.transfer(10, transfer_fee)
print("John's "+checking.type)
print("$", checking.balance)
johns_checking.commit()