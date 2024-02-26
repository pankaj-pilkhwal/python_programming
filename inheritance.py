class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'the name is {self.name}')


class Dancer:
    def __init__(self, dance_type):
        self.dance_type = dance_type   

    def show(self):
        print(f'the dance type is {self.dance_type}')


class Person(Employee, Dancer):
    def __init__(self, name, dance_type):
        super().__init__(name)
        self.dance_type = dance_type

    def show(self):
        print(f'the name is {self.name} and the dance type is {self.dance_type}')


p1 = Person("Shivani", "Kathak")
p1.show()




