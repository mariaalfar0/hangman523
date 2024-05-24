import random

word_list = ['banana', 'mango', 'satsuma', 'maracuja', 'kiwi']
word = random.choice(word_list)

game_state = True


def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        

def ask_for_input():
    while game_state == True:
        guess = input("Please enter your guess: ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
    
    check_guess(guess)

ask_for_input()