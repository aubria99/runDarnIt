from google.appengine.ext import ndb

DEFAULT_PLAYER = 'player'

def game_key(player = DEFAULT_PLAYER):
    return ndb.Key('PlayerName', player)

#class showing a single highscore entry
class scoreStore(nbd.Model):
    player = ndb.UserProperty()
    category = ndb.StringProperty()
    highScore = mdb.IntegerPropoert()

#puts data in the database
def enterScore(user, cat, score):
    scorStore(user = user, cat = cat, highScore = score).put()
        
