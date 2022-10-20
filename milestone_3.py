import random

word_list = ["apple", "mango", "pear", "blueberry", "strawberry"]
print("List of words:", word_list)

word = random.choice(word_list)
print("Random word: ", word)

while True:
    guess = input("Guess a letter: ")
    
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"Good guess! {guess}")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        # If the guess does not pass the checks, then print a message
        print("Invalid letter. Please, enter a single alphabetical character.")