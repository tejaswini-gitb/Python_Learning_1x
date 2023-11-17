# inheritance

class Animal:

        def car(self):
            print("lambo")

        def speak(self):
            pass

class Dog(Animal):
    def speak(self):
         print("BOw bow")

    def i_want_drive(self):
        Animal().car()


dog =Dog()
dog.speak()
dog.i_want_drive()