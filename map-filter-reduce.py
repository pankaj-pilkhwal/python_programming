from functools import reduce

my_list = [1, 2, 4, 6, 4, 3, 7]

def cube():
    return 2**3

cubel = lambda x:x**3 # above funtion in lambda

def odd(x):
    if x%2==1:
        return x
    
oddl = lambda x: x%2==1 # above funtion in lambda


# Map
square_root = list(map(cube, my_list))


# Filter
odd_numbers = list(filter(oddl, my_list))


# Reduce
# temp = list(reduce)

print(square_root)
print(odd_numbers)


