# Alice Vichitthavong 
# CPSC 315
# Cheating Hangman 
# 5/13/13

def main():
    with open('dictionary.txt') as f:
        lines = f.read().splitlines()
    
    exitGame = 1
    while(exitGame == 1):       
        length = getWordLength(lines)
        guesses = getNumGuesses()
        
        remainingWords = getStartingWords(lines,length)
        status = getStartingStatus(length)
        lettersGuessed =[]
        gameOver = 0
        
        seeWordsRemaining = int(input("See count of words remaining during game play?(Enter 1 for yes, 0 for no): "))
        print()
        
        while(guesses > 0 and gameOver == 0):
            printGameStats(remainingWords,lettersGuessed,guesses,status,seeWordsRemaining)
            letter = promptGuess(lettersGuessed)
            lettersGuessed.append(letter)
            guesses -= 1
            
            remainingWords = getRemainingWords(letter,remainingWords,guesses,length)
            status = getStatus(remainingWords[0], lettersGuessed)
            print()
            
            if(letter in status):
                guesses += 1
            
            if("-" not in status):
                gameOver = 1
                print("You win!")
                print("The word was " + status) 
                exitGame = int(input("Play again?(Enter 1 for yes, 0 for no): ")) 
                print()     
                
            if(guesses == 0 and gameOver == 0):
                print("You lose!") 
                print("The word was "  + remainingWords[0])  
                exitGame = int(input("Play again?(Enter 1 for yes, 0 for no): "))      
                print()
    print("Thank you for playing!")
        
# Print available word lengths and prompt player for a length    
def getWordLength(lines):
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
def getNumGuesses():
    valid = 0
    while(valid == 0):
        n = int(input("Number of guesses: "))
        if(n > 0):
            return n

# return string of starting status of game    
def getStartingStatus(n):
    s = ""
    for i in range(0,n):
        s += "-"
    return s

# Return list of all words with length requested by player
def getStartingWords(lines,length):
    words = []
    for word in lines:
        if(word.__len__() == length):
            words.append(word)
    return words
     
# Print current game stats   
def printGameStats(wordFamily,lettersGuessed,guesses,status,seeWordsRemaining):
    if(seeWordsRemaining == 1):
        print("Remaining words: " + str(len(wordFamily)))
    print("Current game status: " + str(status) )
    print("Guesses remaining: " + str(guesses))
    print("Guesses made: " + str(lettersGuessed))
    
# Prompt player to guess a letter and return the letter
def promptGuess(lettersGuessed):
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

def getStatus(wf,lettersGuessed):
    status = ""
    for l in wf:
        if(l in lettersGuessed):
            status += l
        else: 
            status += "-"
    return status

if __name__ == '__main__': main()