import random

# TODO: Add Docstring


class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
        self.__word_list = word_list
        self.__num_lives = num_lives

        self.__word = random.choice(word_list).lower()
        self.__word_guessed = list("_" * len(self.__word))

        self.__num_letters_not_guessed = len(
            set(self.__word) - set(str(self.__word_guessed))
        )
        self.__list_of_guesses = []

    def __ask_for_input(self):
        while True:
            letter = input("Enter a single letter: ").strip()
            if not len(letter) == 1 or not letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter in self.__list_of_guesses:
                print("You already tried that letter!")
            else:
                self.__list_of_guesses.append(letter)
                self.__check_guess(letter)
                break

    def __check_guess(self, letter):
        letter = letter.lower()

        if self.__word.find(letter) >= 0:
            print(f"Good guess! '{letter}' is in the word.")
            for i, character in enumerate(self.__word):
                if character == letter:
                    self.__word_guessed[i] = letter
            print(self.__word_guessed)
        else:
            self.__num_lives -= 1
            print(f"Sorry, '{letter}' is not in the word")
            print(f"You have {self.__num_lives} lives left")

    def play_game(self):
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
    word_list = ["apple", "mango", "cherry", "blueberry", "strawberry"]
    game = Hangman(word_list, 5)
    game.play_game()
