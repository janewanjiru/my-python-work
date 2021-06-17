# class Account:
#     def __init__(self,name,phone):
#       self.name=name
#       self.phone=phone
#       self.balance=0
#     def  borrow(self,amount):
#         if amount<=0:
#             return f"Entered invalid input"
#         elif amount>=self.loan:
#             return f"Your loan is cleared and your account balance is{self.balance}" 
#         else:
#             amount<=self.loan
#             amount-self.loan+=self.loan
#             return f"your account loan_balance is {self.balance}"

    
# class Rename:
#     def __init__(self,name) :
#         self.name=name

#         print: Hello my name is f{'name'}
class School:
    number_of_students=0
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.fee=50000
        self.excess=0

        School.number_of_students +=1
    def calculate_fees(self,amount):
        try:
            amount+"five thousands"
        except TypeError:
            return "please enter amount in figures"  
        if amount>500 :
            return f"You can pay the fees"  
        elif amount< self.fee and amount>500:
            return f"your fee balance is {self.fee}" 
        else:
            amount>self.fee
            balance=amount-self.fee
            self.excess+=self.excess
            return f"Your amount balance is {self.balance }"


                  





        
                   