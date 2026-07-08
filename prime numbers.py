lowwer = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

print("Prime numbers between", lowwer, "and", upper, "are:")
for num in range(lowwer, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)