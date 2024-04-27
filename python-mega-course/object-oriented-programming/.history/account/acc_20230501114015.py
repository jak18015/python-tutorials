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

class Checking:
    def __init__(self):
        Acc
