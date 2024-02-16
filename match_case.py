num = int(input('Enter a number \n'))

match num:
    case 10: print(10)
    case 20: print(20)
    case _ if num < 50: print("num is less than 50")
    case default: print("This is default")


