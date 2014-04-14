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
    def __init__(self, scene, location, operator, digits):
        spyral.Sprite.__init__(self, scene)
        if digits == 1:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
        elif digits == 2:
            self.num1 = random.randint(10, 100)
            self.num2 = random.randint(10, 100)
        elif digits == 3:
            self.num1 = random.randint(100, 1000)
            self.num2 = random.randint(100, 1000)
        else:
            self.num1 = random.randint(1, 10000000)
            self.num2 = random.randint(1, 10000000)
        self.font = spyral.Font(DEF_FONT, 36)
<<<<<<< HEAD

        self.image = self.font.render(str(self.num1) + "+" + str(self.num2) + "= ?")

class Title(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        
        self.image = spyral.Image(size=(300, 100))
        self.image = spyral.Image("libraries/spyral/resources/images/Title.png")
        self.anchor = 'center'     '


=======
        if operator == 'addition':
            self.answer = self.num1 + self.num2
            self.image = self.font.render(str(self.num1) + "+" + str(self.num2) + "= ?")
        elif operator == 'multiplication':
            self.answer = self.num1*self.num2
            self.image = self.font.render(str(self.num1) + "x" + str(self.num2) + "= ?")
        elif operator == 'subtraction':
            self.answer = self.num1-self.num2
            self.image = self.font.render(str(self.num1) + "-" + str(self.num2) + "= ?")
        elif operator == 'division':
            checkdivision(self.num1, self.num2)
        
    def checkdivision(self, num1, num2):
        if self.num1 % self.num2 == 0:
            self.answer = num1/num2
            self.image = self.font.render(str(self.num1) + "/" + str(self.num2) + "= ?")
        else:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
            checkdivision(num1, num2)
            
class Options(spyral.Scene):
    def __init__(self, *args, **kwargs):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image("libraries/spyral/resources/images/testBackground.png")
        
    
>>>>>>> Jason-Branch
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

	
