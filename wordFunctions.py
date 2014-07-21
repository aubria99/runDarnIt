import random #random library supported by Python2.7

def getWord(possibleWords): #randomly selects the word that will be picked out of the array of strings and returns that word
    pos = random.randint(0, (len(possibleWords) - 1))
    return possibleWords[pos]

def createBlank(word): #creates the blanks to show the player based on the length of the word, returns the blank
    blank = ""
    for let in word:
        blank += '_'
    return blank

def getTurnNeed(word): #gets the unique occurence of a letter, returns the length of the array
    letInWord = []     #NOTE: for example, apple has a turns needed of 4 since p occurs twice
    for let in word:
        if let not in letInWord:
            letInWord.append(let)
    return len(letInWord)

def printBlank(blank): #prints those blanks with spaces so that the user can see the number of spaces, void function
    showWord = ""
    for let in blank:
        showWord += (let + ' ')
    print "\n" + showWord

def updateBlank(guess, word, blank): #when the player guesses a correct letter, the blanks are updated, returns the updated blank
    newBlank = ""
    for pos in range(len(word)): #NOTE: since word and blank are the same length, either or would word for this for loop
        if guess == word[pos]: #only replaces the blank with the letter guessed when the letter occurs in the word
            newBlank += word[pos]
        else:                  #otherwise, replace with the what is already in the blank
            newBlank += blank[pos]
    return newBlank
