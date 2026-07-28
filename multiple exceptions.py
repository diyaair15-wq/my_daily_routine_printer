try:
    num1,num2 = eval(input("enter two numbers and use a coma to seperate"))
    result = num1/num2
    print("result is",result)

except ZeroDivisionError:
    print("division by 0 is error")
    
except SyntaxError:
    print("comma is missing")
    
else:
    print("no exceptions")
    
finally:
    print("this will execute no matter what")