# from bank import Account, MobileMoneyAccount

# bank = Account(name="Jane",phone="0789765433")
# print(bank.deposit(50000))
# print(bank.deposit(1000))
# # print(bank.transactions)
# bank.get_statement()

# bank = MobileMoneyAccount(name="Jane Doe",phoneNumber="0789765433",service_provider="safaricom")
# print(bank.deposit(10000))
# print(bank.buy_airtime (1000))
# print(bank.get_statement())
# bank.get_statement()
from jane import School
 
student1=School("paul",4563738,7000)
student2=School("Mack",332323,4000)
student3=School(name="Joy",id=454689,fee_balance=2000)
student4=School(name="Bien",id=59874,fee_balance=1000)
print(School.number_of_students)
print(student1.name)
print(student3.id)
print(student1.fee_balance)
print(student2.fee_balance)
print(student3.fee_balance)
print(student4.fee_balance)