import random
import sys
# Group work by Nick Avelleyra, Jason Walsh, Patrick Whetham
answer = random.randint(1,10)
numofguesses = 0
guess = int(raw_input('Guess a number between 1 and 10: '))

while (numofguesses < 4):                        
    if (guess == answer):
        print 'You won'
        sys.exit()
        
    elif (abs(answer - guess) <= 3):
            print 'Warm'
            numofguesses += 1
            guess = int(raw_input('Guess another number between 1 and 10: '))
    elif (abs(answer - guess) > 3):
            print 'Cold'
            numofguesses += 1
            guess = int(raw_input('Guess a number between 1 and 10: '))

print 'You LOSE'
sys.exit()
