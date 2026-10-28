from random import random


class FruitQuiz:
    def __init__(self):
        self.fruits = {
            'Apple': 'red',
            'orange': 'orange',
            'watermelon': 'green',
            'banana': 'yellow',
            'grapes': 'purple',
            'peach': 'pink'}
    def quiz(self):
        while True:
            fruit,color = random.choice(list(self.fruits.items()))
            print("what is the color of {}?".format(fruit))
            user_answer = input("Your answer: ")
            if(user_answer.lower() == color):
                print("correct answer")
            else:
                print("wrong answer")
            option = int(input("enter 0, if you want to continue otherwise enter 1: "))
            if (option):
                break
print("welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()