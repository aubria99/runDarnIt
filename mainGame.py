import webapp2
import blankWord
import docPoint
import highBase
import randomGetWord
import cgi
import time
from inputValid import validString
from google.appengine.api import users

subCat = #get the array of words here...
gameWord = randomGetWord.getWord(subCat)
gameBlank = blankWord.createBlanks(gameWord)

turnsNeeded = randomGetWord.getTurnsNeeded(gameWord)
turnsTake = 0
lifePoints = 6
highScore = 0
seconds = 0

begin = time.time() #gets the time in seconds past

if user.get_current_users(): #if the user is online (which they should) use that nickname
    player = user.nickname()
else: #if not, use one of the following names here
    player = randomGetWord.getWord(["Ghost", "Stat", "Star"])

class MainGame(webapp2.RequestHandler):
    def get(self):
        self.response.header['Content-Type'] = 'text/plain'
        self.response.write(blankWord.printBlanks(gameBlank))
        self.response.write("Please enter a letter or a word in the box below.")

class PlayGame(webapp2.RequestHandler):
    def post(self):
        userInput = cgi.escape(self.request.get('content'))
        
        if(!inputValid.validString(userInput, gameWord)): #if the input is invalid, enter again
            self.response.write("Invalid input! Remember, only letters and guess of equal length of the word allowed.")
        else:
            if lifePoints != 0: #continue the game as long as all life has not been lost
                nextStep = docPoint.dieOrLive(userInput)
            else:
                nextStep = "Die"
                
            if(nextStep == "Cont"): #letter guess was correct, turn used, continue game
                turnsTake += 1
                gameBlank = blankWord.updateBlank(gameWord, gameBlank, userInput)
                
            elif(nextStep == "Win" or gameBlank == gameWord): #word guessed or correctly or all letter guessed, end game
                end = time.time() #gets the time in seconds
                seconds = int(end - begin)
                highScore = ((turnsTake - turnsNeeded) * (6 - lifePoints)) + seconds
                self.response.write("You Won!")
                highBase.enterScore(player, subCat, highScore)
                
            else:
                if(nextStep == "Point"): #incorrect letter guess, deduct point, continue game
                    turnsTake += 1
                    lifePoints -= 1
                else: #all life used or incorrect word guess, terminate game
                    lifePoints = 0
                    highScore = ((turnsTake - turnsNeeded) * (6 - lifePoints)) + seconds
                    self.response.write("You Lost...")
                    

        self.response.write(blankWord.printBlanks(gameBlank))

application = webapp2.WSGIApplication([('/', MainGame), ('/enter', PlayGame),]debug = True)

