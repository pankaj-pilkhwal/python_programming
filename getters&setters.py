class Parent:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        print("getter is called...")
        return self._name
    
    @name.setter
    def name(self, name):
        print("setter is called")
        self._name = name


p = Parent()
print(p.name)
p.name = "Pankaj Pilkhwal"
print(p.name)

