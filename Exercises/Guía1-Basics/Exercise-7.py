'''Create a program that asks the user for two whole numbers and displays by
screen dividing <n> into <m> gives a quotient <q> and a remainder <r> where <n> and <m>
are the numbers entered by the user, and <c> and <r> are the quotient and the rest of the
integer division respectively.'''

n = int(input('Enter a number: '))
m = int(input('Enter another number: '))
q = n // m 
r = n % m

print(f'The quotient is {q} and the remainder is {r}.')
