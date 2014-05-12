import spyral 
import random
import math
import Model
import MainScreen
import Race
import Player
from Model import resources
from Player import PlayerVehicle
from Player import PlayerLWheels
from Player import PlayerRWheels
import TextInterface

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
tempCount = 0

#Creates a Garage Sprite with its image
class Garage(spyral.Sprite):
    def __init__(self, scene):
        super(Garage, self).__init__(scene)
        Model.loadResources()
        
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
            Model.Vtype = "red"
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
            Model.Vtype = "blue"
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
            Model.LWtype = "Lwheel"

class drawRightWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Wheel.png")
	    self.pos = ((WIDTH/4) + 125, (HEIGHT/2)+270)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RWtype = "Rwheel"


class drawLeftFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = (WIDTH-300, (HEIGHT/2)+270)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.LWtype = "LFwheel"

class drawRightFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = (WIDTH-80, (HEIGHT/2)+270)

	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RWtype = "RFwheel"

#Creates a Garage scene
class GarageScene(spyral.Scene):
    def __init__(self):
	global manager
        super(GarageScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")
        
        self.currentCarText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (WIDTH/2, 50), "Current Car:")
        self.currentCarText.anchor = 'midbottom'

        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = (WIDTH/2, 100)
        self.layers = ["bottom", "top"]
        if (Player.WithWheels == True):
            self.PlayerLWheels = PlayerLWheels(self.scene)
            self.PlayerLWheels.pos.x = self.PlayerVehicle.pos.x - 100
            self.PlayerLWheels.pos.y = self.PlayerVehicle.pos.y + 30
            self.PlayerRWheels = PlayerRWheels(self.scene)
            self.PlayerRWheels.pos.x = self.PlayerVehicle.pos.x + 120
            self.PlayerRWheels.pos.y = self.PlayerVehicle.pos.y + 30
            self.PlayerLWheels.layer = "top"
            self.PlayerRWheels.layer = "top"


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

        spyral.event.register("input.mouse.down.left", self.update)	
        #spyral.event.register('director.update', self.update)

    def update(self):
      #  global tempCount        
  #      if (tempCount > 0):
        self.PlayerVehicle.kill()
        self.PlayerLWheels.kill()
        self.PlayerRWheels.kill()
        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = (WIDTH/2, 100)
        self.layers = ["bottom", "top"]
        if (Player.WithWheels == True):
            self.PlayerLWheels = PlayerLWheels(self.scene)
            self.PlayerLWheels.pos.x = self.PlayerVehicle.pos.x - 100
            self.PlayerLWheels.pos.y = self.PlayerVehicle.pos.y + 30
            self.PlayerRWheels = PlayerRWheels(self.scene)
            self.PlayerRWheels.pos.x = self.PlayerVehicle.pos.x + 120
            self.PlayerRWheels.pos.y = self.PlayerVehicle.pos.y + 30
            self.PlayerLWheels.layer = "top"
            self.PlayerRWheels.layer = "top"
     #   tempCount =+ 1
            

#Pops the Garage Scene and pushes the Main Menu to the front	
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu()) 





