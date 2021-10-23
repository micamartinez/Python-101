'''Create a program that asks the user for their age and shows on the screen if
is of legal age or not, being 18 years of legal age.'''

age = int(input('How old are you? '))

if age >= 18:
	print('The user is of legal age')
else:
	print('The user is a minor')
