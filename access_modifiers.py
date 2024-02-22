# Priavte Access Modifier (used with double underscore)
class Employee:
    def __init__(self):
        self.__name = "Pankaj"  # double underscore makes it private.


pankaj = Employee()
# print(pankaj.__name)          # cannot access private variables directly. throws error

print(pankaj._Employee__name)   # private varialbes can be accessed indirectly like this. using name mangling

print(pankaj.__dir__())



# Protected Access Modifier (used with single underscore. It is just a naming convention and does not provide
#                                                           any protection or restrict any access to members)
class Student:
    def __init__(self):
        self._name = "Pankaj"
    
    def _funName(self):         # Protected method
        return "Pankaj Pilkhwal says hello!!!"


class Subject(Student): # Inherited Student class
    pass


obj1 = Student()
obj2 = Subject()

# calling by object of Student class
print(obj1._name)
print(obj1._funName())

# calling by object of Subject class
print(obj2._name)
print(obj2._funName())


