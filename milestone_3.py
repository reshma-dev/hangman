def guess_letter():
    while True:
        guess = input("Enter a single letter: ").strip()
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


if __name__ == "__main__":
    # Test one letter guess request from user
    guess = guess_letter()
    print(guess)
