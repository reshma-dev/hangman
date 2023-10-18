import random


def choose_word():
    word_list = ["apple", "mango", "cherry", "blueberry", "strawberry"]
    return random.choice(word_list)


def guess_letter():
    while True:
        guess = input("Enter a single letter: ").strip()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


if __name__ == "__main__":
    # Check whether the guess is in the word
    word = choose_word()
    guess = guess_letter()
    print(f"Word: {word}, guess: {guess}")

    if word.lower().find(guess.lower()) >= 0:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")
