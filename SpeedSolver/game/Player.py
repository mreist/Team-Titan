import spyral

currentTime = 0
bestTime = 10000000
tokens = 0

class Player(spyral.Sprite):
    def __init__(self, highscore, vehicle):
        spyral.Sprite.__init__(self)