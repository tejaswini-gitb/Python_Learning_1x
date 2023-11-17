# hierachical inheritanc


class Vehicle:
    def info(self):
        return "this is a vehicle"

class Car(Vehicle):
    def info(self):
        return "this is car"

class biCar(Vehicle):

    def info(self):
        return "this is bicar"

car= Car()
bicar =biCar()
print(car.info())
print(bicar.info())