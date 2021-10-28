'''Create a program that will echo everything the user enters 
until the user types "exit" which will finish.'''

while True:
    word = input('Write a word or write "exit" to finish: ')
    if word != 'exit':
        print(word)
    else:
        break
