# COLLECTION:
# list, dic, tuple, set, orderdict - data type

from collections import namedtuple

person = namedtuple("person",["name","age","gender"])

person = person(name ="amogh", age =34, gender="M")
print("name",person.name)
print("age",person.age)
print("gender",person.gender)

class Person2:

    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print(f"Person details {self.name}")

person2 = Person2("amogh", "23", "m")
person2.print_details()