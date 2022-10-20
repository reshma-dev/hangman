# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1: Setup the environment  

Python applications often use packages and modules that don’t come as part of the standard library. Virtual environments provide an isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.

- Create a virtual environment for the Hangman project
```console
   conda create -n hangman_env
```
- Activate the virtual environment
```console
   conda activate hangman_env
```

## Milestone 2: Create variables for the game  

This milestone makes use of basic Python data types like lists and constructs like if-else for checking conditions.  
Also makes use of a module ```random``` to pick a random word from our ```word_list```
- Define the list of possible words - ```word_list```
- Choose a random word from the list - ```word```
- Ask user for an input character and validate that a single alphabet character is entered - ```guess```  

## Milestone 3: Check if the guessed character is in the word  

This milestone introduces checks to determine whether the guessed letter is in the randomly chosen word or not  

Organise the code into functions: 
- ```check_guess(guess)``` 
  - In order to be able to match both capital and lowercase guesses, convert guess to lowercase
  - Validate if the guess is a single character and is an alphabet
  - Check if the letter is in the randomly chosen word
- ```ask_for_input()``` 
  - request user to input a character as a guess  

## Milestone 4: Create the game class  

Use the Object Oriented Programming (OOP) paradigm to develop the Hangman game

- Create the class to hold the following information
  - ```word```: str - the word to be guessed, picked randomly from the word_list
  - ```word_guessed```: list - initialised with '_' for each letter not yet guessed
  - ```num_letters```: int - the number of UNIQUE letters in the word that have not been guessed yet
  - ```num_lives```: int - the number of lives the player has at the start of the game
  - ```word_list```: list - a list of words
  - ```list_of_guesses```: list - a list of the guesses that have been tried  
  
- Define methods  
  - ```check_guess()```
    - Check if the guessed letter is found in the randomly chosen word
    - Update the remaining lives based on the above check
  - ```ask_for_input()```
    - To request for guesses
    - Validate the user input for length and type of character  

## Milestone 5: Putting it all together  
This finally puts it all together. Write a function to code the game logic using the ```Hangman``` class  

Logic: Keep requesting guesses one character at a time, until the game is over. The game ends when either:
- **Game lost** - there aren't any more lives left - ```num_lives == 0```
- **Game won** - the user gueeses the word correctly to win the game!