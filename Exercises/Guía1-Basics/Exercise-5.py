'''Create a program that asks for the user's name and after the 
user enters it, it shows on the screen <NAME> has <n> letters.'''

NAME = input('Enter your name: ')
n = len(NAME) 

print(f'{NAME} has {n} letters.')
