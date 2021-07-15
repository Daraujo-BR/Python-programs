''' The idea behind the program:
At the beginning of the game, the user receives the value of 1000 dollars, his objective is to reach the maximum value (25,000 dollars)! If the black or green ball comes out, the user wins the amount that was bet, if the ball that comes out is red or white, the user loses the bet amount! The player loses the game if in any bet he loses half the amount he has in the previous round. After each round the user can decide whether or not to continue the game. GOOD GAME!'''

#Username
name = input('Welcome guest! What\'s your name?')
#Introduction!
print(f'It\'s nice to meet you, {name}! Take 1000 dollars, if you can reach 25000 dollars playing this game, it is all yours! If you do not reach that amount, what you win is all mine haha! Ah yes, if at any time you lose half of the total amount you had in the previous round, you lose the game! Good luck!')
#Function to call the game
def trade_game():
    import random
    #Bag that has the balls to remove at every bet (3x green - 5x red - 5 white - 10 black)
    #Win bet: green balls, black --------- Lose bet: white balls, red
    bag = ['white','white','white','white','white','red','red','red','red','red','green','green' ,'green','black','black','black','black','black','black','black','black','black','black']
    #Total $ at start of game
    balance = 1000
    #As long as the condition is ok, that is, until it finds a break, it will continue
    while True:
        #Always shuffle the bag in the loop
        random.shuffle(bag)
        #User puts how much he wants to bet
        bet = int(input('Enter the amount you want to bet: '))
        #Check if the bet is higher than what the user have in their wallet
        if bet <= balance:
        #Catch random ball
            marble_taken = random.choice(bag)
            #The amount that stores the bet win or loss starts at zero
            result = 0
            #Amount used to save the wallet amount before a new round
            value = balance
            #Condition if the ball is green, the stake wins
            if marble_taken == 'green' or marble_taken == 'black':
                result += bet
            else:
            #Condition if the ball is red, you lose bet amount
                result -= bet
            # Adds or takes away the value in the wallet from what was bet
            balance += result
            #Print which ball came out and the value in the wallet
            print(f'{marble_taken.upper()}! Portfolio value:{balance} dollars!')
            #Verification that the value in the line is less than or equal to half of what it had in the last round
            if balance <= value/2:
                print('You lost! Your wallet value is less than or equal to half what you had in the last round!')
                break
            #Checking if the cash value reached the maximum score
            if balance == 25000:
                print('Congratulations you reached or exceeded the maximum value! You are the best player in the world!')
                break
            #Ask the user if he wants to continue playing.
            decision = input('Do you want to continue the game? Type (YES) to continue, type any key to exit!')
            if decision.lower() == 'yes':
                continue
            else:
                break
         #Condition if you place a value greater than what you have in your portfolio
        else:
            print('You entered a value greater than what you have in your wallet!')
    #Compliments for playing
    print(f'Thanks for playing! Portfolio value: {balance} dollars')
#Function call
trade_game()