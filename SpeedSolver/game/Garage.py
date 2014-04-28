import spyral 
import random
import math
import MainScreen

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


#Creates the Garage Image sprite

#Creates a Garage Sprite with its image

class Garage(spyral.Sprite):
    def __init__(self, scene):
        super(Garage, self).__init__(scene)
        
        self.image = spyral.Image(size =(5, 5))
        self.image = spyral.Image("images/Garage.png")
        self.anchor = 'center'

#Creates the Garage Scene

#Creates a Garage scene

class GarageScene(spyral.Scene):
    def __init__(self):
        super(GarageScene, self).__init__(SIZE)
        #allows the player to quit the game
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        #displays the background
        self.background = spyral.Image("images/Background.png")
        #calls the garage sprite and sets its position
        CarGarage = Garage(self)
        CarGarage.pos = ((WIDTH/2), (HEIGHT/2)-100)

        #creates a back button to go back to the Main Menu

	#Creates a back button to go back to the Main Menu

        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
		
        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)


	#Pops the Garage scene then pushes the Main Menu Scene

#Pops the Garage Scene and pushes the Main Menu to the front	

    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu()) 





