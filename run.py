from bank import Account, MobileMoneyAccount

# bank = Account(name="Jane",phone="0789765433")
# print(bank.deposit(50000))
# print(bank.deposit(1000))
# # print(bank.transactions)
# bank.get_statement()

bank = MobileMoneyAccount(name="Jane Doe",phoneNumber="0789765433",service_provider="safaricom")
print(bank.deposit(10000))
print(bank.buy_airtime (1000))
print(bank.get_statement())
# bank.get_statement()