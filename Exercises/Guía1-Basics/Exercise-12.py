'''Create a program that asks the user for two numbers and displays by
screen the division. If the divisor is zero, the program should return a message
indicating that it cannot be divided by 0.'''

number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter another number: '))

while True:
	if number_2 != 0:
		division = number_1 / number_2
		print(division)
		break
	else:
		print('Division by zero is not possible')
		number_2 = int(input('Enter another number: '))
