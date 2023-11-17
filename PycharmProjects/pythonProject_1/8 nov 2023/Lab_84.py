#public - variable - don't mention anything
#protected
#private

#variable anf function

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age =age

    def get_name(self):
        return self.__name

    def set_name(self):
        if name == "john":
            print("dont set")
        else:
            self("your details",self.__name, self.__age)
    def print_details(self):
        print("your details",self.__name, self.__age)

person = Person("amit",34)
person.print_details()

person.set_name("john")

name = person.get_name()
print(name)