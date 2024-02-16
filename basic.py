class Parent:
    a: int 
    b: int
    def set(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        print(self.a + self.b)
    


par = Parent()

par.set(10, 50)

par.sum()