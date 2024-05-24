import random

word_list = ['banana', 'mango', 'satsuma', 'maracuja', 'kiwi']

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)

        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        This function checks if the user's guessed letter is in the secret word.

        Returns:
        - Whether guess is in the word
        - Whether guess has already been guessed
        - How many lives the user has left 

        """
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = str(guess)
                else:
                    continue  
            self.num_letters = self.num_letters - 1      
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        This function asks the user for an input, and checks whether is it valid. To be valid, 
        the input needs to be one single alphabetic character that has not already been guessed.
        If the letter has not been guessed, it appends this guess to the list of guessed letters.

        """
        while True:
            guess = input("Please enter your guess: ")
            if len(guess) == 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """
    This function runs the Hangman game. The player starts with 5 lives, and the function
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
    
    return "Thanks for playing, the game is over."

play_game(word_list)    
    
    
