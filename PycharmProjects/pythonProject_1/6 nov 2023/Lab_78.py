class Car:
    def start_engine(self):
        print("start my car engine---")

car1 = Car()
car2 = Car()

print(id(car1))
print(id(car2))


class Car:
    name ="abc"

    def __init__(self) :
        print("start my car engine" + self.name)

car1 = Car()
car2 = Car()

print(id(car1))
print(id(car2))