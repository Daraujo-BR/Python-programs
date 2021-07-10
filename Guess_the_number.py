#adivinhar o numero (ta perto? é multiplo, outras dicas)
#Colocar as instruções
#Colocar as outras dicas!
import random
user = []
number = random.randint(1,100)
print(number)
while user!= number: 
    user = int(input('What number you think it is?'))
    if user < number:
        print('The number is higher! Give it another try! ')
    else: 
        print('The number is smaller! Give it another try! ')
if user == number:
        print('Congratulations!')