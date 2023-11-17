class Myclass:

    def __init__(self):
        self. __private__car = "private car only for 1 person"
        self._protected_attribute =42
        self.public_var= 55

    def __private_method(self):
        return " this is a private method"

obj = Myclass()
#print(obj._Myclass__private_car)
print(obj.public_var)