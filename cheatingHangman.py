# Alice Vichitthavong 
# CPSC 315
# Cheating Hangman 

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
        gameIsOver = 0
        print()
        
        gameIsInProgress = numOfGuesses > 0 and gameIsOver == 0
        while(gameIsInProgress):
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
                print("You lose!") 
                print("The word was "  + remainingWords[0])  
                sessionIsOpen = int(input("Play again?(Enter 1 for yes, 0 for no): "))      
                print()
    print("Thank you for playing!")
   
# Print available word lengths and prompt player for a wordLength    
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
    
    isValidWordLength = 0
    while(isValidWordLength == 0):
        length = int(input("Enter word Length: "))
        if(length in wordLengths):
            return length

# Prompt user for starting number of guesses
def promptForNumberOfGuesses():
    while(1):
        guesses = int(input("Number of guesses(1-25): "))
        if(guesses > 0 and guesses < 26):
            return guesses

# return string of starting status of game    
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
     
# Print current game stats   
def printGameStats(wordFamily, lettersGuessed, guesses, status):
    print("Current game status: " + str(status) )
    print("Guesses remaining: " + str(guesses))
    print("Guesses made: " + str(lettersGuessed))
    
# Prompt player to guess a letter and return the letter
def promptForGuess(lettersGuessed):
    letter = str(input("Guess a letter: " ))   
    if(letter in lettersGuessed):
        while(1):
            print("\nYou already guessed " + letter)
            letter = str(input("Guess another letter: "))
            if(letter not in lettersGuessed):
                return letter
    return letter  
 
# Return the list of words remaining that player can guess from


def getRemainingWords(guess, remainingWords, numOfGuesses, wordLength):#letter, wordFamily, guesses, length):   
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
    
    familyToReturn = ""
    for i in range(0, wordLength):
        familyToReturn += "-"
        
    words = []
    if(numOfGuesses == 0 and familyToReturn in wordFamilies):
        for word in remainingWords:
            wordFamily = ""
            for letter in word:
                if(letter == guess):
                    wordFamily += guess
                else:
                    wordFamily += "-"
            if(wordFamily == familyToReturn):
                words.append(word)
    else:
        familyToReturn = ""
        maxCount = 0
        for wf in wordFamilies:
            if wordFamilies[wf] > maxCount:
                maxCount = wordFamilies[wf]
                familyToReturn = wf
        
        for word in remainingWords:
            wf = ""
            for l in word:
                if(l == guess):
                    wf += guess
                else:
                    wf += "-"
            if(wf == familyToReturn):
                words.append(word)
    return words

def getWordStatus(wordFamily,lettersAlreadyGuessed):
    status = ""
    for letter in wordFamily:
        if(letter in lettersAlreadyGuessed):
            status += letter
        else: 
            status += "-"
    return status

def printCountOfRemainingWords(remainingWords):
    print("DEBUG MODE Remaining words: " + str(len(remainingWords)))

if __name__ == '__main__': main()