'''Create a program in which the user is asked for a phrase and a letter, 
and displays the number of times the letter appears in the phrase on the screen.'''

phrase = input('Write a phrase: ')
letter = input('Write a letter: ')

print(f'The letter {letter} appears {phrase.count(letter)} times in the phrase.')
