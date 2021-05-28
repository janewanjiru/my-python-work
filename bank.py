class Bank:
    def __init__(self,accountName,accountNumber,owner):
        self.accountBalance=accountName
        self.accountNumber=accountNumber
        self.owner=owner
    def withdraw(self):   
        return f"Hello {self.owner} your  withdraw amount is below the limit"
    def deposit(self):
        return f"The{self.onwer} deposit money from{self.accountName}"
    def  balance(self):
        return f"Hello please enter {self.accountName} to check your balance"


       
