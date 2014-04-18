import spyral 
import random
import math
import Vehicle
import Options

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class Title(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        
        self.image = spyral.Image(size=(300, 100))
        self.image = spyral.Image("images/Title.png")
        self.anchor = 'center' 

class MainMenu(spyral.Scene):
	def __init__(self):
		super(MainMenu, self).__init__(SIZE)

		spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
		spyral.event.register("system.quit", spyral.director.quit)

		self.background = spyral.Image("images/Background.png")
		playerVehicle = Vehicle.Vehicles(self)
		playerVehicle.pos = (WIDTH/2, (HEIGHT/2)+200)
    
		self.Title = Title(self)
		self.Title.pos = (WIDTH/2, (HEIGHT/2) - 300)

		class RegisterForm(spyral.Form):
			StartGame = spyral.widgets.Button("Start Game")
			OptionButton = spyral.widgets.Button("Options")
    		self.my_form = RegisterForm(self)

		self.my_form.focus()
		self.my_form.StartGame.pos = ((WIDTH/2)-50, (HEIGHT/2) + 200)
		self.my_form.OptionButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)

		spyral.event.register("form.RegisterForm.OptionButton.clicked", self.goToOptions)
		
	def goToOptions(self):
		spyral.director.pop
		spyral.director.push(Options.OptionScene()) 
