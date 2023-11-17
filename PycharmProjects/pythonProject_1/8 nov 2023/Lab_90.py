
class father:
    def father_money(self):
        return "500"

class mother:
    def mother_money(self):
        return "600"

class son(father, mother):
   pass

son= son()
print(son.father_money())
print(son.mother_money())