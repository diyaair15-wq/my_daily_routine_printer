
n = int(input('Enter a decimal integer: '))

n1=n
n2=n

string2 = ('')
#loop for printing in reverse 
while(int(n1/2)!=0 ):
    i = str(n1%2)
    string2 = i + string2 
    n1=int(n1/2)
 
i = str(n1%2)
string2 = i + string2    

print(f"Binary representation of {n}: {string2}")



string3 = ('')

while(int(n2/8)!=0 ):
    i = str(n2%8)
    string3 = i + string3 
    n2=int(n2/8)

i = str(n2%8)
string3 = i + string3

print(f"Octal representation of {n}: {string3}")

