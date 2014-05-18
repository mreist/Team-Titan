import spyral 
import Instructions
import Race
import Garage
import LeaderBoard
import RaceSelection
import Model

from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

#Draws Garage Image on Main Screen
class drawGarageImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)

	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Garage.png")
	    self.pos = ((WIDTH/2), (HEIGHT/2)-200)

        #Upon click goes into Garage Scene
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

        #Creates the Start, Instruction, Leaderboard, and Sound Button
        class RegisterForm(spyral.Form):
            StartGame = spyral.widgets.Button("Start Game")
            InstructionsButton = spyral.widgets.Button("Instructions")
            LeaderboardButton = spyral.widgets.Button("Leaderboard")
            #SoundButton = spyral.widgets.Button("Sound")

        #Sets button positions
        my_form = RegisterForm(self)
        my_form.focus()
        my_form.StartGame.pos = ((WIDTH/2)-50, (HEIGHT/2) + 200)
        my_form.InstructionsButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 350)
        my_form.LeaderboardButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 400)
        #my_form.SoundButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 250)



        #Functions that will take you to garage/game/options depending on which button is clicked
        spyral.event.register("form.RegisterForm.StartGame.clicked", self.goToRace)
        spyral.event.register("form.RegisterForm.InstructionsButton.clicked", self.goToInstructions)
        spyral.event.register("form.RegisterForm.LeaderboardButton.clicked", self.goToLeaderboard)
        #spyral.event.register("form.RegisterForm.SoundButton.clicked", self.SwitchSound)
		
    def goToRace(self):
        Model.SelectMode = "Race"
        spyral.director.pop
        spyral.director.push(RaceSelection.RaceSelection())

    def goToInstructions(self):
        spyral.director.pop
        spyral.director.push(Instructions.InstructionScene())
        
    def goToLeaderboard(self):
        Model.SelectMode = "LeaderBoard"
        spyral.director.pop
        spyral.director.push(RaceSelection.RaceSelection())
        
    #def SwitchSound(self):
        #Race.Background_Music
        
        #if(Race.Background_Music == True):
            #Race.Background_Music = False
        #elif(Race.Background_Music == False):
            #Race.Background_Music = True
