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
            
            remainingWords = getRemainingWords(guess,remainingWords,numOfGuesses,wordLength)
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
def promptForWordLength(lines):
    wordLengths =[];  
    for i in lines:
        n = i.__len__()
        if(n not in wordLengths):
            wordLengths.append(n)
             
    wordLengths.sort()
    print("Available word lengths")
    print(wordLengths)
    print()
    
    valid = 0
    while(valid == 0):
        n = int(input("Enter word Length: "))
        if(n in wordLengths):
            return n

# Prompt user for starting number of guesses
def promptForNumberOfGuesses():
    valid = 0
    while(valid == 0):
        n = int(input("Number of guesses: "))
        if(n > 0):
            return n

# return string of starting status of game    
def initializeWordStatus(n):
    s = ""
    for i in range(0,n):
        s += "-"
    return s

# Return list of all words with length requested by player
def initializeRemainingWords(lines,length):
    words = []
    for word in lines:
        if(word.__len__() == length):
            words.append(word)
    return words
     
# Print current game stats   
def printGameStats(wordFamily,lettersGuessed,guesses,status):
    print("Current game status: " + str(status) )
    print("Guesses remaining: " + str(guesses))
    print("Guesses made: " + str(lettersGuessed))
    
# Prompt player to guess a letter and return the letter
def promptForGuess(lettersGuessed):
    l = str(input("Guess a letter: " ))   
    if(l in lettersGuessed):
        valid = 0
        while(valid == 0):
            print("\nYou already guessed " + l)
            l = str(input("Guess another letter: "))
            if(l not in lettersGuessed):
                return l
    return l  
 
# Return the list of words remaining that player can guess from
def getRemainingWords(letter, wordFamily,guesses,length):   
    wordFamilies = dict()
    for word in wordFamily:
        s = ""
        for l in word:
            if(l == letter):
                s += letter
            else:
                s += "-"
                
        if(s not in wordFamilies):
            wordFamilies[s] = 1
        else:
            wordFamilies[s] = wordFamilies[s] + 1
    
    familyToReturn = ""
    for i in range(0,length):
        familyToReturn += "-"
        
    words = []
    if(guesses == 0 and familyToReturn in wordFamilies):
        for word in wordFamily:
            wf = ""
            for l in word:
                if(l == letter):
                    wf += letter
                else:
                    wf += "-"
            if(wf == familyToReturn):
                words.append(word)
    else:
        familyToReturn = ""
        maxCount = 0
        for wf in wordFamilies:
            if wordFamilies[wf] > maxCount:
                maxCount = wordFamilies[wf]
                familyToReturn = wf
        
        for word in wordFamily:
            wf = ""
            for l in word:
                if(l == letter):
                    wf += letter
                else:
                    wf += "-"
            if(wf == familyToReturn):
                words.append(word)
    return words

def getWordStatus(wf,lettersGuessed):
    status = ""
    for l in wf:
        if(l in lettersGuessed):
            status += l
        else: 
            status += "-"
    return status

def printCountOfRemainingWords(remainingWords):
    print("Remaining words: " + str(len(remainingWords)))

if __name__ == '__main__': main()