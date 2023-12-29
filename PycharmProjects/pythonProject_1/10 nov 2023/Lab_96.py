# method over loading
# python doesn't support method overriding

class MathUtil:
    def add(self, a, b=0, c=0):
        return a + b + c

math = MathUtil()
op0= math.add(1)
print(op0)
op1= math. add(10,9)
print(op1)
# math. add(5,5,7)

op2= math. add(10,9, c=0)
print(op2)
