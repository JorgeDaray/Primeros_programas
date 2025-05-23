# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
from os import name, system
from time import sleep

WORDLIST_FILENAME = "words.txt"

ALFABETO = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = []
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guessedWord.append(secretWord[i])
        else:
            guessedWord.append(' _ ')
    newWord = ''.join(guessedWord)
    return newWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = []
    for i in range(len(ALFABETO)):
        if ALFABETO[i] not in lettersGuessed:
            availableLetters.append(ALFABETO[i])
    return ','.join(availableLetters)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    print("Welcome to Hangman")
    print("The secret word has", len(secretWord), "letters\n")
    i = 0
    while i < 8 and isWordGuessed(secretWord, lettersGuessed) == False:
        print("You have taken ", i, "/8 of your permitted guesses")
        print("You have not guessed the following letters:\n", getAvailableLetters(lettersGuessed))
        print(getGuessedWord(secretWord, lettersGuessed), "\n")
        letter = str(input("Guess a letter: "))

        if len(letter) == 1 and letter[0] in lettersGuessed:
            print("You already guessed that, try again:", getGuessedWord(secretWord, lettersGuessed))
            sleep(1)
            clear()
            continue
        else:
            for i in range(len(letter)):
                lettersGuessed.append(letter[i])

        if letter in secretWord:
            print("Your guess was correct:", getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Your guess was incorrect:", getGuessedWord(secretWord, lettersGuessed))

        sleep(1.5)
        clear()

        if letter not in secretWord:
            i = i + 1

    if isWordGuessed == True:
        print("You guessed the word with", i, "wrong guesses, congratulations")
    else:
        print("You have taken ", i, "/8 wrong guesses to get to:")
        print(getGuessedWord(secretWord, lettersGuessed))
        print("The secret word was:", secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)