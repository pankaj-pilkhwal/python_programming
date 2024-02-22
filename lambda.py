cube = lambda x: x**3

print(cube(10))


def hello(fx):
    print (f'hello, the lamdba gave {fx()}')

hello(lambda x=10: x**5)