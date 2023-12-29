  # polymorphism---- oops cocept
  # ABC
  # exception

# polymorphism---- oop's cocept
# object-- behave differntly based on sitution   ---> thing----> person
  # person ---> speak, walk, sleep, think

class Shape:
    def area(self):
        print("area of shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self. length = length
        self. width = width

    def area(self):
        super(). area()
class Circle(Shape):
    def __init__(self, radius):   # constructer
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shape1= Rectangle(5,8)
print(shape1.area())

shape2= Circle(15)
print(shape2.area())

shape3= Shape()
print(shape3.area())