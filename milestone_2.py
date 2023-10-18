import random


def choose_word():
    word_list = ["apple", "mango", "cherry", "blueberry", "strawberry"]
    return random.choice(word_list)


def guess_letter():
    while True:
        guess = input("Enter a single letter: ").strip()
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            return guess
        else:
            print("Oops! This is not a valid input, try again...")


if __name__ == "__main__":
    # Test random choice of word from list
    # for i in range(10):
    #     word = choose_word()
    #     print(word)

    # Test one letter guess request from user
    guess = guess_letter()
    print(guess)
