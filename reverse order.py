s = input('Enter text: ')
i = 0
count = 0
while i < len(s):
    if s[i].isdigit():
        count += 1
    i += 1
print(count)


