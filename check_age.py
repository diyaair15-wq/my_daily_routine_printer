age=int(input("Enter your age: "))
if age>10 and age<20:
    print("age is between 10 and 20")
elif age==10:
    print("age is 10")
elif age==20:
    print("age is 20")
else:
    print(f"user age is {age} and it's not in the specified range")