'''Create a program that asks the user for an integer and displays
whether it is odd or even.'''

number = int(input('Enter a number: '))

if number % 2 == 0:
	print(f'{number} is even')
else:
	print(f'{number} is odd')
