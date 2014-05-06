import spyral 
import random
import math
import model
import MainScreen
import Race
import Player
from model import resources

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

#Creates a Garage Sprite with its image
class Garage(spyral.Sprite):
    def __init__(self, scene):
        super(Garage, self).__init__(scene)
        model.loadResources()
        
        self.image = spyral.Image(size =(5, 5))
        self.image = spyral.Image("images/Garage.png")
        self.anchor = 'center'

class drawRedImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/RedCar.png")
	    self.pos = (WIDTH-200, (HEIGHT/2)+200)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.Vtype = "red"
            Player.WithWheels = True

class drawBlueImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/CarNoWheels.png")
	    self.pos = (WIDTH/4, (HEIGHT/2)+200)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.Vtype = "blue"
            Player.WithWheels = True

class drawLeftWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Wheel.png")
	    self.pos = (WIDTH/6, (HEIGHT/2)+270)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.LWtype = "Lwheel"

class drawRightWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Wheel.png")
	    self.pos = ((WIDTH/4) + 125, (HEIGHT/2)+270)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.RWtype = "Rwheel"
            
class drawLeftFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = (WIDTH-300, (HEIGHT/2)+270)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.LWtype = "LFwheel"

class drawRightFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = ((WIDTH-80), (HEIGHT/2)+270)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            model.RWtype = "RFwheel"            

#Creates a Garage scene
class GarageScene(spyral.Scene):
    def __init__(self):
	global manager
        super(GarageScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")
        
        CarGarage = Garage(self)
        CarGarage.pos = ((WIDTH/2), (HEIGHT/2)-100)

        self.RedImage = drawRedImage(self.scene)
        self.BlueImage = drawBlueImage(self.scene)
        self.LeftWheelImage = drawLeftWheelImage(self.scene)
        self.RightWheelImage = drawRightWheelImage(self.scene)
        self.LeftFWheelImage = drawLeftFWheelImage(self.scene)
        self.RightFWheelImage = drawRightFWheelImage(self.scene)
        
	#Creates a back button to go back to the Main Menu
        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
		
        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)

#Pops the Garage Scene and pushes the Main Menu to the front	
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu()) 





