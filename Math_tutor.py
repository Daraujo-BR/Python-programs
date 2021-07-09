'''The idea behind the code:
Create a program that the user is challenged to solve a number of math problems.
The user decide how many problems he/she wants to do, in addition, the user decides the maximum number used on each account. In the end, after solving and answering all the accounts, the user can see which accounts he/she got it right and wrong'''

#Greetings
print('Welcome to Math Tutor!')

import random
#Create function
def math_tutor():
    #Ask how many accounts the user wants to do
    qts_loop = int(input('Write how many accounts you want to do: '))
    #Create list with operators inside
    operators = ['+','-','*','/']    
    #List that will save the results
    results = []
    #loop following the number of accounts user wants to do
    for i in range(qts_loop):
        #math tutor choose which operator takes
        tutor_choose = random.choice(operators)
        #User choose the maximum number allowed in each account
        value_max = int(input(f'Choose the maximum value for the numbers {i+1}:'))
        #nº1 random
        n1 = random.randint(0,value_max)
        #nº2 random
        n2 = random.randint(0,value_max)
        #Ask the result to the user
        user = int(input(f'What is the result of: {n1} {tutor_choose} {n2}?'))
        #Conditions for operators
        if tutor_choose == '+':
            result = n1 + n2
        elif tutor_choose == '-':
            result = n1 - n2
        elif tutor_choose == '*':
            result = n1 * n2
        else:
            #Checking zero division error
            try:
                result = n1/n2
            except ZeroDivisionError():
                print('You cannot divide by zero!')
        #Checking if users get the answer right or wrong!
        if user == result:
            conclusion = 'You got it right'
        else:
            conclusion = 'You missed'
        #Print if user missed or give the right answer
        results.append(f'{conclusion}! Account {i+1}: {n1} {tutor_choose} {n2} = {result} \n')
    #Final: print each account and result
    together = '\n'.join(results)
    print(together)

#Call function
math_tutor()

#OQ falta (ideias):
# Mostrar o quanto acertou em %



        