#creates the blanks so that the user can guess the word
def createBlanks(playWord):
    blank = ""
    for letter in playWord:
        blank += '_'
    return blank

#this prints the blank with a letter so that the space can be seen
def printBlank(blank):
    temp = ""
    for letter in blank:
        temp += (letter + ' ')
    return temp

#this will update the blanks according to the user's guess
def updateBlank(playWord, blank, userGuess)
    temp = ""
    for pos in range(len(playWord)):
        if userGuess == playWord[pos: pos + 1]:
            temp += letter 
        else:
            temp += blank[pos: pos + 1]

    blank = temp
    return blank
