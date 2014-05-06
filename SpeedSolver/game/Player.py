import spyral
import model
from model import resources
from spyral import Animation, easing

currentTime = 0
bestTime = 100000
tokens = 0
firstPlay = True
WithWheels = True

class PlayerVehicle(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.anchor = 'center'
        self.Vtype = model.Vtype
        self.image  = model.resources[self.Vtype]
        
if (WithWheels == True):        
    class PlayerLWheels(spyral.Sprite):
        def __init__(self, Scene):
            spyral.Sprite.__init__(self, Scene)
            try:
                self.anchor = 'center'
                self.LWtype = model.LWtype
        
                self.image  = model.resources[self.LWtype]
            except (KeyError, AttributeError):
                print "Nothing1"
            
    class PlayerRWheels(spyral.Sprite):
        def __init__(self, Scene):
            spyral.Sprite.__init__(self, Scene)
            try:
                self.anchor = 'center'
                self.RWtype = model.RWtype
         
                self.image  = model.resources[self.RWtype]
            except (KeyError, AttributeError):
                print "Nothing2"

