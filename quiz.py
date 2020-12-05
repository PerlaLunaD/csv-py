name= 'Goreti'

print(f'welcome to {name} choose your own adventure, as you follow the story. Enjoy the play, lets do it.')
print('you will find a room with two doors. The frist door is red and the second door is white')

door_choice = input('What door do you want to choose? \nRed door or White? :')
if door_choice == 'red':
    print('great, you walk through the red door and now you are in your own future.')

choice_one = input('what do you want to do? \nEnter 1 to accept or 2 to decline: ')
if choice_one == '1':
    print(f'{name} continue to the next level, good lucky')
else:
    print(f'{name} the game is over. Too bad')

choice_two = input('What box do you want to open? \nBox orange or Box yellow: ')
if choice_two == 'Box orange':
    print(' Take the key. Do you know what will open?')
    print('Find out in the last level')

choice_three = input('Are you ready for you gift? Choose one door: 1, 2, 3, 4, 5, 6: ?')
if choice_three == '3':
   print(f'Congratulates {name}, you are in front to next washing machine')
elif choice_three == '4':
   print(f'Congratulates {name}, you are in front to your stove')
elif choice_three =='1':
    print('You have won $100 dll')
else:
   print('You are where it all began!!')
   print('Better luck next time!')





# INPUT te permite escribir a tu eleccion, asignada a diferentes variables, puedes eleguir