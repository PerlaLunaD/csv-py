# First python game

import random, sys

# Game setup
# options
# gameOptions = ['rock', 'paper', 'scissors', 'quit']

wins = 0
looses = 0
ties = 0

print('Lets play paper scissors rock! \nEnter your choice as: rock, paper, scissors or quit :')
playMover = input()

# Print out what user selected vs
if playMover == 'quit':
    print('Ok, game cancelled')
    sys.exit()
else:
    print(f'{playMover.title()} versus...')


compuMover = ['rock', 'paper', 'scissors', 'quit']

randomNumber = random.randint(1, 4)

if randomNumber == 1:
    compuMove = 'rock'
    print('ROCK')

elif randomNumber == 2:
    compuMover = 'paper'
    print('PAPER')

elif randomNumber == 3:
    compuMover = 'scissors'
    print('SCISSORS')




if playMover == compuMover:
    print('Is a tie')
    ties = ties + 1

elif playMover == 'rock' and compuMover == 'scissors':
    print('you win')
    wins = wins + 1

elif playMover == 'paper' and compuMover == 'rock':
    print('you win')
    wins = wins + 1

elif playMover == 'scissors' and compuMover == 'paper':
    print('you win')
    wins = wins + 1

elif playMover == 'rock' and compuMover == 'paper':
    print('you lose!')
    losses = looses + 1

elif playMover == 'paper' and compuMover == 'scissors:':
    print('you lose!')
    losses = looses + 1

elif playMover == 'scissors' and compuMover == 'rock':
    print('you lose!')
    looses = looses + 1
