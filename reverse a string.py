string = input("Enter a string: ")
string2 = ('')
for i in string:
    string2 = i + string2
print("the original string is:",string)
print("the reversed string is:",string2)