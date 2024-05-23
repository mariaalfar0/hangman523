import random

word_list = ['banana', 'mango', 'satsuma', 'maracuja', 'kiwi']

word = random.choice(word_list)

guess = input("Please guess a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")