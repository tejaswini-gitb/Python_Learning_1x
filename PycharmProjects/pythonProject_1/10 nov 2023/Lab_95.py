# overriding -- same in parent name and child
 # child always always ovride the parent functions

class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        super(). sound()   # super - call my parent
        print("dog sound: bow bow")

animal=Animal()
animal.sound()

dog= Dog()
dog.sound()