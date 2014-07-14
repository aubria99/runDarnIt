def dieOrLive(playWord, userGuess):
    if len(playWord) == len(userGuess):
        if playWord != userGuess:
            return "Die" #if die is returned, player losses remaining life
        else:
            return "Win" #if win is returned, the game will exit

    elif userGuess not in playWord:
        return "Point" #if point is returned, player losses a point

    return "Cont" #if cont is returned, the it is a correct guess; game continues
