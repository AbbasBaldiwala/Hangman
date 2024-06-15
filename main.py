import random as r
import art
import wordBank

def FillInLetters(wordToGuess: str, correctGuesses):
    blanksAndGuesses = ""
    counter = 0
    for char in wordToGuess:
        if char in correctGuesses:
            blanksAndGuesses += " " + char
        else:
            blanksAndGuesses += " _"
            counter += 1
    print(blanksAndGuesses)

    return counter

wordList = wordBank.word_list
userWon: bool = False

rand = r.randint(0, len(wordList) - 1)
word = wordList[rand]
correctGuesses = []
numLives = len(art.stages) - 1
print(art.logo)
while numLives > 0 and not userWon:
    guess: str = input("Guess a letter: ")
    if guess in word and guess not in correctGuesses:
        correctGuesses.append(guess)
    elif guess in correctGuesses:
        print("That letter was already guessed, Try again")
    else:
        numLives -= 1

    numUnderscores = FillInLetters(word, correctGuesses)
    if numUnderscores == 0:
        userWon = True
        print("You Win")
    print(art.stages[numLives])

if not userWon:
    print("GAME OVER, The correct word was:\n")
    correctWord = ""
    for char in word:
        correctWord += char + " "

    print(correctWord)




