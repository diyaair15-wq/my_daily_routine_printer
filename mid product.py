num = int(input("Enter a number: "))
t = num
numlen = 0
while t > 0:
    numlen += 1
    t = int(t / 10)
if numlen >= 4:
   numlen = int(numlen / 2)
   chk = 0
   while numlen > 0:
       rem = num % 10
       if chk == numlen:
            midone = rem
       elif chk == numlen - 1:
           midtwo = rem
       num = int(num / 10)
       chk += 1
       prod = midone * midtwo    
       print("\nproduct of mid digits(" +str(midone) + " * " + str(midtwo) + ") is: " + str(prod))
else:
    print("The number is less than 4 digits, so it does not have middle digits to multiply.")
       