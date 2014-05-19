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
from Model import resources
from Player import PlayerVehicle
from Player import PlayerLWheels
from Player import PlayerRWheels

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
tempCount = 0
RedCarUnlocked = False
GreenCarUnlocked = False
BlackCarUnlocked = False
WhiteCarUnlocked = False
PurpleCarUnlocked = False
PinkCarUnlocked = False
YellowCarUnlocked = False
OrangeCarUnlocked = False

LeftFWUnlocked =  False
RightFWUnlocked = False
BobUnlocked = True
QuestionVisible = False
AnswerVisible = False

question = None
questionanswer = None
question1 = 0


#Creates a Garage Sprite with its image
class Garage(spyral.Sprite):
    def __init__(self, scene):
        super(Garage, self).__init__(scene)
        Model.loadResources()
        
        self.image = spyral.Image(size =(5, 5))
        self.image = spyral.Image("images/Garage.png")
        self.anchor = 'center'

class drawBlueImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/BluePaint.png")
	    self.pos = ((WIDTH/2 + 150, 87))

	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.Vtype = "blue"
            Player.WithWheels = True


class drawRedImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/RedPaint.png")
	    self.pos = ((WIDTH/2 - 150, 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global RedCarUnlocked
        if (RedCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "red"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    RedCarUnlocked = True
        if (RedCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "red"
        Player.WithWheels = True
        
        
class drawBlackImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/BlackPaint.png")
	    self.pos = ((WIDTH/2 + 150, HEIGHT/2 - 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global BlackCarUnlocked
        if (BlackCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "black"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    BlackCarUnlocked = True
        if (BlackCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "black"
        Player.WithWheels = True


class drawWhiteImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/WhitePaint.png")
	    self.pos = ((WIDTH/2 - 150, HEIGHT/2 - 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global WhiteCarUnlocked
        if (WhiteCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "white"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    WhiteCarUnlocked = True
        if (WhiteCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "white"
        Player.WithWheels = True
        
        
        
class drawGreenImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/GreenPaint.png")
	    self.pos = ((WIDTH/2, HEIGHT/2 - 87))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global GreenCarUnlocked
        if (GreenCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "green"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    GreenCarUnlocked = True
        if (GreenCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "green"
        Player.WithWheels = True


class drawPurpleImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/PurplePaint.png")
	    self.pos = ((WIDTH/2 + 150 , HEIGHT - 671))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global PurpleCarUnlocked
        if (PurpleCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "purple"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    PurpleCarUnlocked = True
        if (PurpleCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "purple"
        Player.WithWheels = True       
        
class drawPinkImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/PinkPaint.png")
	    self.pos = ((WIDTH/2 - 150 , HEIGHT - 671))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global PinkCarUnlocked
        if (PinkCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "pink"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    PinkCarUnlocked = True
        if (PinkCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "pink"
        Player.WithWheels = True
        
        
        
class drawYellowImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/YellowPaint.png")
	    self.pos = ((WIDTH/2 , HEIGHT - 671))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global YellowCarUnlocked
        if (YellowCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "yellow"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    YellowCarUnlocked = True
        if (YellowCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "yellow"
        Player.WithWheels = True


class drawOrangeImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/OrangePaint.png")
	    self.pos = ((WIDTH/2, HEIGHT - 811))
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global OrangeCarUnlocked
        if (OrangeCarUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.Vtype = "orange"
                    Player.tokens = Player.tokens - 1
                    print Player.tokens
                    OrangeCarUnlocked = True
        if (OrangeCarUnlocked == True):
            if self.collide_point(pos):
                Model.Vtype = "orange"
        Player.WithWheels = True        
        
        
class drawLeftWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Wheel.png")
	    self.pos = (WIDTH - 1025, (HEIGHT/2)-330)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.LWtype = "Lwheel"

class drawRightWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Wheel.png")
	    self.pos = (WIDTH - 175, (HEIGHT/2)-315)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            Model.RWtype = "Rwheel"


class drawLeftFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = (WIDTH - 1125 , (HEIGHT/2)-290)
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global LeftFWUnlocked
        
        if (LeftFWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.LWtype = "LFwheel"
                    Player.tokens = Player.tokens - 1
                    LeftFWUnlocked = True
                print Player.tokens
                
        if (LeftFWUnlocked == True):
            if self.collide_point(pos):
                Model.LWtype = "LFwheel"

class drawRightFWheelImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)
	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/FancyWheel.png")
	    self.pos = (WIDTH - 75, (HEIGHT/2)-270)

	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        global RightFWUnlocked
        if (RightFWUnlocked == False):
            if self.collide_point(pos):
                if (Player.tokens > 0):
                    Model.RWtype = "RFwheel"
                    Player.tokens = Player.tokens - 1
                    RightFWUnlocked = True
                print Player.tokens
        if (RightFWUnlocked == True):
            if self.collide_point(pos):
                Model.RWtype = "RFwheel"
                
   
	    
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

        self.currentCarText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), ((WIDTH/2, HEIGHT/2 + 135)), "Current Car:")
        self.currentCarText.anchor = 'midbottom'
        
        self.tokenText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), ((WIDTH - 200), (HEIGHT/2) + 400), "Number of Tokens: "+ str(Player.tokens))
        
        self.tokenText.anchor = 'center'
        
        

        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = ((WIDTH/2), (HEIGHT/2) + 200)
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
        self.FBobImage = drawFBobImage(self.scene)
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
        #spyral.event.register('director.update', self.update)

    def update(self):
      #  global tempCount        
  #      if (tempCount > 0):
        self.tokenText
        self.tokenText.update("Number of Tokens: " + str(Player.tokens))
        self.PlayerVehicle.kill()
        self.PlayerLWheels.kill()
        self.PlayerRWheels.kill()
        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = ((WIDTH/2), (HEIGHT/2) + 200)
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
                        self.feedback.pos = (50, HEIGHT)
                        Player.tokens = Player.tokens + 1 
                else:
                        if(self.currentTurn > 0):
                            self.feedback.kill()
                        self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, (150,0,0)), (WIDTH/2, 50), ("Incorrect: " + question.output))
                        self.feedback.anchor = 'bottomleft'            
                        self.feedback.pos = (50, HEIGHT) 
                    
                       
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
        #self.question.kill()
        AnswerVisible = False
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu()) 
