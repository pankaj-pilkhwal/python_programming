class Student:
    # name: str
    # age: int
    # city: str

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


pankaj = Student("Pankaj", 28, "Pune")
print(pankaj.age)


num = 1_00_000
print(num)