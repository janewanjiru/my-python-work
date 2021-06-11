from datetime  import  datetime

class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction=100
        self.limit=5000
        self.fees=50
        self.loan_limit=0
        self.transactions=[]  
    def deposit(self,amount):
        try:
          amount+10
        except TypeError:
            return f"Please enter in figures "
        if amount<=0:
            return f"please deposit  invalid amount"
        else:
            self.balance+=amount
            transaction={"amount":amount,"balance": self.balance,"narration":"You deposited","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"    
    def withdraw(self,withdraw_amount):
        total= withdraw_amount+self.transaction
        if withdraw_amount<=0:
            return f"Input valid amount"
        elif total>self.balance:
            return f" insufficient balance"
        else:
            self.balance-=total
            return f"Hello{self.name} you have sufficient that you can now borrow {withdraw_amount}  and your balance is {self.balance} " 

    def borrow(self,amount):
        try:
            amount+10
        except TypeError:
            return f"please enter amount in figures"    
        if amount>=self.loan_limit:
          return f"you will not be able to borrow the money" 
        elif amount<0:
            return f"you can't borrow"
        elif self.loan>0:
            return f"you have an already existing loan "  
        else:
            loan_fee=amount*0.5
            self.loan=loan_fee+amount 
            transaction={"amount":amount,"balance": self.balance,"narration":"You borrowed","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} you have received {amount} and you pay {self.loan} "  
    def repay(self,amount):
        try:
            amount+10
        except TypeError:
            return f"please enter amount in figures"    
        if amount<=0:
             return f"Amount must be greater than 0"
        elif amount>=self.loan_amount:
             payment=amount-self.loan_amount
             self.balance+=payment
             transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
             self.transaction.append(transaction)

             return f'You have repaid your loan new balance is {self.balance}'

        else:
             diff=self.loan_amount-amount
             transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
             self.transaction.append(transaction)

             return f"{amount} has been deducted to repay your loan outstanding debt is {diff}"
    
    def get_statement(self):
        for transaction in self.transactions:
            amount=transaction["amount"]
            narration=transaction["narration"]  
            balance=transaction["balance"] 
            time=transaction["time"] 
            date=time.strftime("%D") 
            print(f"{date}......{narration}......{amount}.....balance{balance}")

    def  transfer(self,amount):
        try:
            amount+10
        except TypeError:
            return f"please enter amount in figures"

        check: amount>0

        fee=amount*0.05
        total=amount+fee
        if total>self.balanceAccount:
            return f"Your balance is {self.balance} you need {self.total} in order to transfer {self.amount}" 
        else:
            self.balance-=total
            Account.deposit(amount) 
            return f"your balanceAccount is below your {amount}"       
class MobileMoneyAccount(Account):
        
    def __init__(self,name,phoneNumber,service_provider):
            Account. __init__(self,name,phoneNumber)
            self.service_provider=service_provider

    def buy_airtime(self,amount):
        if amount<=0:
            return f"invalid input"
        else:
         amount<=self.balance
         self.balance-=amount
         transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
         self.transactions.append(transaction)
         return f"you've bought airtime of {amount}"
           



          

        

              


    

    


       


    
   


       

        
    


