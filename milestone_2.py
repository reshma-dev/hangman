import random

word_list = ["apple", "mango", "pear", "blueberry", "strawberry"]
print("List of words:", word_list)

word = random.choice(word_list)
print("Random word: ", word)

guess = input("Enter a single letter: ")