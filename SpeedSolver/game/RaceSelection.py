import spyral 
import Vehicle
import Race
import LeaderBoard
import TextInterface
import Model
from Model import resources

from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

   
class RaceSelect(spyral.Sprite):
    def __init__(self, Scene):
        super(RaceSelect, self).__init__(scene)
        Model.loadResources()

        self.anchor = 'center'
        self.RaceSelect = Model.RaceSelect
        self.background  = spyral.Image(size=SIZE).fill(WHITE)      

#Draws Night Icon        
class drawNightImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'topleft'
	    self.image = spyral.image.Image("images/Night.png")
	    self.pos = (WIDTH/3, 0)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RaceSelect = "Night"
            spyral.director.pop
            if Model.SelectMode == "Race":
                spyral.director.push(Race.RaceScene())
            else:
                spyral.director.push(LeaderBoard.LeaderboardScene())

#Draws Day Icon
class drawDayImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'topleft'
	    self.image = spyral.image.Image("images/Day.png")
	    self.pos = (0, 0)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RaceSelect = "Day"
            spyral.director.pop
            if Model.SelectMode == "Race":
                spyral.director.push(Race.RaceScene())
            else:
                spyral.director.push(LeaderBoard.LeaderboardScene())
            
#Draws Snow Icon        
class drawSnowImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'topleft'
	    self.image = spyral.image.Image("images/Snow.png")
	    self.pos = (WIDTH*2/3, 0)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RaceSelect = "Snow"
            spyral.director.pop
            if Model.SelectMode == "Race":
                spyral.director.push(Race.RaceScene())
            else:
                spyral.director.push(LeaderBoard.LeaderboardScene())
                

#Draws Beach Icon
class drawBeachImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'topleft'
	    self.image = spyral.image.Image("images/Beach.png")
	    self.pos = (0, HEIGHT/2)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RaceSelect = "Beach"
            spyral.director.pop
            if Model.SelectMode == "Race":
                spyral.director.push(Race.RaceScene())         
            else:
                spyral.director.push(LeaderBoard.LeaderboardScene())
            
            
#Draws Prehistoric Icon            
class drawPrehistImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'topleft'
	    self.image = spyral.image.Image("images/Prehistoric.png")
	    self.pos = (WIDTH/3, HEIGHT/2)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RaceSelect = "PreHist"
            spyral.director.pop
            if Model.SelectMode == "Race":
                spyral.director.push(Race.RaceScene())
            else:
                spyral.director.push(LeaderBoard.LeaderboardScene())


#Draws Rainbow Road Icon  
class drawRRImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'topleft'
	    self.image = spyral.image.Image("images/Rainbow.png")
	    self.pos = (WIDTH*2/3, HEIGHT/2)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	


    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RaceSelect = "RR"
            spyral.director.pop
            if Model.SelectMode == "Race":
                spyral.director.push(Race.RaceScene())            
            else:
                spyral.director.push(LeaderBoard.LeaderboardScene())      

class RaceSelection(spyral.Scene):
    def __init__(self):
        global manager
        super(RaceSelection, self).__init__(SIZE)

        #Allows users to quit game via quit button or esc key
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.layers = ["bottom", "top"]

        self.background = spyral.Image(size=SIZE).fill(WHITE)
        self.NightImage = drawNightImage(self.scene)
        self.DayImage = drawDayImage(self.scene)
        self.SnowImage = drawSnowImage(self.scene)
        self.BeachImage = drawBeachImage(self.scene)
        self.PrehistImage = drawPrehistImage(self.scene)
        self.RRImage = drawRRImage(self.scene)


       
