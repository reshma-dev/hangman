import random

def check_guess(guess):
    guess = str(guess).lower()

    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"Good guess! {guess}")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        # If the guess does not pass the checks, then print a message
        print("Invalid letter. Please, enter a single alphabetical character.")

def ask_for_input():
    guess = input("Guess a letter: ")
    check_guess(guess)


word_list = ["apple", "mango", "pear", "blueberry", "strawberry"]
print("List of words:", word_list)

word = random.choice(word_list)
print("Random word: ", word)

while True:
    ask_for_input()