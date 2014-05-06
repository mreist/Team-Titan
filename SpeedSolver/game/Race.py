import spyral 
import random
import math
import MainScreen
import Images
import Vehicle
import pygame
import time
import TextInterface
import Questions
from spyral import Animation, easing
import ResultsScreen
import model
import Player
<<<<<<< HEAD
from model import resources
from Player import PlayerVehicle
from Player import PlayerLWheels
from Player import PlayerRWheels
=======
import sets
>>>>>>> origin/MaxxTesting

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
Background_Music = True;
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
Game_music = pygame.mixer.Sound("SandStorm.wav")

class RaceScene(spyral.Scene):
    def __init__(self):
        super(RaceScene, self).__init__(SIZE)
        
        model.loadResources()
        
        global timeStart

        global manager

        timeStart = time.time() 

        timeStart = time.time()
        self.layers = ["bottom", "top"]
        self.PlayerVehicle = PlayerVehicle(self.scene)
        self.PlayerVehicle.pos = (WIDTH/4, (HEIGHT/2)+200)
        self.layers = ["bottom", "top"]
        if (Player.WithWheels == True):
            self.PlayerLWheels = PlayerLWheels(self.scene)
            self.PlayerLWheels.pos.x = self.PlayerVehicle.pos.x - 100
            self.PlayerLWheels.pos.y = self.PlayerVehicle.pos.y + 35
            self.PlayerRWheels = PlayerRWheels(self.scene)
            self.PlayerRWheels.pos.x = self.PlayerVehicle.pos.x + 125
            self.PlayerRWheels.pos.y = self.PlayerVehicle.pos.y + 35
            self.PlayerLWheels.layer = "top"
            self.PlayerRWheels.layer = "top"
            animation = Animation('angle', easing.Linear(0, -2.0*math.pi), duration = 3.0, loop = True)
            self.PlayerRWheels.animate(animation)
            self.PlayerLWheels.animate(animation)
            
        self.isMoving = 0
        self.currentTurn = 0
        self.currentDistance = 0
        self.level = 0

        
        
        
        #Initializae race variables
        #Start game with speed of 10        
        self.speed = 5
        #Race distace is set to 100        
        self.raceDistance = 1000
        

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        
       
        if(Background_Music == True):
           Game_music.play(-1)
        
        self.background = spyral.Image("images/Background.png")


        self.PlayerVehicle.layer = "bottom"
        
        


        #Creates background images

        self.LrgCloud = Images.LargeCloud(self)
        self.Tree = Images.Tree(self)

        #Creates Bottom Road Lines
        self.BottomLine1 = Images.RoadLines(self)
        self.BottomLine2 = Images.RoadLines(self)
        self.BottomLine3 = Images.RoadLines(self)

        self.BottomLine1.pos.y = HEIGHT - 180 
        self.BottomLine2.pos.y = HEIGHT - 180
        self.BottomLine3.pos.y = HEIGHT - 180

        BottomOne = Animation('x', easing.Linear(WIDTH + 100, -2700), duration = 3.0, loop = True)
        self.BottomLine1.animate(BottomOne)

        BottomTwo = Animation('x', easing.Linear(WIDTH + 1400, -1400), duration = 3.0, loop = True)
        self.BottomLine2.animate(BottomTwo)

        BottomThree = Animation('x', easing.Linear(WIDTH + 2700, -100), duration = 3.0, loop = True)
        self.BottomLine3.animate(BottomThree)

        #Creates Top Road Lines
        self.TopLine1 = Images.RoadLines(self)
        self.TopLine2 = Images.RoadLines(self)
        self.TopLine3 = Images.RoadLines(self)

        self.TopLine1.pos.y = HEIGHT - 300 
        self.TopLine2.pos.y = HEIGHT - 300
        self.TopLine3.pos.y = HEIGHT - 300

        TopOne = Animation('x', easing.Linear(WIDTH + 100, -2700), duration = 3.0, loop = True)
        self.TopLine1.animate(TopOne)

        TopTwo = Animation('x', easing.Linear(WIDTH + 1400, -1400), duration = 3.0, loop = True)
        self.TopLine2.animate(TopTwo)

        TopThree = Animation('x', easing.Linear(WIDTH + 2700, -100), duration = 3.0, loop = True)
        self.TopLine3.animate(TopThree)

        #Initialize Questions and Question 
        self.questionOne = Questions.Question(self, 'addition', 1)
        self.questionOne.anchor ='midleft'        
        self.questionOne.pos = (WIDTH + 200, 550)

        self.questionTwo = Questions.Question(self, 'subtraction', 1)
        self.questionTwo.anchor ='midleft'                
        self.questionTwo.pos = (WIDTH + 200, 650)
        
        self.questionThree = Questions.Question(self, 'multiplication', 1)
        self.questionThree.anchor ='midleft'
        self.questionThree.pos = (WIDTH + 200, 750)
        
        self.questionOneAnimation = Animation('x', easing.Linear(self.questionOne.x, self.questionOne.x - (WIDTH + 300)), 8)
        self.questionOne.animate(self.questionOneAnimation)

        self.questionTwoAnimation = Animation('x', easing.Linear(self.questionTwo.x, self.questionThree.x - (WIDTH + 300)), 8)
        self.questionTwo.animate(self.questionTwoAnimation)

        self.questionThreeAnimation = Animation('x', easing.Linear(self.questionThree.x, self.questionThree.x - (WIDTH + 300)), 8)
        self.questionThree.animate(self.questionThreeAnimation)

        inputValues = sets.Set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-'])

        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            AnswerInput = spyral.widgets.TextInput(100, '', validator = inputValues)
            Sound = spyral.widgets.Button("Sound")

        
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))
        self.my_form.AnswerInput.pos = ((WIDTH/2 + 150), (HEIGHT/2)+400)
        self.my_form.AnswerInput.visible = False        
        self.my_form.Sound.pos = ((WIDTH-100), (HEIGHT-850))
        
        spyral.event.register('director.update', self.update)
        
        #Initialize on screen text
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (WIDTH - 300, 100), str(time.time() - timeStart))
        self.speedText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, 100), str(self.speed))
        self.distanceText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (350, 100), str(self.currentDistance))

        #Minimap stuff        
        self.mapStart = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, 300), "Start")
        self.mapStart.anchor = 'midright'
        self.mapFinish = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (700, 300), "Finish")
        self.mapFinish.anchor = 'midleft'
        self.miniMapBall = miniMap(self)
        self.miniMapBall.x = 100
        self.miniMapBall.y = 300

        spyral.event.register('PlayerVehicle.y.animation.end', self.endMoving)
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        spyral.event.register("input.keyboard.down.space", self.checkAnswer)
        spyral.event.register("input.keyboard.down.down", self.moveDown)
        spyral.event.register("input.keyboard.down.up", self.moveUp)
        spyral.event.register("form.RegisterForm.Sound.clicked", self.SwitchSound)

    #Checks if answer is correct,
    def checkAnswer(self):
<<<<<<< HEAD
        
        if int(self.my_form.AnswerInput.value) == self.currentQuestion.answer:
            if(self.currentTurn > 0):
                self.feedback.kill()
            self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, (0,120,0)), (WIDTH/2, 50), ("Correct: " + self.currentQuestion.output))
            self.feedback.anchor = 'bottomleft'
            self.feedback.pos = (50, HEIGHT)            
            self.level += 1
            self.speed += 5
        else:
            if(self.currentTurn > 0):
                self.feedback.kill()
            self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, (150,0,0)), (WIDTH/2, 50), ("Incorrect: " + self.currentQuestion.output))
            self.feedback.anchor = 'bottomleft'            
            self.feedback.pos = (50, HEIGHT)
            if(self.speed > 2):
                self.speed -= 2

        operands = ['addition', 'multiplication', 'subtraction', 'division']
        
        self.currentTurn += 1
        self.currentQuestion.kill()
        self.currentQuestion = Questions.Question(self, random.choice(operands), 1)
        self.currentQuestion.pos = (WIDTH/2, (HEIGHT))
        self.my_form.focus()
=======
        if(self.my_form.AnswerInput.visible == True):
            try:
                if int(self.my_form.AnswerInput.value) == self.currentQuestion.answer:
                    print "CORRECT"
                    if(self.currentTurn > 0):
                        self.feedback.kill()
                    self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, (0,120,0)), (WIDTH/2, 50), "Correct! %d + %d = %d" %(self.currentQuestion.num1, self.currentQuestion.num2, self.currentQuestion.answer))
                    self.feedback.anchor = 'bottomleft'
                    self.feedback.pos = (50, HEIGHT)            
                    self.level += 1
                    self.speed += 5
                else:
                    print "INCORRECT"
                    if(self.currentTurn > 0):
                        self.feedback.kill()
                    self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 32, (150,0,0)), (WIDTH/2, 50), "Incorrect! %d + %d = %d" %(self.currentQuestion.num1, self.currentQuestion.num2, self.currentQuestion.answer))
                    self.feedback.anchor = 'bottomleft'            
                    self.feedback.pos = (50, HEIGHT)
                    if(self.speed > 2):
                        self.speed -= 2

                self.currentTurn += 1
                print ("previous answer: " + str(self.currentQuestion.answer))
                self.currentQuestion.kill()
                #self.currentQuestion = Questions.Question(self, 'addition', 1)
                #self.currentQuestion.pos = (WIDTH/2, (HEIGHT))

                self.questionOne = Questions.Question(self, 'addition', 1)
                self.questionOne.anchor ='midleft'        
                self.questionOne.pos = (WIDTH + 200, 550)
                self.questionTwo = Questions.Question(self, 'subtraction', 1)
                self.questionTwo.anchor ='midleft'
                self.questionTwo.pos = (WIDTH + 200, 650)
                self.questionThree = Questions.Question(self, 'multiplication', 1)
                self.questionThree.anchor ='midleft'        
                self.questionThree.pos = (WIDTH + 200, 750)

                self.questionOne.animate(self.questionOneAnimation)
                self.questionTwo.animate(self.questionTwoAnimation)
                self.questionThree.animate(self.questionThreeAnimation)

                print ("new answer: " + str(self.currentQuestion.answer))
                self.my_form.focus()
                print str(self.level)
                self.isMoving = 0
                self.my_form.AnswerInput.visible = False

            except ValueError:
                print 'Nothing'
>>>>>>> origin/MaxxTesting

    def update(self, delta): 
        self.currentTime = time.time() - timeStart 
        self.timeText.update("Current Time: %.2f" % self.currentTime)
        self.speedText.update("Speed: %d mph" % self.speed)
        self.distanceText.update("Distance: %d" % self.currentDistance) 
        self.currentDistance += self.speed * delta
        self.miniMapBall.x = (100 + (self.currentDistance / self.raceDistance) * 600)
        
        tree = Animation('x', easing.Linear(WIDTH + 100, -100), duration = 4.5, loop = False)
        large = Animation('x', easing.Linear(WIDTH + 100, -100), duration = 10.0, loop = False)

<<<<<<< HEAD
        if(self.currentTime%15 > 0 and self.currentTime%15 < .05):
            self.Tree.animate(tree)

        if(self.currentTime%20 > 0 and self.currentTime%20 < .05):
            self.LrgCloud.animate(large)
            
=======
>>>>>>> origin/MaxxTesting
        if(self.currentDistance >= self.raceDistance):
            global Game_music
            Game_music.stop()

<<<<<<< HEAD
            finishTime = time.time() - timeStart                      
            print "Finish Time = %.2f" % finishTime 
            Player.currentTime = finishTime                                            

=======
            finishTime = time.time() - timeStart
            Player.currentTime = finishTime                      
            print "Finish Time = %.2f" % finishTime            
>>>>>>> origin/MaxxTesting
            self.goToResults()

        if (self.collide_sprites(self.Chassis, self.questionOne)):
            print "Collide with 1"
            self.my_form.AnswerInput.visible = True            
            self.questionOne.stop_all_animations()
            self.currentQuestion = self.questionOne
            self.questionTwo.kill()
            self.questionThree.kill()
            self.currentQuestion.pos = ((WIDTH/2 - 75), (HEIGHT - 30))
            self.isMoving = 1
        elif (self.collide_sprites(self.Chassis, self.questionTwo)):
            print "Collide with 2"
            self.my_form.AnswerInput.visible = True           
            self.questionTwo.stop_all_animations()
            self.currentQuestion = self.questionTwo
            self.questionOne.kill()
            self.questionThree.kill()
            self.currentQuestion.pos = ((WIDTH/2 - 75), (HEIGHT - 30))
            self.isMoving = 1
        elif (self.collide_sprites(self.Chassis, self.questionThree)):
            print "Collide with 3"
            self.my_form.AnswerInput.visible = True
            self.questionThree.stop_all_animations()
            self.currentQuestion = self.questionThree
            self.questionOne.kill()
            self.questionTwo.kill()
            self.currentQuestion.pos = ((WIDTH/2 - 75), (HEIGHT - 30))
            self.isMoving = 1

    #Quit button method that stops the music and goes back to Main Menu
    def goToMenu(self):
        global Game_music
        Game_music.stop()
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
 
    def goToResults(self):
        spyral.director.pop
        spyral.director.push(ResultsScreen.ResultsScreen())

        
    #Button that allows the player to turn on/off the sound    
    def SwitchSound(self):
        global Game_music
        global Background_Music
        
        if(Background_Music == True):
            Game_music.stop()
            Background_Music = False
        elif(Background_Music == False):
            Game_music.play(-1)
            Background_Music = True
        
    def moveUp(self):
        if(self.PlayerVehicle.y >= (HEIGHT/2 + 200) and self.isMoving == 0):
            self.isMoving = 1
            chassisUp = Animation('y', easing.Linear(self.PlayerVehicle.y, self.PlayerVehicle.y-100), .5)
            self.PlayerVehicle.animate(chassisUp)

            if(Player.WithWheels == True):
                leftWheelUp = Animation('y', easing.Linear(self.PlayerLWheels.y, self.PlayerLWheels.y-100), .5)
                rightWheelUp = Animation('y', easing.Linear(self.PlayerRWheels.y, self.PlayerRWheels.y-100), .5)
            
                self.PlayerLWheels.animate(leftWheelUp)
                self.PlayerRWheels.animate(rightWheelUp)

    def moveDown(self):
        if(self.PlayerVehicle.y <= (HEIGHT/2 + 200) and self.isMoving == 0):
            self.isMoving = 1
            chassisDown = Animation('y', easing.Linear(self.PlayerVehicle.y, self.PlayerVehicle.y+100), .5)
            self.PlayerVehicle.animate(chassisDown)
            
            if(Player.WithWheels == True):
                leftWheelDown = Animation('y', easing.Linear(self.PlayerLWheels.y, self.PlayerLWheels.y+100), .5)
                rightWheelDown = Animation('y', easing.Linear(self.PlayerRWheels.y, self.PlayerRWheels.y+100), .5)
            
                self.PlayerLWheels.animate(leftWheelDown)
                self.PlayerRWheels.animate(rightWheelDown)

    def endMoving(self):
        self.isMoving = 0

class miniMap(spyral.Sprite):
    def __init__(self, scene):
        super(miniMap, self).__init__(scene)

        self.image = spyral.Image(size=(20, 20))
        self.image.draw_circle(WHITE, (10, 10), 10)
        self.anchor = 'center'
