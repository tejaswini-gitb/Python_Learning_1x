# take a input from user we will createmow

class Car:
    color= None
    model = None

    def car_details(self):
        print("your car details:", self.color, self.model)

car_color=input("enter your car color")
car_model=input("enter your car model")

car_obj_ref= Car()
car_obj_ref.Color= car_color
car_obj_ref.model= car_model

car_obj_ref.car_details()