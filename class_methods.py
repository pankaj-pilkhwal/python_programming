class Employee:
    company = "Apple"

    def show(self):
        print(f'the name is {self.name} and company is {self.company}')

    @classmethod    # helps in directly changing class variables.
    def change_compnay(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "harry"
e1.show()
e1.change_compnay("TESLA")
e1.show()
print(Employee.company)
