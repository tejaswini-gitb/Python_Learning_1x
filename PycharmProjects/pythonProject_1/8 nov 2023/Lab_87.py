#single inheritae
#use the propertirs and method of your base class or parent class

class father :
    bnk_bal = 1000

    def one_bnk(self):
        print("use it")


class son(father):
    pass

s= son()
s.one_bnk()
print(s.bnk_bal)