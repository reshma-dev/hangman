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