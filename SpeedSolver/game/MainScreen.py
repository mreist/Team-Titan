import spyral 
import random
import math
import Instructions
import Vehicle
import Options
import Race
import Garage
import LeaderBoard
import RaceSelection

from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"



class drawGarageImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Garage.png")
	    self.pos = ((WIDTH/2), (HEIGHT/2)-200)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            spyral.director.pop
            spyral.director.push(Garage.GarageScene())

class MainMenu(spyral.Scene):
    def __init__(self):
        super(MainMenu, self).__init__(SIZE)
        
#Loads custom start/option buttons
        #self.load_style("game/style.spys")

#Allows users to quit game via quit button or esc key
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

#Sets Main MenuBackground and places Garage image
        self.background = spyral.Image("images/Background.png")
        self.GarageImage = drawGarageImage(self.scene)

#Creates the Start and Option button
        class RegisterForm(spyral.Form):
            StartGame = spyral.widgets.Button("Start Game")
            InstructionsButton = spyral.widgets.Button("Instructions")
#            OptionButton = spyral.widgets.Button("Options")
            LeaderboardButton = spyral.widgets.Button("Leaderboard")
            SoundButton = spyral.widgets.Button("Sound")


        
        my_form = RegisterForm(self)
        my_form.focus()
        my_form.StartGame.pos = ((WIDTH/2)-50, (HEIGHT/2) + 200)
        my_form.InstructionsButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 350)
#        my_form.OptionButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)
        my_form.LeaderboardButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 400)
        my_form.SoundButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 250)



#Functions that will take you to garage/game/options depending on which button is clicked
#        spyral.event.register("form.RegisterForm.OptionButton.clicked", self.goToOptions)
        spyral.event.register("form.RegisterForm.StartGame.clicked", self.goToRace)
        spyral.event.register("form.RegisterForm.InstructionsButton.clicked", self.goToInstructions)
        spyral.event.register("form.RegisterForm.LeaderboardButton.clicked", self.goToLeaderboard)
        spyral.event.register("form.RegisterForm.SoundButton.clicked", self.SwitchSound)
        #spyral.event.register("input.mouse.down", self.goToGarage)
        
        
#    def goToOptions(self):
#        spyral.director.pop
#        spyral.director.push(Options.OptionScene()) 
		
    def goToRace(self):
        spyral.director.pop
        spyral.director.push(RaceSelection.RaceSelection())

    def goToInstructions(self):
        spyral.director.pop
        spyral.director.push(Instructions.InstructionScene())
        
    def goToLeaderboard(self):
        spyral.director.pop
        spyral.director.push(LeaderBoard.LeaderboardScene())
        
    def SwitchSound(self):
        Race.Background_Music
        
        if(Race.Background_Music == True):
            Race.Background_Music = False
        elif(Race.Background_Music == False):
            Race.Background_Music = True
            
    #def goToGarage(self, pos):
        #pos = spyral.Vec2D(pos)
        #if pos.x > 390 and pos.x < 870 and pos.y >50 and pos.y < 475:
          #  spyral.director.pop
           # spyral.director.push(Garage.GarageScene())
