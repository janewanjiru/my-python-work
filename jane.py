class Account:
    def __init__(self,name,phone):
      self.name=name
      self.phone=phone
      self.balance=0
    def  borrow(self,amount):
        if amount<=0:
            return f"Entered invalid input"
        elif amount>=self.loan:
            return f"Your loan is cleared and your account balance is{self.balance}" 
        else:
            amount<=self.loan
            amount-self.loan+=self.loan
            return f"your account loan_balance is {self.balance}"

    

        
                   