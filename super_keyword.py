class Parent:
    def parent_method(self):
        # print("This is a super method from Parent class")
        pass


class GrandParent:
    def parent_method(self):
        # print("This is a from Grand Parent class")
        pass


class Child(GrandParent, Parent):
    def __init__(self):
        super().parent_method()


c = Child()



# next code
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


pankaj = Programmer("Pankaj Pilkhwal", 1234, "Java & Python")
print(pankaj.name)
print(pankaj.id)
print(pankaj.lang)