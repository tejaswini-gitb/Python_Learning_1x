# hybrid inheritance

class A:
    def method(self):
        return "method A"

class B(A):
    def method(self):
            return "method B"

class C(A):
    def method(self):
            return "method C"

class D(B, C):
    def method(self):
            return "method D"

d =D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())