# multi level inheritance

class grandparent:
    def grandparent_method(self):
        return "grandparent's method"

class Parent(grandparent):
    def parent_method(self):
        return "parentd's method"

class child(Parent):
    def cild_method(self):
        return "child's method"

child = child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
