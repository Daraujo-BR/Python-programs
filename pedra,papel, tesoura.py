import random

jogada = ['Rock','Paper','Scissors']
computer_choose = random.choice(jogada)
user = input('Choose one of pedra,papel, tesoura?')
if computer_choose == 'Rock':
    if user.capitalize() == 'Paper':
        print(f'Oh no! You won! I choose {computer_choose}!')
    elif user.capitalize() == 'Scissors':
        print(f'Yeah! You lost! I choose {computer_choose}!')
    else:
        print(f'It is a draw! I choose {computer_choose} too!') 
#Tentar fazer em formato de objeto orientado
#Colocar as demais escolhas
#Colocar em ingles
#Colocar as instruções too
#Acertar pq tá errado