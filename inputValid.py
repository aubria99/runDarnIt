#operates the two input validation functions, returns true if valid and false if not.
def validString(userInput, playWord):
    valid = validChar(userInput)
    if valid:
        valid = validLength(userInput, playWord)
    return valid
    
#checks each indivdual letter to ensure it is a letter
def validChar(userInput):
    for letter in userInput:
        if not letter.isalpha():
            return False
    return True

#checks the length of a word, only characters or words of equal length to the word needing to be guessed 
def validLength(userInput, playWord):
    if len(userInput) == 1 or len(userInput) == len(playWord):
        return True
    return F
