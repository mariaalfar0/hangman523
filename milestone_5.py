import random


class Hangman:
    '''
    Initialises the Hangman game.
    
    A Hangman Game that asks the user for a letter and checks 
    if it is in the word. It starts with a default number of 
    lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed 
        list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.

        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.num_letters = self.num_letters - 1
            for idx, val in enumerate(self.word):
                 if self.word[idx] == guess:
                    self.word_guessed[idx] = val
                          
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Asks the user for an input, and checks whether is it valid. 
        
        To be valid, the input needs to be one single alphabetic character
        that has not already been guessed. If the letter has not been guessed, 
        it appends this guess to the list of guessed letters.

        """
        while True:
            guess = input("Please enter your guess: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """
    Runs the Hangman game. 
    
    The player starts with 5 lives, and the function
    takes a word list as an argument.
    
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
    
    print("Thanks for playing, the game is over.")

if __name__ == '__main__':
    word_list = ['banana', 'mango', 'satsuma', 'maracuja', 'kiwi']
    play_game(word_list)
# %%

 
    
    
