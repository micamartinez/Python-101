'''Create a program that asks the user for an amount to invest, the
annual interest and the number of years, and display the capital obtained in the
investment'''

capital = float(input('Amount to invest: '))
annual_int = float(input('Annual interest: '))
years = float(input('Years to invest: '))

if annual_int > 1:
	annual_int = annual_int / 100
    		
capital_final = capital + capital * annual_int * years

print(capital_final)
