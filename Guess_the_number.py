'''The idea behind the code
The computer choose a number between 1 and 100, try to know what number is it. Don't worry, the computer will give you some clues to help.
'''

import random
#Creating the variable that saves the value of user!
user = []
#Computer choose the random number
number = random.randint(1,100)
#Loop while user doesn't got the right number
while user!= number: 
    #User try to discover the number by the input
    user = int(input('What number you think it is?'))
    #Conditional if number is even
    if number % 2 == 0:
        print('The number is even!')
    #Conditional if number is odd
    else:
        print('The number is odd!')
    #Conditional to know if number that user tried is multiple of the number computer choose
    if number % user == 0:
        print(f'{user} is a multiple of the number')
    #Conditional to know if number that user tried is lower than the number computer choose
    if user < number:
        print('The number is higher! Give it another try! ')
    #Conditional to know if number that user tried is higher than the number computer choose
    else: 
        print('The number is smaller! Give it another try! ')
if user == number:
        print('Congratulations!')