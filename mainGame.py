import webapp2
import cgi
import time
import highBase
import wordFunctions
from google.appengine.api import users

subCat = #get the array of words here...
usedLet = []

gameWord = wordFunctions.getWord(subCat)
gameBlank = wordFunctions.createBlanks(gameWord)

turnsNeeded = wordFunctions.getTurnNeed(gameWord)
turnsTake = 0
life = 6
highScore = 0

begin = time.time() #gets the time in seconds past

if user.get_current_users(): #if the user is online (which they should) use that nickname
    player = user.nickname()
else: #if not, use one of the following names here
    player = wordFunctions.getWord(["Ghost", "Star"])

class MainGame(webapp2.RequestHandler):
    def get(self):
        self.response.header['Content-Type'] = 'text/plain'
        self.response.write(wordFunctions.printBlanks(gameBlank))
        self.response.write("Please enter a letter or a word in the box below.")
        self.response.write("\nYour life points: " + str(life))

class PlayGame(webapp2.RequestHandler):
    def post(self):
        userInput = cgi.escape(self.request.get('content'))

        """input validation and gameplay section"""       
        if not userInput.isalpha(): #input validation checking for only letters
            self.response.write("\nIncorrect Input. Only letters allowed.")

        elif userInput in usedLet: #ensures that a player doesn't guess the same thing
            self.response.write("\nYou already used that letter!")
        
        elif len(gameWord) == len(userInput): #checks to see if the words are of equal length, only valid word guess     
            if gameWord == userInput.tolower: #checks to see if the words are the same
                gameBlank = gameWord
            else:
                life = 0 #automatic loss
            turnsTake += 1
                    
        elif len(userInput) == 1: #checks to make sure that it is a valid letter guess
            if userInput in gameWord:
                gameBlank = wordFunctions.updateBlank(userInput.tolower(), gameWord, gameBlank) #this program does not deal with any upper case letters, guess converted to lowercase
            else:
                life -= 1 #bad guess, lose a life point
            usedLet.append(userInput) #adds the guess to the array to be compared later
            turnsTake += 1

        else: #input is invalid because you did not guess a word of equal length or a letter
            self.response.write("\nInvalid Input. Remember only guess a letter OR the entire word.\n")

        """game win or loss section"""
        if '_' not in gameBlank: #win condition, if all blanks are filled
            gameDone = True
            self.response.write("\nYou Won!")

        elif life == 0: #lose condition, if life goes to zero
            gameDone = True
            self.response.write("\nYou Died...")
            self.response.write("\nThe word was " + gameWord)

        """entering high score section"""
        if gameDone: #if the game is done, total high score and store it in database
            end = time.time() #gets the time in seconds
            highScore = ((turnsTake - turnsNeeded) * (6 - life)) + int(end - begin)
            highBase.enterScore(player, subCat, highScore)
            self.response.write("Your high score is : " + str(highScore))
        else: #ask for user input again
            self.response.write(wordFunctions.printBlanks(gameBlank))
            self.response.write("Please enter a letter or a word in the box below.")
            self.response.write("\nYour life points: " + str(life))
