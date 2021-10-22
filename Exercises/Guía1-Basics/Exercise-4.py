'''Create a program that asks for the user's name and a whole number
and print on the screen,in different lines, the name of the user so many times
as the number entered.'''

name = input('Name: ')
number = int(input('Enter a whole number: '))

for i in range(number):
    print(name)
    
