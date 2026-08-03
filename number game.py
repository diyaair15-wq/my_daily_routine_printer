import random
playing = True
number = str(random.randint(0, 9))

print("i will generate a random number between 0 and 9, and you have to guess it.")
print("the game ends when yo guess the number correctly.")
while playing:
    guess = input("guess the number: ")
    if   number == guess:
         print("you guessed it right!")
         break
    else:
        print("wrong guess, try again.")
        