import spyral 
import random
import math
import Vehicle
import Options
import Race
import Garage
import LeaderBoard
import TextInterface

from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


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

        self.instructions = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, WHITE), (WIDTH/2, 50), "Click The Race You Would Like To Play")
        self.instructions.anchor = 'center'


        #Functions that will take you to garage/game/options depending on which button is clicked
        spyral.event.register("form.RegisterForm.DayRaceButton.clicked", self.goToRace)
        spyral.event.register("form.RegisterForm.NightRaceButton.clicked", self.goToRace)
        
        
    def goToRace(self):
        spyral.director.pop
        spyral.director.push(Race.RaceScene())
