import spyral

currentTime = 0
bestTime = 100000
tokens = 0
firstPlay = True

class Player(spyral.Sprite):
    def __init__(self, highscore, vehicle):
        spyral.Sprite.__init__(self)
