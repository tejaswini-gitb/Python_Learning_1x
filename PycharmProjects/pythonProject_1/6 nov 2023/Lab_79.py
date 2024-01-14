from Tools.i18n.msgfmt import make


class Car:
    name ="teju"   

    def __init__(self,make,model):
        self.make = make
        self.model= model
        print("called first")


    def start_engine(self):
        print("starting a car", self.make,self.model)

car1= Car("toyota","carr")
car2= Car("minicr","18+")

car1.start_engine()
car2.start_engine()

print(id(car1))
print(id(car2))