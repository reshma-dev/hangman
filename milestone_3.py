import random


def choose_word():
    word_list = ["apple", "mango", "cherry", "blueberry", "strawberry"]
    return random.choice(word_list)


def ask_for_input():
    while True:
        letter = input("Enter a single letter: ").strip()
        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


def check_guess(word, letter):
    letter = letter.lower()
    word = word.lower()

    if word.find(letter) >= 0:
        print(f"Good guess! '{letter}' is in the word.")
    else:
        print(f"Sorry, {letter} is not in the word. Try again")


if __name__ == "__main__":
    # Check whether the guess is in the word
    word = choose_word()
    guess = ask_for_input()

    check_guess(word, guess)
    print(f"Word: {word}, guess: {guess}")
