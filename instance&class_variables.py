class Employee:
    company_name = "TATA Motors"        # class variable

    def __init__(self, name):
        self.name = name        # instance variable
        self.raise_percent = 5  # instance variable

    def show_details(self):
        print(f"company_name is: {self.company_name}, name is {self.name} and raise_percent is {self.raise_percent}.")


emp1 = Employee("Pankaj")
emp1.raise_percent  = 7

emp2 = Employee("Neeraj")

emp1.show_details()
emp2.show_details()


