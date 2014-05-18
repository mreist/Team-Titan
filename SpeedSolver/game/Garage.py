import spyral 
import random
import math
import Model
import MainScreen
import Race
import Player
import TextInterface
from Model import resources
from Player import PlayerVehicle
from Player import PlayerLWheels
from Player import PlayerRWheels
from Player import PlayerDecal

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
tempCount = 0

#Boolean value for the Car Unlockables
RedCarUnlocked = False
GreenCarUnlocked = False
BlackCarUnlocked = False
WhiteCarUnlocked = False
PurpleCarUnlocked = False
PinkCarUnlocked = False
YellowCarUnlocked = False
OrangeCarUnlocked = False

#Boolean value for the FancyWheel Unlockables
LeftFWUnlocked =  False
RightFWUnlocked = False

#Boolean value for the Decal Unlockables
FireDecalUnlocked = False
BobUnlocked = True

#Cost of each Unlockable by tokens
paintCost = 2
wheelCost = 4
decalCost = 6


#Creates a BluePaint Sprite with its image

class drawBlueImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/BluePaint.png")
	    self.pos = ((WIDTH/2 + 150, 87))

	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    
#When the paint bucket is clicked it changes the Car Vtype to the particular color
    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.Vtype = "blue"
            Player.WithWheels = True

#Creates a RedPaint Sprite with its image
class drawRedImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/RedPaint.png")
	    self.pos = ((WIDTH/2 - 150, 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    
#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global RedCarUnlocked
        if (RedCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "red"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    RedCarUnlocked = True
        if (RedCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "red"
        Player.WithWheels = True
        
 #Creates a BlackPaint Sprite with its image       
class drawBlackImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/BlackPaint.png")
	    self.pos = ((WIDTH/2 + 150, HEIGHT/2 - 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global BlackCarUnlocked
        if (BlackCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "black"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    BlackCarUnlocked = True
        if (BlackCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "black"
        Player.WithWheels = True

#Creates a WhitePaint Sprite with its image
class drawWhiteImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/WhitePaint.png")
	    self.pos = ((WIDTH/2 - 150, HEIGHT/2 - 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global WhiteCarUnlocked
        if (WhiteCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "white"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    WhiteCarUnlocked = True
        if (WhiteCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "white"
        Player.WithWheels = True
        
        
#Creates a GreenPaint Sprite with its image        
class drawGreenImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/GreenPaint.png")
	    self.pos = ((WIDTH/2, HEIGHT/2 - 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	
	    
#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global GreenCarUnlocked
        if (GreenCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "green"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    GreenCarUnlocked = True
        if (GreenCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "green"
        Player.WithWheels = True

#Creates a PurplePaint Sprite with its image
class drawPurpleImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/PurplePaint.png")
	    self.pos = ((WIDTH/2 + 150 , HEIGHT - 671))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global PurpleCarUnlocked
        if (PurpleCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "purple"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    PurpleCarUnlocked = True
        if (PurpleCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "purple"
        Player.WithWheels = True       
 
 #Creates a PinkPaint Sprite with its image       
class drawPinkImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/PinkPaint.png")
	    self.pos = ((WIDTH/2 - 150 , HEIGHT - 671))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	
	    
#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global PinkCarUnlocked
        if (PinkCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "pink"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    PinkCarUnlocked = True
        if (PinkCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "pink"
        Player.WithWheels = True
        
        
#Creates a YellowPaint Sprite with its image        
class drawYellowImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/YellowPaint.png")
	    self.pos = ((WIDTH/2 , HEIGHT - 671))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global YellowCarUnlocked
        if (YellowCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "yellow"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    YellowCarUnlocked = True
        if (YellowCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "yellow"
        Player.WithWheels = True

#Creates a OrangePaint Sprite with its image
class drawOrangeImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/OrangePaint.png")
	    self.pos = ((WIDTH/2, HEIGHT - 811))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

#When the paint bucket is clicked it changes the Car Vtype to the particular color
#Checks to see if the car is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the car is unlocked and the boolean value is set to true.


    def handle_clicked(self, pos):
        global OrangeCarUnlocked
        if (OrangeCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= paintCost):
                    Model.Vtype = "orange"
                    Player.tokens = Player.tokens - paintCost
                    print Player.tokens
                    OrangeCarUnlocked = True
        if (OrangeCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "orange"
        Player.WithWheels = True        
        
#Creates a default LWheel Sprite with its image 

class drawLeftWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Wheel.png")
	    self.pos = (WIDTH - 1025, (HEIGHT/2)-330)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    
#When the LWheel is clicked it changes the Lwheel LWtype to the particular Wheel
#Default LWheel

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.LWtype = "Lwheel"
            
#Creates a default RWheel Sprite with its image 
class drawRightWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Wheel.png")
	    self.pos = (WIDTH - 175, (HEIGHT/2)-315)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    
#When the RWheel is clicked it changes the Rwheel RWtype to the particular Wheel
#Default RWheel

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RWtype = "Rwheel"

#Creates a default LFWheel Sprite with its image 

class drawLeftFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = (WIDTH - 1125 , (HEIGHT/2)-290)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

#When the LFWheel is clicked it changes the Lwheel LWtype to the particular wheel
#Checks to see if the wheel is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the wheel is unlocked and the boolean value is set to true.


    def handle_clicked(self, pos):
        global LeftFWUnlocked
        
        if (LeftFWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > wheelCost):
                    Model.LWtype = "LFwheel"
                    Player.tokens = Player.tokens - wheelCost
                    LeftFWUnlocked = True
                print Player.tokens
                
        if (LeftFWUnlocked == True):
            if self.collide_point(pos):
                Model.LWtype = "LFwheel"
                
#Creates a default RWheel Sprite with its image 

class drawRightFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = (WIDTH - 75, (HEIGHT/2)-270)

	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    
#When the RFWheel is clicked it changes the Rwheel RWtype to the particular wheel
#Checks to see if the wheel is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the wheel is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global RightFWUnlocked
        if (RightFWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > wheelCost):
                    Model.RWtype = "RFwheel"
                    Player.tokens = Player.tokens - wheelCost
                    RightFWUnlocked = True
                print Player.tokens
        if (RightFWUnlocked == True):
            if self.collide_point(pos):
                Model.RWtype = "RFwheel"
                
#Creates a FireDecal Sprite with its image 

class drawFireDecal(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Fire.png")
	    self.pos = ((WIDTH -120, HEIGHT - 300))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

#When the Decal is clicked it changes the Decal type to the particular Decal
#Checks to see if the Decal is unlocked, if it is not then checks how many tokens the player has.
#If they have enough tokens the Decal is unlocked and the boolean value is set to true.

    def handle_clicked(self, pos):
        global FireDecalUnlocked
        if (FireDecalUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > decalCost):
                    Model.Decal = "fire"
                    Player.tokens = Player.tokens - decalCost
                    print Player.tokens
                    FireDecalUnlocked = True
        if (FireDecalUnlocked == True):
            if self.collide_point(pos):
                Model.Decal = "fire"

#Creates a FancyBob Sprite with its image 
class drawFBobImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyBob.png")
	    self.pos = (WIDTH - 300, (HEIGHT/2) + 150)
	    #self.PlayerLWheels = PlayerLWheels(self.scene)
	  #  self.PlayerRWheels = PlayerRWheels(self.scene)
	   # spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    #def handle_clicked(self, pos):
       # global BobUnlocked
       # if (BobUnlocked == False):
         #   if self.collide_point(pos):
        #        if (Player.tokens > 0):
          #          Model.Vtype = "Bob"
         #           Player.tokens = Player.tokens - 1
          #          BobUnlocked = True
                    
          #      print Player.tokens
        #if (BobUnlocked == True):
        #    if self.collide_point(pos):
        #        Model.Vtype = "Bob"        
       #Player.WithWheels = False

#Creates a Garage scene
class GarageScene(spyral.Scene):
    def __init__(self):
	global manager
        super(GarageScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/GarageScene.png")
        

        self.currentCarText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), ((WIDTH/2, HEIGHT/2 + 135)), "Current Car:")
        self.currentCarText.anchor = 'midbottom'
        
        self.tokenText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), ((WIDTH - 200), (HEIGHT/2) + 400), "Number of Tokens: "+ str(Player.tokens))
        
        self.tokenText.anchor = 'center'

        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = ((WIDTH/2), (HEIGHT/2) + 200)
        self.PlayerDecal = PlayerDecal(self.scene)
        self.PlayerDecal.pos = ((WIDTH/2) -25, (HEIGHT/2) + 215)
        self.PlayerDecal.layer = "middle"
        self.layers = ["bottom", "middle", "top"]
        if (Player.WithWheels == True):
            self.PlayerLWheels = PlayerLWheels(self.scene)
            self.PlayerLWheels.pos.x = self.PlayerVehicle.pos.x - 100
            self.PlayerLWheels.pos.y = self.PlayerVehicle.pos.y + 30
            self.PlayerRWheels = PlayerRWheels(self.scene)
            self.PlayerRWheels.pos.x = self.PlayerVehicle.pos.x + 120
            self.PlayerRWheels.pos.y = self.PlayerVehicle.pos.y + 30
            self.PlayerLWheels.layer = "top"
            self.PlayerRWheels.layer = "top"

        self.BlueImage = drawBlueImage(self.scene)
        self.RedImage = drawRedImage(self.scene)
        self.BlackImage = drawBlackImage(self.scene)
        self.WhiteImage = drawWhiteImage(self.scene)
        self.GreenImage = drawGreenImage(self.scene)
        self.PurpleImage = drawPurpleImage(self.scene)
        self.PinkImage = drawPinkImage(self.scene)
        self.YellowImage = drawYellowImage(self.scene)
        self.OrangeImage = drawOrangeImage(self.scene)
        
        
        self.LeftWheelImage = drawLeftWheelImage(self.scene)
        self.RightWheelImage = drawRightWheelImage(self.scene)
        self.LeftFWheelImage = drawLeftFWheelImage(self.scene)
        self.RightFWheelImage = drawRightFWheelImage(self.scene)

        self.FireDecalImage = drawFireDecal(self.scene)

        self.FBobImage = drawFBobImage(self.scene)

	#Creates a back button to go back to the Main Menu
        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
		
        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 400)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)

        spyral.event.register("input.mouse.down.left", self.update)	
        #spyral.event.register('director.update', self.update)

    def update(self):
      #  global tempCount        
  #      if (tempCount > 0):
        self.tokenText.update("Number of Tokens: " + str(Player.tokens))
        self.PlayerVehicle.kill()
        self.PlayerLWheels.kill()
        self.PlayerRWheels.kill()
        self.PlayerDecal.kill()
        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = ((WIDTH/2), (HEIGHT/2) + 200)
        self.PlayerDecal = PlayerDecal(self.scene)
        self.PlayerDecal.pos = ((WIDTH/2) -25, (HEIGHT/2) + 215)
        self.PlayerDecal.layer = "middle"
        self.layers = ["bottom", "middle", "top"]
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
