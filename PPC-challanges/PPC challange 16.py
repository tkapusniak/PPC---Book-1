#PPC Challange 16
import random
answer = random.randint(0,100)
guess = int(input('What is your guess?' ))
while guess != answer:
    if guess < answer:
        print('Go higher!')
    if guess > answer:
        print('Go lower!')
    guess = int(input('What is your guess? '))
print('You got it!')
