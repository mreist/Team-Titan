import spyral
import Model
from Model import resources
from spyral import Animation, easing

currentTime = 0
bestTime = 100000
tokens = 10
firstPlay = True

DayTop10 = [['JFR', 1], ['MTR', 30], ['JTW', 60], ['NNA', 75], ['FAP', 1000], ['',1000000], ['',1000000], ['',1000000], ['',1000000], ['',1000000]]
NightTop10 = [['JFR', 2], ['MTR', 30], ['JTW', 60], ['NNA', 75], ['FAP', 1000], ['',1000000], ['',1000000], ['',1000000], ['',1000000], ['',1000000]]
SnowTop10 = [['JFR', 3], ['MTR', 30], ['JTW', 60], ['NNA', 75], ['FAP', 1000], ['',1000000], ['',1000000], ['',1000000], ['',1000000], ['',1000000]]
BeachTop10 = [['JFR', 4], ['MTR', 30], ['JTW', 60], ['NNA', 75], ['FAP', 1000], ['',1000000], ['',1000000], ['',1000000], ['',1000000], ['',1000000]]
PreHistTop10 = [['JFR', 5], ['MTR', 30], ['JTW', 60], ['NNA', 75], ['FAP', 1000], ['',1000000], ['',1000000], ['',1000000], ['',1000000], ['',1000000]]
RRTop10 = [['JFR', 6], ['MTR', 30], ['JTW', 60], ['NNA', 75], ['FAP', 1000], ['',1000000], ['',1000000], ['',1000000], ['',1000000], ['',1000000]]

LeaderBoards = [[DayTop10, 'Day'], [NightTop10, 'Night'], [SnowTop10, 'Snow'], [BeachTop10, 'Beach'], [PreHistTop10, 'PreHist'], [RRTop10, 'RR']]

WithWheels = True

class PlayerVehicle(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.anchor = 'center'
        self.Vtype = Model.Vtype
        self.image  = Model.resources[self.Vtype]
        
if (WithWheels == True):        
    class PlayerLWheels(spyral.Sprite):
        def __init__(self, Scene):
            spyral.Sprite.__init__(self, Scene)
            try:
                self.anchor = 'center'
                self.LWtype = Model.LWtype
        
                self.image  = Model.resources[self.LWtype]
            except (KeyError, AttributeError):
                print "Nothing1"
            
    class PlayerRWheels(spyral.Sprite):
        def __init__(self, Scene):
            spyral.Sprite.__init__(self, Scene)
            try:
                self.anchor = 'center'
                self.RWtype = Model.RWtype
         
                self.image  = Model.resources[self.RWtype]
            except (KeyError, AttributeError):
                print "Nothing2"

