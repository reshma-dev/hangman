import random


def choose_word():
    word_list = ["apple", "mango", "cherry", "blueberry", "strawberry"]
    return random.choice(word_list)


if __name__ == "__main__":
    for i in range(10):
        word = choose_word()
        print(word)
