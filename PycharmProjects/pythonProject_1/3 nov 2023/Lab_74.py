# car
# object --tesla, lambo

class Car:
    #attributes
    name = None
    color = None
    model = None
    speed = None
    engine = None

#methodsnov
    def start_engine(self):
        print(" starting engine")

    def Break(self):
        print("use a break")

    def drive(self):
        print("I'm driving :", self.name)

tesla_obj= Car()  # object
tesla_obj.name = "tesla"

lambo_obj= Car()
lambo_obj.name = "lambo"

# self -- is a special variable used within context0f oop's

tesla_obj.drive()
lambo_obj.drive()