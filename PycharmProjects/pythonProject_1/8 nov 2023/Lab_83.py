class BankAccount:
    def __init__(self):
        self.balance = 0    # instance cariable (can access it via only object)


    def Is_Auth_True(self,amount):
       # self.balance = self.balnce += amount
       self.balance += amount

    def _without(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("your balnce", self.balance)

jp_chase = BankAccount()
#jp_chase.deposit(2000)
#jp_chase.deposit(1000)

# with Auth
jp_chase.Is_Auth_true(True)

jp_chase._BankAzccount__private_var=200
print(jp_chase._BankAccount__private_var)

jp_chase.Is_Auth_True_show_bal(False)