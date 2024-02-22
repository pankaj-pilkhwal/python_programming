class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def show_details(self):
        print(f'person name is {self.name} and his age is {self.age}.')

    @classmethod    # using class method as alternative constructor
    def from_str(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    


p1 = Person("Pankaj", 28)
p1.show_details()

p2 = Person.from_str("Neeraj, 25")
p2.show_details()