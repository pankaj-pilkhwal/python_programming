names: list = ["pankaj", "neeraj", "shivani", "ankit", "harshit"]

for index, name in enumerate(names):
    print(name)
    if index == 0:
        print(f'{index} => {name} is awesome programmer.') 


for index, name in enumerate(names, start=1):
    print(name)
    if index == 1:
        print(f'{index} => {name} is awesome programmer.')