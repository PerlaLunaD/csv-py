# First python game

import random
from sys import exit

# Game setup
wins = 0
looses = 0
ties = 0

computerOptions = ['quit', 'rock', 'paper', 'scissors']


def get_player_move():
    print('Lets play paper scissors rock! \nEnter your choice as: rock, paper, scissors or quit :')
    player_input = input()

    # Print out what user selected vs
    if player_input not in computerOptions:
        print('Oops, that option is not valid. Try again')
        player_input = input()
    if player_input == 'quit':
        print('Ok, game cancelled')
        exit()
    else:
        print(f'{player_input.title()} versus...')
        return player_input


def log_user_move():
    computer_move = computerOptions[random.randint(1, 3)]
    print(f'{computer_move.upper()}')
    return computer_move


def check_result(player, computer):
    print(f'playerMove is: {player} and computerMove is: {computer}')
    if playerMove == computerMove:
        print('Is a tie')

    elif playerMove == 'rock' and computerMove == 'scissors':
        print('you win')

    elif playerMove == 'paper' and computerMove == 'rock':
        print('you win')

    elif playerMove == 'scissors' and computerMove == 'paper':
        print('you win')

    elif playerMove == 'rock' and computerMove == 'paper':
        print('you lose!')

    elif playerMove == 'paper' and computerMove == 'scissors':
        print('you lose!')

    elif playerMove == 'scissors' and computerMove == 'rock':
        print('you lose!')


playerMove = get_player_move()
computerMove = log_user_move()
check_result(playerMove, computerMove)

