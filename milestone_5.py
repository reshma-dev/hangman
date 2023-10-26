import random


class Hangman:
    """
    Hangman is a classic game in which a player thinks of a word
    and the other player tries to guess that word within a certain amount of attempts.

    This is an implementation of the game, where the computer thinks of a word
    and the user tries to guess it.

    The class uses the `random` module to pick a word from the word_list

    Parameters:
    ----------
    word_list: list
        List of words from which a word is randomly chosen by the program
        Optional argument, defaults to ["apple", "mango", "cherry"] if not specified
    num_lives: int
        Number of lives the player has at the start of the game.
        Optional argument, defaults to 5 if not specified

    Attributes:
    ----------
    __word: str
        The word to be guessed, picked randomly from the word_list
    __word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
    __num_letters_not_guessed: int
        The number of UNIQUE letters in the word that have not been guessed yet
    __num_lives: int
        The number of lives the player has
    __list_of_guesses: list
        A list of the guesses that have already been tried

    Methods:
    -------
    play_game()
        The only public method to be called to play the game with a word list
        This method puts the game logic together.
    __check_guess(letter)
        Checks if the letter is in the word.
    __ask_for_input()
        Asks the user for a guess.
        Continues to request for a letter until a valid, single alphabet character is entered.

    """

    def __init__(self, word_list=["apple", "mango", "cherry"], num_lives=5) -> None:
        self.__num_lives = num_lives

        self.__word = random.choice(word_list).lower()
        self.__word_guessed = list("_" * len(self.__word))

        self.__num_letters_not_guessed = len(set(self.__word))
        self.__list_of_guesses = []

    def __ask_for_input(self):
        """
        Ask user to guess one letter

        Validate that a single character is entered
        Validate that the entered letter is an alphabetical character

        If an already guessed letter is entered again, notify the user
        If a new guess is entered, call check_guess and add letter to guessed list
        """
        while True:
            letter = input("Enter a single letter: ").strip().lower()
            if not len(letter) == 1 or not letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter in self.__list_of_guesses:
                print("You already tried that letter!")
            else:
                self.__list_of_guesses.append(letter)
                self.__check_guess(letter)
                break

    def __check_guess(self, letter):
        """
        Checks if the letter is in the randomly chosen word.
        If it is, the corresponding '_' in the word_guessed list is replaced with the letter.
        If it is not, number of remaining lives is reduced by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked as a guess

        """
        if self.__word.find(letter) >= 0:
            print(f"Good guess! '{letter}' is in the word.")
            for i, character in enumerate(self.__word):
                if character == letter:
                    self.__word_guessed[i] = letter
            print(self.__word_guessed)
            self.__num_letters_not_guessed -= 1
        else:
            self.__num_lives -= 1
            print(f"Sorry, '{letter}' is not in the word")
            print(f"You have {self.__num_lives} lives left")

    def play_game(self):
        """
        Brings the game logic together

        Check if num_lives is 0.
        If it is, that means the game has ended and the user lost.

        Check if num_letters_not_guessed > 0.
        If it is, then to continue the game, call ask_for_input method.

        If the num_lives is not 0 and the num_letters_not_guessed is not greater than 0,
        that means the user has won the game.
        """
        print(self.__word_guessed)
        while True:
            if self.__num_lives == 0:
                print("You lost!")
                break
            elif self.__num_letters_not_guessed > 0:
                self.__ask_for_input()
            else:
                print("Congratulations! You won the game")
                break


if __name__ == "__main__":
    word_list = [
        "apple",
        "mango",
        "cherry",
        "blueberry",
        "strawberry",
        "blackberry",
        "pear",
        "satsuma",
    ]
    game = Hangman(word_list, 5)
    game.play_game()
