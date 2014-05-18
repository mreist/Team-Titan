import spyral 
import random
import math
import Vehicle
import Options
import Race
import Garage
import LeaderBoard
import TextInterface
import Model
from Model import resources

from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class RaceSelect(spyral.Sprite):
    def __init__(self, Scene):
        super(RaceSelect, self).__init__(scene)
        Model.loadResources()

        self.anchor = 'center'
        self.RaceSelect = Model.RaceSelect
        self.background  = spyral.Image(size=SIZE).fill(WHITE)      
        
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

        #Sets Main MenuBackground and places Garage image
        self.background = spyral.Image(size=SIZE).fill(WHITE)
        self.NightImage = drawNightImage(self.scene)
        self.DayImage = drawDayImage(self.scene)
        self.SnowImage = drawSnowImage(self.scene)
        self.BeachImage = drawBeachImage(self.scene)
        self.PrehistImage = drawPrehistImage(self.scene)
        self.RRImage = drawRRImage(self.scene)
        
        #Creates the Start and Option button

       
        self.titleText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, WHITE), (WIDTH/2, 50), "Click The Race You Would Like To Play")
        self.titleText.anchor = 'center'
        self.titleText.layer = 'top'
        #self.dayText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 18, WHITE), (200, HEIGHT/2 - 100), "The day race uses addition and subtraction")
        #self.dayText.anchor = 'midleft'
        #self.nightText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 18, WHITE), (WIDTH - 100, HEIGHT/2 - 100), "The night race uses multiplication and division")
        #self.nightText.anchor = 'midright'
        #self.instructions1 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 100), 'Steer your vehicle into the questions you would like to answer.')
        #self.instructions2 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 130), 'Input your answers into the box that appears when you touch your question.')
        #self.instructions3 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 160), 'Answer questions as fast as you can to complete the race. ')
        #self.instructions4 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 190), 'The harder the questions are, the faster you will go! Do your best!')


       
