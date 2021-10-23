'''Create a program for a company that has game rooms for
all ages and wants to automatically calculate the price to charge to their
customers. The program should ask the user the age of the client and show
the price of the ticket. If the client is under 4 years old, they can enter for free, if they are
between 4 and 18 years old they must pay 500 and if they are over 18 years old, 1000.'''

age = int(input('Enter your age: '))

if 0 < age < 4:
	print('Free ticket.')
elif 4 <= age < 18:
	print('You must pay 500 pesos')
elif 18 <= age:
	print('You must pay 1000 pesos')
else:
	print('You did not enter a correct number')
