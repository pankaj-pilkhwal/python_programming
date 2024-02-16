import logging as log
from xmlrpc.client import SERVER_ERROR

try:
    a = int(input("Enter a number: "))
    print(f"Multipliation table of {a} is : ")
    for i in range(1, 11):
        print(f"{a} X {i} = {a * i}")

    lis: list = [1, 2, 3]
    print(lis[5])   # will through index error as index 5 is out of range in our list of 3 elemnts
except ValueError as ve:
    log.error(ve)
    log.error("Invalid input given. Please enter a valid number")
except IndexError as ie:
    print(ie)

 # if we don't do exception handling than program will crash and won't run the next line of code.


try:
    a = 10/0
except ZeroDivisionError as zde:
    log.error("can not divide by 0")
    log.error(zde)
finally:
    log.info("finally block is executed even in case of exceptions.")


print("\nsome more line of code.")
print("End of program.")



