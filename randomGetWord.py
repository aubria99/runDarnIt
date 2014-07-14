import random #importing a library from python

holder = []

#this will randomly get a word from the array
def getWord(catDictionary):
    position = random.randint(0, len(catDictionary))
    return catDictionary[position]

#this will get the number of turns needed to get perfect on the game
def getTurnsNeed(playWord):
    for letter in playWord:
        if letter not in holder:
            holder.append(letter)

    return len(holder)
