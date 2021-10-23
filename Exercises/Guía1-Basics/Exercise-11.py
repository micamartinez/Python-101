'''Create a program that stores the password string in
a variable, ask the user for the password and print on screen if the
password entered by the user matches the one stored in the variable.'''

password = 'password'
user = input('Password: ')

while True:
	if password == user:
		print('The passwords match.')
		break
	else:
		print('The passwords do not match.')
		user = input('Password: ')
		
