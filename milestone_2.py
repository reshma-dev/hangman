import random

word_list = ["apple", "mango", "pear", "blueberry", "strawberry"]
print("List of words:", word_list)

word = random.choice(word_list)
print("Random word: ", word)

guess = input("Enter a single letter: ")

# A string is alphabetic if all characters in the string are alphabetic 
# and there is at least one character in the string.
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")