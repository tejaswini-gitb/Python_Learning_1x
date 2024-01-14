 #encapsulation:
#data members(attributes) and methods together in a class
# person --- name, age, eat, sleep

class Myclass:

    def __init__(self):
        self.public_var=10
        self._proctected_var=18
        self.__private_var=17

    def public_method(self):
        print("this is public")


obj=Myclass()
obj.public_var= 77
obj.public_method()

#obj._proctected_var= 84
#print(obj.__protected_var)

obj._private_var= 97
print(obj._private_var)
