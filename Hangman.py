# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


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
            guessedWord.append(" _ ")
    newWord = " ".join(guessedWord)
    return newWord
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    Abecedario = string.ascii_lowercase
    letras_disponibles = []
    for i in range(len(Abecedario)):
        if Abecedario[i] not in lettersGuessed:
            letras_disponibles.append(Abecedario[i])
    return ",".join(letras_disponibles)

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
    palabra = secretWord
    print("Bienvenido al juego del ahorcado")
    print("La palabra secreta tiene: ", len(secretWord),"letras\n" )
    vidas = 7
    while vidas > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        fallas = 0
        print("Letras disponibles:",getAvailableLetters(lettersGuessed))
        print("Tu tienes",+vidas,"vidas disponibles ")
        print(getGuessedWord(secretWord,lettersGuessed))
        letter = input("enter a letter: ")
        if letter in lettersGuessed:
            print("Tu haz repetido esta palabra, intenta otra vez:")
            continue
        else:
            lettersGuessed.append(letter)
        if letter in palabra:
            print("Haz adivinado:", getGuessedWord(secretWord,lettersGuessed))
        else:
            fallas += 1
            print("Haz fallado:", getGuessedWord(secretWord,lettersGuessed))
        if letter not in palabra:
            vidas = vidas - 1

    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Haz ganado, Felicidades :) ")
    else:
        print(getGuessedWord(secretWord, lettersGuessed))
        print("Haz perdido, lo siento :( ")
        print("The secret word was:", secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
