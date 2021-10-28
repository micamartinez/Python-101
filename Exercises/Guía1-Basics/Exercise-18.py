''' Create a program that asks the user for a word and then displays 
the letters of the word entered one by one, starting with the last one.'''

word = input('Enter a word: ')

for letter in reversed(word):
    print(letter)
