import spyral
import random
import math
import pygame

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class Vehicle(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        
        self.image = spyral.Image(size=(300, 100))
        #Based on which vehicle they select use a switch statement to select self.image
        self.image = spyral.Image("libraries/spyral/resources/images/car.png")
        self.anchor = 'center'     #Default anchor is 'topleft'

        self.speed = 0

class Question(spyral.Sprite):
    def __init__(self, scene, location):
        spyral.Sprite.__init__(self, scene)
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.answer = self.num1 + self.num2
        self.font = spyral.Font(DEF_FONT, 36)

        self.image = self.font.render(str(self.num1) + "+" + str(self.num2) + "= ?")

class Title(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        
        self.image = spyral.Image(size=(300, 100))
        self.image = spyral.Image("libraries/spyral/resources/images/Title.png")
        self.anchor = 'center'     '


class SpeedSolver(spyral.Scene):
	def __init__(self, *args, **kwargs):

		super(SpeedSolver, self).__init__(SIZE)
       
    		
		self.background = spyral.Image("libraries/spyral/resources/images/Background.png")
		self.playerVehicle = Vehicle(self)
		self.playerVehicle.pos = (WIDTH/2, (HEIGHT/2)+200)
    
		self.Title = Title(self)
		self.Title.pos = (WIDTH/2, (HEIGHT/2) - 300)

		class RegisterForm(spyral.Form):
			StartGame = spyral.widgets.Button("Start Game")
			Options = spyral.widgets.Button("Options")
    		self.my_form = RegisterForm(self)
		self.my_form.focus()
		self.my_form.StartGame.pos = ((WIDTH/2)-50, (HEIGHT/2) + 200)
		self.my_form.Options.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)
		
		#spyral.event.register("input.mouse.down", self.StartGame)
		#spyral.event.register("input.mouse.down", self.Options)

   		#def StartGame(self,pos):
	
   		#def Options(self,pos):
	
		spyral.event.register('input.keyboard.down.esc', spyral.director.pop)
   		spyral.event.register("system.quit", spyral.director.pop)

	
