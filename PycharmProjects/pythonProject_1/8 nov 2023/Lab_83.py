class BankAccount:
    def __init__(self):
        self.balance = 0    # instance cariable (can access it via only object)


    def deposit(self,amount):
       # self.balance  = self.balnce + amount
       self.balance += amount

    def _witdraw(self, amount):    #  _ protected
        self.balance -= amount

    def __show_balance(self):
        print("your balnce", self.balance)

jp_chase = BankAccount()
#jp_chase.deposit(2000)
jp_chase._witdraw(458)
jp_chase.show_balance()

# with Auth
jp_chase.Is_Auth_true(True)

jp_chase._BankAzccount__private_var=200
print(jp_chase._BankAccount__private_var)

jp_chase.Is_Auth_True_show_bal(False)