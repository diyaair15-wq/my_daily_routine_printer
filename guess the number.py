import random
import time 

number=random.randint(1,100)

def intro():
    print('may i ask you for your name')
    global name
    name = input()
    if (number%2==0):
        x='even'
    else:
        x='odd'
    print('this is an {}number'.format(x))
    time.sleep(.5)
    print('go ahead.guess')
def pick():
    guessestaken = 0
    
    while guessestaken<6 :
        time.sleep(25.)
        enter=input("guess:")
        
        try:
            guess = int(enter)
            if guess<=100 and guess>=1:
                guessestaken=guessestaken+1
                
                if guessestaken<6:
                    if guesse<number:
                        print("the guess of the number that you have entered is too high ")
                    if guess!=number:
                        time.sleep(.5)
                        print("try again")
                    if guess==number:
                        break
                    
                if guess>100 or guess<1:
                    print('silly goose ,that number isn't in the range')
                    time.sleep(.25)
                    print("please enter a new number in the 1-100 range")
            except:
                 print("i think what you entered is a number,sorry")
        if guess==number:
            print("you guess corectly")
    playagain="yes"
    while playagain=="yes" or playagain=="y" or playagain=="Yes":
        intro()
        pick()
        print("do you want to play again")
        playagain=input()