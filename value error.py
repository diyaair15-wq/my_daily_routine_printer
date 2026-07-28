try:
    num = int(input("enter a number"))
    print("the number entered is",num)
    
except ValueError as ex:
    print("exception:",ex)