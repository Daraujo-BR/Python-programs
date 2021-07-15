'''The idea behind the code
It's a simple program that prints a little story formed by the answes of users'''

import datetime

#Greetings
print('Welcome, talking about you...')
#Some questions that will form the story
name = input('What\'s your name? ')
age = int(input('How old are you? '))
food = input('What\'s your favorite food? ')
place = input('What\' the place would you like to visit? ')
people = input('Who would you like to be with? ')
do_there = input('What would you like to do there? ')
do_now = input('What are you doing right now? ')

#Print the story
print('About you:')
print(f'Hey guys, it is a pleasure to talk to you. My name is {name} and i am {age} years old. Now I would like to be in {place} with {people}, we would be eating {food}, my favorite food. There, I could {do_there}. But right now ({datetime.date.today()}) i am {do_now}!')