# Create a program that displays the multiplication table from 1 to 10 on the screen.

for i in range(1,11):
    print(f'Multiplication table of {i}')
    for j in range(10):
        table = i * j
        print(f'{i} * {j} = {table}')
