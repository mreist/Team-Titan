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
        spyral.Sprite.__init__(self, Scene)
        self.anchor = 'center'
        self.RaceSelect = Model.RaceSelect
        self.background  = Model.resources[self.RaceSelect]      
        

class RaceSelection(spyral.Scene):
    def __init__(self):
        super(RaceSelection, self).__init__(SIZE)

        #Allows users to quit game via quit button or esc key
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        #Sets Main MenuBackground and places Garage image
        self.background = spyral.Image("images/Background.png")

        #Creates the Start and Option button
        class RegisterForm(spyral.Form):
            DayRaceButton = spyral.widgets.Button("Day Race")
            NightRaceButton = spyral.widgets.Button("Night Race")

        my_form = RegisterForm(self)
        my_form.focus()
        my_form.DayRaceButton.pos = (WIDTH/2 - 100, HEIGHT/2)
        my_form.NightRaceButton.pos = (WIDTH/2 + 100, HEIGHT/2)
        
        self.titleText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, WHITE), (WIDTH/2, 50), "Click The Race You Would Like To Play")
        self.titleText.anchor = 'center'
        self.dayText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 18, WHITE), (200, HEIGHT/2 - 100), "The day race uses addition and subtraction")
        self.dayText.anchor = 'midleft'

        self.nightText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 18, WHITE), (WIDTH - 100, HEIGHT/2 - 100), "The night race uses multiplication and division")
        self.nightText.anchor = 'midright'

        self.instructions1 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 100), 'Steer your vehicle into the questions you would like to answer.')
        self.instructions2 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 130), 'Input your answers into the box that appears when you touch your question.')
        self.instructions3 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 160), 'Answer questions as fast as you can to complete the race. ')
        self.instructions4 = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, HEIGHT/2 + 190), 'The harder the questions are, the faster you will go! Do your best!')


        #Functions that will take you to garage/game/options depending on which button is clicked
        spyral.event.register("form.RegisterForm.DayRaceButton.clicked", self.goToDayRace)
        spyral.event.register("form.RegisterForm.NightRaceButton.clicked", self.goToNightRace)
        
        
    def goToNightRace(self):
        Model.RaceSelect = "Night"
        spyral.director.pop
        spyral.director.push(Race.RaceScene())
        
    def goToDayRace(self):
        Model.RaceSelect = "Day"
        spyral.director.pop
        spyral.director.push(Race.RaceScene())    
