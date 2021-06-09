from bank import Account

bank = Account(name="Jane",phone="0789765433")
print(bank.deposit(50000))
print(bank.deposit(1000))
# print(bank.transactions)
bank.get_statement()
