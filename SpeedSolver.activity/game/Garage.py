import spyral 
import random
import math
import Model
import MainScreen
import Race
import Player
import TextInterface
import sets
import Questions
import Images
from Model import resources
from Player import PlayerVehicle
from Player import PlayerLWheels
from Player import PlayerRWheels
from Player import PlayerDecal

WIDTH = 1200
HEIGHT = 900
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

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
LeftEWUnlocked = False
RightEWUnlocked = False
LeftCWUnlocked = False
RightCWUnlocked = False

#Boolean value for the Decal Unlockables
FireDecalUnlocked = False
FlowerDecalUnlocked = False
LightningDecalUnlocked = False
HeartDecalUnlocked = False
BobUnlocked = True

#Cost of each Unlockable by tokens
paintCost = 2
wheelCost = 4
decalCost = 6

QuestionVisible = False
AnswerVisible = False
question = None
questionanswer = None
question1 = 0

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
                if (Player.tokens >= wheelCost):
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
                if (Player.tokens >= wheelCost):
                    Model.RWtype = "RFwheel"
                    Player.tokens = Player.tokens - wheelCost
                    RightFWUnlocked = True
                print Player.tokens
        if (RightFWUnlocked == True):
            if self.collide_point(pos):
                Model.RWtype = "RFwheel"

class drawLeftEWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/EdgeyWheel.png")
	    self.pos = (WIDTH - 1125 , (HEIGHT/2)-90)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global LeftEWUnlocked
        
        if (LeftEWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= wheelCost):
                    Model.LWtype = "LEwheel"
                    Player.tokens = Player.tokens - wheelCost
                    LeftEWUnlocked = True
                print Player.tokens
                
        if (LeftEWUnlocked == True):
            if self.collide_point(pos):
                Model.LWtype = "LEwheel"
                
class drawRightEWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/EdgeyWheel.png")
	    self.pos = (WIDTH - 75, (HEIGHT/2)-70)

	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    
    def handle_clicked(self, pos):
        global RightEWUnlocked
        if (RightEWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= wheelCost):
                    Model.RWtype = "REwheel"
                    Player.tokens = Player.tokens - wheelCost
                    RightEWUnlocked = True
                print Player.tokens
        if (RightEWUnlocked == True):
            if self.collide_point(pos):
                Model.RWtype = "REwheel"

class drawLeftCWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/CrazyWheel.png")
	    self.pos = (WIDTH - 1025, (HEIGHT/2)-150)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global LeftCWUnlocked
        
        if (LeftCWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= wheelCost):
                    Model.LWtype = "LCwheel"
                    Player.tokens = Player.tokens - wheelCost
                    LeftCWUnlocked = True
                print Player.tokens
                
        if (LeftCWUnlocked == True):
            if self.collide_point(pos):
                Model.LWtype = "LCwheel"
                
class drawRightCWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/CrazyWheel.png")
	    self.pos = (WIDTH - 175, (HEIGHT/2)-135)

	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    
    def handle_clicked(self, pos):
        global RightCWUnlocked
        if (RightCWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= wheelCost):
                    Model.RWtype = "RCwheel"
                    Player.tokens = Player.tokens - wheelCost
                    RightCWUnlocked = True
                print Player.tokens
        if (RightCWUnlocked == True):
            if self.collide_point(pos):
                Model.RWtype = "RCwheel"
                
#Creates a FireDecal Sprite with its image 
class drawFireDecal(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Fire.png")
	    self.pos = ((WIDTH - 100, HEIGHT - 300))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    #When the Decal is clicked it changes the Decal type to the particular Decal
    #Checks to see if the Decal is unlocked, if it is not then checks how many tokens the player has.
    #If they have enough tokens the Decal is unlocked and the boolean value is set to true.
    def handle_clicked(self, pos):
        global FireDecalUnlocked
        if (FireDecalUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= decalCost):
                    Model.Decal = "fire"
                    Player.tokens = Player.tokens - decalCost
                    print Player.tokens
                    FireDecalUnlocked = True
        if (FireDecalUnlocked == True):
            if self.collide_point(pos):
                Model.Decal = "fire"

class drawFlowerDecal(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Flower.png")
	    self.pos = ((WIDTH - 150, HEIGHT - 375))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global FlowerDecalUnlocked
        if (FlowerDecalUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= decalCost):
                    Model.Decal = "flower"
                    Player.tokens = Player.tokens - decalCost
                    print Player.tokens
                    FlowerDecalUnlocked = True
        if (FlowerDecalUnlocked == True):
            if self.collide_point(pos):
                Model.Decal = "flower"


class drawLightningDecal(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Lightning.png")
	    self.pos = ((150, HEIGHT - 375))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global LightningDecalUnlocked
        if (LightningDecalUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= decalCost):
                    Model.Decal = "lightning"
                    Player.tokens = Player.tokens - decalCost
                    print Player.tokens
                    LightningDecalUnlocked = True
        if (LightningDecalUnlocked == True):
            if self.collide_point(pos):
                Model.Decal = "lightning"

class drawHeartDecal(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Heart.png")
	    self.pos = ((100, HEIGHT - 300))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global HeartDecalUnlocked
        if (HeartDecalUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens >= decalCost):
                    Model.Decal = "heart"
                    Player.tokens = Player.tokens - decalCost
                    print Player.tokens
                    HeartDecalUnlocked = True
        if (HeartDecalUnlocked == True):
            if self.collide_point(pos):
                Model.Decal = "heart"


#Creates a FancyBob Sprite with its image 
class drawFBobImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyBob.png")
	    self.pos = (WIDTH - 300, (HEIGHT/2) + 150)
	    #self.PlayerLWheels = PlayerLWheels(self.scene)
	  #  self.PlayerRWheels = PlayerRWheels(self.scene)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)
	    	

    def handle_clicked(self, pos):
        global AnswerVisible
        global QuestionVisible
        global question
        global questionanswer
        global question1
        if self.collide_point(pos):
            QuestionVisible = True
            AnswerVisible = True
            if(QuestionVisible == True and question1 == 0):
                operands = ['WordProb']
                question = Questions.Question(self.scene, random.choice(operands), 'WordProb')
        
                
                question.anchor ='center'
                question.pos = ((WIDTH/2 - 25), (HEIGHT/2) + 300)
                questionanswer = question.answer
                question1 = question1 + 1
            elif (question1 > 0):
                question.kill()   
                question1 = question1 - 1
                AnswerVisible = False

#Creates a Garage scene
class GarageScene(spyral.Scene):
    def __init__(self):
	global manager
	global AnswerVisible
	global QuestionVisible
	
        super(GarageScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/GarageScene.png")
        self.currentTurn = 0

        self.currentCarText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), ((WIDTH/2, HEIGHT/2 + 150)), "Current Car:")
        self.currentCarText.anchor = 'midbottom'
        
        self.tokenText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), ((WIDTH - 200), (HEIGHT/2) + 400), "Number of Tokens: "+ str(Player.tokens))
        
        self.tokenText.anchor = 'center'
        
        #Creates the Default Player Vehicle, wheels and decal
        
        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = ((WIDTH/2), (HEIGHT/2) + 200)
        self.PlayerVehicle.layer = "bottom"
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
        
        
        
        #Draws the different paint bucket images
        self.BlueImage = drawBlueImage(self.scene)
        self.RedImage = drawRedImage(self.scene)
        self.BlackImage = drawBlackImage(self.scene)
        self.WhiteImage = drawWhiteImage(self.scene)
        self.GreenImage = drawGreenImage(self.scene)
        self.PurpleImage = drawPurpleImage(self.scene)
        self.PinkImage = drawPinkImage(self.scene)
        self.YellowImage = drawYellowImage(self.scene)
        self.OrangeImage = drawOrangeImage(self.scene)
        
        #Draws the different Wheel Images
        self.LeftWheelImage = drawLeftWheelImage(self.scene)
        self.RightWheelImage = drawRightWheelImage(self.scene)
        self.LeftFWheelImage = drawLeftFWheelImage(self.scene)
        self.RightFWheelImage = drawRightFWheelImage(self.scene)
        self.LeftEWheelImage = drawLeftEWheelImage(self.scene)
        self.RightEWheelImage = drawRightEWheelImage(self.scene)
        self.LeftCWheelImage = drawLeftCWheelImage(self.scene)
        self.RightCWheelImage = drawRightCWheelImage(self.scene)

        #Draws the different Decal Images
        self.FireDecalImage = drawFireDecal(self.scene)
        self.FireDecalImage.scale = .75     
        self.FlowerDecalImage = drawFlowerDecal(self.scene)
        self.FlowerDecalImage.scale = .75
        self.LightningDecalImage = drawLightningDecal(self.scene)
        self.LightningDecalImage.scale = .75
        self.HeartDecalImage = drawHeartDecal(self.scene)
        self.HeartDecalImage.scale = .75        

        #Draws the Garage Owner Fancy Bob
        self.FBobImage = drawFBobImage(self.scene)
        self.BubbleImage = Images.FBSpeechBubble(self)
        self.BubbleImage.scale = .3
        
        inputValues = sets.Set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-'])
        #Creates a back button to go back to the Main Menu
        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
	    AnswerInput = spyral.widgets.TextInput(100, '', validator = inputValues, text_length = 4)	
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 400)


        self.my_form.AnswerInput.pos = ((WIDTH/2)-50, (HEIGHT/2) + 350)
        self.my_form.AnswerInput.visible = AnswerVisible
        
        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)
        spyral.event.register("input.keyboard.down.return", self.checkAnswer)
        spyral.event.register("input.mouse.down.left", self.update)	

    #Update function that draws the current car, wheels, and decals
    def update(self):
        self.tokenText.update("Number of Tokens: " + str(Player.tokens))
        self.PlayerVehicle.kill()
        self.PlayerLWheels.kill()
        self.PlayerRWheels.kill()
        self.PlayerDecal.kill()
        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = ((WIDTH/2), (HEIGHT/2) + 200)
        self.PlayerVehicle.layer = "bottom"
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
            
        self.my_form.AnswerInput.visible = AnswerVisible
        
        
        
    def checkAnswer(self):
        global AnswerVisible
        global question
        global questionanswer
        if(self.my_form.AnswerInput.visible == True):
            try:
                if int(self.my_form.AnswerInput.value) == questionanswer:
                        if(self.currentTurn > 0):
                            self.feedback.kill()
                        self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, (0,255,0)), (WIDTH/2, 50), ("Correct: " + question.output))
                        
                        self.feedback.anchor = 'bottomleft'
                        self.feedback.pos = ((WIDTH/2)-50, (HEIGHT/2) + 350)
                        Player.tokens = Player.tokens + 1 
                else:
                        if(self.currentTurn > 0):
                            self.feedback.kill()
                        self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, (150,0,0)), (WIDTH/2, 50), ("Incorrect: " + question.output))
                        self.feedback.anchor = 'bottomleft'            
                        self.feedback.pos = ((WIDTH/2)-50, (HEIGHT/2) + 350) 
                    
                       
                self.currentTurn =+ 1
                question.kill()       
                self.my_form.focus()
                self.tokenText
                self.tokenText.update("Number of Tokens: " + str(Player.tokens)) 
                AnswerVisible = False
                self.my_form.AnswerInput.visible = AnswerVisible
            except ValueError:
                print 'Nothing'        
    #Pops the Garage Scene and pushes the Main Menu to the front	
    def goToMenu(self):
    	global AnswerVisible
        AnswerVisible = False
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu()) 
