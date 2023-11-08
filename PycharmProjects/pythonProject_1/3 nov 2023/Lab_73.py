#### OOP's

# class and object in python

# person---
# attributes- name. age, height, weight, gender
# methods ---run, sleep, sing, talk, eat, walk, learn, hear

#objects
# amit, durga, santosh


class Person:
    # attributes
    name = None
    age = None
    gender = None
    prof = None
    height = None
    phone = None

    #methods
    def talk(self):
        print("i can talk ")

    def sleep(self):
        print("i can slepp ")

    def walk(self):
        print("i can walk ")

    def eat(self):
        print("i can eat ")

amit_obj = Person()
amit_obj.name="amit"
amit_obj.age=29
amit_obj.phone= 8952658652

amit_obj.sleep()
amit_obj.walk()
amit_obj.talk()

print(amit_obj)
# -----------------------------------------------

durga_obj = Person()
durga_obj.name="durga"
print(durga_obj)