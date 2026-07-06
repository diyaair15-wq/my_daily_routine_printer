num = float(input("Enter a number: "))
n = int(input("Enter the power: "))
result = 1
for i in range(n):
    result *= num
print(f"{num} raised to the power of {n} is {result}")
