'''The idea behind the code
How about you play the game 'Rock, paper,scissor' with the computer? It's pretty fun go ahead and try it!
'''
import random

# Creating list of elements and choose one
move = ['Rock','Paper','Scissors']
computer_choose = random.choice(move)

user = input('Choose one of Rock, Paper or Scissors?')
#Decision of computer and result
if computer_choose == 'Rock':
    if user.capitalize() == 'Paper':
        print(f'Oh no! You won! I choose {computer_choose}!')
    elif user.capitalize() == 'Scissors':
        print(f'Yeah! You lost! I choose {computer_choose}!')
    else:
        print(f'It is a draw! I choose {computer_choose} too!') 
if computer_choose == 'Paper':
    if user.capitalize() == 'Scissors':
        print(f'Oh no! You won! I choose {computer_choose}!')
    elif user.capitalize() == 'Rock':
        print(f'Yeah! You lost! I choose {computer_choose}!')
    else:
        print(f'It is a draw! I choose {computer_choose} too!') 
if computer_choose == 'Scissors':
    if user.capitalize() == 'Rock':
        print(f'Oh no! You won! I choose {computer_choose}!')
    elif user.capitalize() == 'Paper':
        print(f'Yeah! You lost! I choose {computer_choose}!')
    else:
        print(f'It is a draw! I choose {computer_choose} too!') 