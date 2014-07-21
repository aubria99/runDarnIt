from google.appengine.ext import ndb

DEFAULT_PLAYER = 'd_player'

def game_key(player = DEFAULT_PLAYER):
    return ndb.Key('PlayerName', player)

#class showing a single highscore entry
class scoreStore(nbd.Model):
    player = ndb.UserProperty() (required = True)
    category = ndb.StringProperty() (required = True)
    highScore = mdb.IntegerProporty() (required = True)

#puts data in the database
def enterScore(user, cat, score):
    scoreStore(user = user, cat = cat, highScore = score).put()
