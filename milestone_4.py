import random


class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list).lower()
        self.word_guessed = list("_" * len(self.word))

        self.num_letters_not_guessed = len(set(self.word) - set(str(self.word_guessed)))
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            letter = input("Enter a single letter: ").strip()
            if not len(letter) == 1 or not letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(letter)
                self.check_guess(letter)
                break

    def check_guess(self, letter):
        letter = letter.lower()

        if self.word.find(letter) >= 0:
            print(f"Good guess! '{letter}' is in the word.")
            for i, character in enumerate(self.word):
                if character == letter:
                    self.word_guessed[i] = letter
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word")
            print(f"You have {self.num_lives} lives left")


if __name__ == "__main__":
    word_list = ["apple", "mango", "cherry", "blueberry", "strawberry"]
    h = Hangman(word_list)
    print("Word guessed so far: ", h.word_guessed)
    print("Number of letters not guessed yet: ", h.num_letters_not_guessed)
    h.ask_for_input()
