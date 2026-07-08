string = input("Enter any word: ")
character = input("Enter a character to count: ")
i = 0
count = 0
while i < len(string):
    if string[i] == character:
        count += 1
    i += 1
print(f"The character '{character}' appears {count} times in the word '{string}'.")