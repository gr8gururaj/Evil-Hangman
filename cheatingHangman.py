# Alice Vichitthavong 
# CPSC 315
# Cheating Hangman 

import re

def main():
    with open('dictionary.txt') as file:
        words = file.read().splitlines()
    
    #Turn on DEBUG_MODE by setting value to 1. Turn off by setting value to 0.
    #DEBUG_MODE displays number of words remaining after each guess is made by player.
    DEBUG_MODE = 1
    
    sessionIsOpen = 1
    while(sessionIsOpen): 
        wordLength = promptForWordLength(words)
        numOfGuesses = promptForNumberOfGuesses()
        
        remainingWords = initializeRemainingWords(words, wordLength)
        wordStatus = initializeWordStatus(wordLength)
        lettersAlreadyGuessed =[]
        print()
        
        gameIsOver = 0
        while(gameIsOver == 0):
            if(DEBUG_MODE == 1):
                printCountOfRemainingWords(remainingWords)
            
            printGameStats(remainingWords,lettersAlreadyGuessed,numOfGuesses,wordStatus)
            guess = promptForGuess(lettersAlreadyGuessed)
            lettersAlreadyGuessed.append(guess)
            numOfGuesses -= 1
            
            remainingWords = getRemainingWords(guess, remainingWords, numOfGuesses, wordLength)
            wordStatus = getWordStatus(remainingWords[0], lettersAlreadyGuessed)
            print()
            
            if(guess in wordStatus):
                numOfGuesses += 1
            
            if("-" not in wordStatus):
                gameIsOver = 1
                print("You win!")
                print("The word was " + wordStatus) 
                sessionIsOpen = int(input("Play again?(Enter 1 for yes, 0 for no): ")) 
                print()     
                
            if(numOfGuesses == 0 and gameIsOver == 0):
                gameIsOver = 1
                print("You lose!") 
                print("The word was "  + remainingWords[0])  
                sessionIsOpen = int(input("Play again?(Enter 1 for yes, 0 for no): "))      
                print()
                
    print("Thank you for playing!")
   
def promptForWordLength(words):
    wordLengths =[];  
    for word in words:
        length = word.__len__()
        if(length not in wordLengths):
            wordLengths.append(length)
             
    wordLengths.sort()
    print("Available word lengths")
    print(wordLengths)
    print()
    
    while(1):
        try:
            length = int(input("Enter word Length: "))
            if(length in wordLengths):
                return length
        except ValueError:
            print("Invalid input")   
            print() 

def promptForNumberOfGuesses():
    while(1):
        try:
            guesses = int(input("Number of guesses(1-20): "))
            if(guesses > 0 and guesses < 20):
                return guesses            
        except ValueError:
            print("Invalid input")   
            print() 

  
def initializeWordStatus(length):
    status = ""
    for i in range(0,length):
        status += "-"
    return status

# Return list of all words with length requested by player
def initializeRemainingWords(lines,length):
    words = []
    for word in lines:
        if(word.__len__() == length):
            words.append(word)
    return words
     
def printGameStats(wordFamily, lettersGuessed, guesses, status):
    print("Current game status: " + str(status) )
    print("Guesses remaining: " + str(guesses))
    print("Guesses made: " + str(lettersGuessed))
    
def promptForGuess(lettersGuessed):
    letter = str(input("Guess a letter: " )).lower()   
    pattern = re.compile("^[a-z]{1}$")
    isInvalidGuess = letter in lettersGuessed or re.match(pattern, letter) == None
    
    if(isInvalidGuess):
        while(1): 
            print()    
            if(re.match(pattern, letter) == None):
                print("Invalid guess. Enter a single character")
            if(letter in lettersGuessed):    
                print("\nYou already guessed " + letter)
           
            letter = str(input("Guess a letter: " ))  
            isValidGuess = letter not in lettersGuessed and re.match(pattern, letter) != None 
             
            if(isValidGuess):
                return letter
    return letter  

def getWordStatus(wordFamily,lettersAlreadyGuessed):
    status = ""
    for letter in wordFamily:
        if(letter in lettersAlreadyGuessed):
            status += letter
        else: 
            status += "-"
    return status

# Return the list of words remaining that player can guess from
def getRemainingWords(guess, remainingWords, numOfGuesses, wordLength):#letter, wordFamily, guesses, length):   
    wordFamilies = generateWordFamiliesDictionary(remainingWords, guess)
    
    familyToReturn = initializeWordStatus(wordLength)
    canAvoidGuess = numOfGuesses == 0 and familyToReturn in wordFamilies
    
    if(canAvoidGuess):
        familyToReturn = initializeWordStatus(wordLength)
    else:
        familyToReturn = findWordFamilyWithHighestCount(wordFamilies)

    words = generateListOfWords(remainingWords, guess, familyToReturn)
    return words

def generateWordFamiliesDictionary(remainingWords, guess):
    wordFamilies = dict()
    for word in remainingWords:
        status = ""
        for letter in word:
            if(letter == guess):
                status += guess
            else:
                status += "-"
                
        if(status not in wordFamilies):
            wordFamilies[status] = 1
        else:
            wordFamilies[status] = wordFamilies[status] + 1
    return wordFamilies
 
def generateListOfWords(remainingWords, guess, familyToReturn):
    words = []
    for word in remainingWords:
        wordFamily = ""
        for letter in word:
            if(letter == guess):
                wordFamily += guess
            else:
                wordFamily += "-"
                
        if(wordFamily == familyToReturn):
            words.append(word)
    return words

def findWordFamilyWithHighestCount(wordFamilies):
    familyToReturn = ""
    maxCount = 0
    for wordFamily in wordFamilies:
        if wordFamilies[wordFamily] > maxCount:
            maxCount = wordFamilies[wordFamily]
            familyToReturn = wordFamily
    return familyToReturn

def printCountOfRemainingWords(remainingWords):
    print("(DEBUG MODE ON)Remaining words: " + str(len(remainingWords)))

if __name__ == '__main__': main()