import spyral
import Model
from Model import resources
from spyral import Animation, easing

#The Players time
currentTime = 0
bestTime = 100000
# Number of tokens a player has. 
#Tokens allow a player to buy items in the Garage such as new wheels, decays and vehicles.
tokens = 10

firstPlay = True
#Top ten players in the leaderboard
top10 = [['JFR', 1], ['MTR', 30], ['JTW', 60], ['NNA', 75], ['FAP', 1000], ['',1000000], ['',1000000], ['',1000000], ['',1000000], ['',1000000]]
WithWheels = True


#Player Vehicle class that has a Vtype and compares it to the Model.Vtype in order to display a particular vehicle
class PlayerVehicle(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.anchor = 'center'
        self.Vtype = Model.Vtype
        self.image  = Model.resources[self.Vtype]
        
#Player Decal class that has a Decal and compares it to the Model.Decal in order to display a particular Decal
class PlayerDecal(spyral.Sprite):
    def __init__(self, Scene):
        spyral.Sprite.__init__(self, Scene)
        self.anchor = 'center'
        self.Decal = Model.Decal
        self.image = Model.resources[self.Decal]

if (WithWheels == True):
    
    #Player LWheel class that has a LWheel and compares it to the Model.LWheel.
    #In order to display different Lwheel images
    class PlayerLWheels(spyral.Sprite):
        def __init__(self, Scene):
            spyral.Sprite.__init__(self, Scene)
            try:
                self.anchor = 'center'
                self.LWtype = Model.LWtype
        
                self.image  = Model.resources[self.LWtype]
            except (KeyError, AttributeError):
                print "Nothing1"
                
    #Player RWheel class that has a RWheel and compares it to the Model.RWheel.
    #In order to display different Rwheel images  
    
    class PlayerRWheels(spyral.Sprite):
        def __init__(self, Scene):
            spyral.Sprite.__init__(self, Scene)
            try:
                self.anchor = 'center'
                self.RWtype = Model.RWtype
         
                self.image  = Model.resources[self.RWtype]
            except (KeyError, AttributeError):
                print "Nothing2"

