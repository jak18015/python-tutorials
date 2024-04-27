class Account:
    
    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):
        self.balance=self.balance + amount
    
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    def __init__(self, filepath):
        Account.__init__(self, filepath)
    
    def transfer(self, amount, fee):
        self.balance = self.balance - amount - (amount*())

checking = Checking("account\\balance.txt")
checking.transfer(10, 0.01)
print(checking.balance)
checking.commit()