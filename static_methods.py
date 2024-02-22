class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b
    

# result = Math.add(1, 2)
# print(result)

# print(add(1, 10))
    
a = Math(5)
print(a.num)
b = a.add_to_num(6)
print(a.num)
print(a.add(10, 20))