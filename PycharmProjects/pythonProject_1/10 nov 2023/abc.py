# Abstraction -- OOP's
# hiding the imp details and showing what is required

# car -- start -- engine --put gear -- start driving
# hide core implementation and show only imp details

from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bow BOw🐶"

class Cat(Animal):
    def sound(self):
        return "mew mew 🐈"

class Tiger(Animal):
    def sound(self):
        return "roar -++-🐯!!!"

dog =Dog()
print(dog.sound())

cat =Cat()
print(cat.sound())

tiger =Tiger()
print(tiger.sound())