import spyral 
import random
import Images
import math
import MainScreen
import Vehicle
import pygame
import time
import TextInterface
import Questions
from spyral import Animation, easing
import Garage
import ResultsScreen
import Player

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
        
        global timeStart
        timeStart = time.time() 

        self.isMoving = 0


        #Start game with speed of 10        
        self.speed = 10
        #Race distace is set to 100        
        self.raceDistance = 1000
        self.currentDistance = 0

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        
       
        #if(Background_Music == True):
        #   Game_music.play(-1)

        
        self.background = spyral.Image("images/Background.png")
        self.level = 0

        self.Chassis = Vehicle.Car(self)
        self.LeftWheel = Vehicle.Wheels(self)
        self.RightWheel = Vehicle.Wheels(self)      

        #Creates background images
        self.SmCloud = Images.SmallCloud(self)
        self.LrgCloud = Images.LargeCloud(self)
        self.Tree = Images.Tree(self)

        small = Animation('x', easing.Linear(WIDTH + 100, -500), duration = 3.0, loop = True)
        self.SmCloud.animate(small)


        large = Animation('x', easing.Linear(WIDTH + 100, -500), duration = 5.5, loop = True)
        self.LrgCloud.animate(large)

        tree = Animation('x', easing.Linear(WIDTH + 100, -500), duration = 4.5, loop = True)
        self.Tree.animate(tree)

        self.Chassis.pos = (WIDTH/4, (HEIGHT/2)+200)
        self.LeftWheel.pos.x = self.Chassis.pos.x - 100
        self.LeftWheel.pos.y = self.Chassis.pos.y + 35
        self.RightWheel.pos.x = self.Chassis.pos.x + 125
        self.RightWheel.pos.y = self.Chassis.pos.y + 35


        #playerVehicle = Vehicle.Vehicles(self)
        #playerVehicle.pos = (WIDTH/4, (HEIGHT/2)+200)

        animation = Animation('angle', easing.Linear(0, -2.0*math.pi), duration = 3.0, loop = True)
        self.RightWheel.animate(animation)
        self.LeftWheel.animate(animation)

        self.currentQuestion = Questions.Question(self, 'addition', 1)
        self.currentQuestion.pos = (WIDTH/2, (HEIGHT))

        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            AnswerInput = spyral.widgets.TextInput(100, "")
            Sound = spyral.widgets.Button("Sound")

        
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))
        self.my_form.AnswerInput.pos = ((WIDTH/2 + 150), (HEIGHT/2)+400)
        self.my_form.Sound.pos = ((WIDTH-100), (HEIGHT-850))
        
        spyral.event.register('director.update', self.update)
        
        #Initialize on screen text
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (WIDTH - 300, 100), str(time.time() - timeStart))
        self.speedText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, 100), str(self.speed))
        self.distanceText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (350, 100), str(self.currentDistance))
        self.mapStart = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (100, 300), "Start")
        self.mapStart.anchor = 'midright'
        self.mapFinish = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, WHITE), (700, 300), "Finish")
        self.mapFinish.anchor = 'midleft'

        self.miniMapBall = miniMap(self)
        self.miniMapBall.x = 100
        self.miniMapBall.y = 300
        
        #Not sure why this is Car.y.animation and not Chassis.y.animation, but it works?
        spyral.event.register('Car.y.animation.end', self.endMoving)
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        spyral.event.register("input.keyboard.down.space", self.checkAnswer)
        spyral.event.register("input.keyboard.down.down", self.moveDown)
        spyral.event.register("input.keyboard.down.up", self.moveUp)
        spyral.event.register("form.RegisterForm.Sound.clicked", self.SwitchSound)


    def checkAnswer(self):
        if int(self.my_form.AnswerInput.value) == self.currentQuestion.answer:
            print "CORRECT"
            self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 50, (255,0,0)), (WIDTH/2, 50), "Correct!")
            self.level += 1
            self.speed += 5
            self.feedback.kill()
        else:
            print "INCORRECT"
            self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 50, (0,255,0)), (WIDTH/2, 50), "Incorrect!")
            self.feedback.pos = (100, 100)
            self.feedback.kill()

        print ("previous answer: " + str(self.currentQuestion.answer))
        self.currentQuestion.kill()
        self.currentQuestion = Questions.Question(self, 'addition', 1)
        self.currentQuestion.pos = (WIDTH/2, (HEIGHT))
        print ("new answer: " + str(self.currentQuestion.answer))
        self.my_form.focus()
        print str(self.level)

    def update(self, delta): 
        self.currentTime = time.time() - timeStart 
        self.timeText.update("Current Time: %.2f" % self.currentTime)
        self.speedText.update("Speed: %d mph" % self.speed)
        self.distanceText.update("Distance: %d" % self.currentDistance) 
        self.currentDistance += self.speed * delta
        self.miniMapBall.x = (100 + (self.currentDistance / self.raceDistance) * 600)
        print self.currentDistance
        print self.miniMapBall.pos.x
        if(self.currentDistance >= self.raceDistance):
            global Game_music
            Game_music.stop()
            finishTime = time.time() - timeStart
            Player.currentTime = finishTime                      
            print "Finish Time = %.2f" % finishTime            
            self.goToResults()

         
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
        if(self.Chassis.pos.y >= (HEIGHT/2 + 200) and self.isMoving == 0):
            self.isMoving = 1
            chassisUp = Animation('y', easing.Linear(self.Chassis.pos.y, self.Chassis.pos.y-100), .5)
            leftWheelUp = Animation('y', easing.Linear(self.LeftWheel.pos.y, self.LeftWheel.pos.y-100), .5)
            rightWheelUp = Animation('y', easing.Linear(self.RightWheel.pos.y, self.RightWheel.pos.y-100), .5)
            self.Chassis.animate(chassisUp)
            self.LeftWheel.animate(leftWheelUp)
            self.RightWheel.animate(rightWheelUp)

    def moveDown(self):
        if(self.Chassis.pos.y <= (HEIGHT/2 + 200) and self.isMoving == 0):
            self.isMoving = 1
            chassisDown = Animation('y', easing.Linear(self.Chassis.pos.y, self.Chassis.pos.y+100), .5)
            leftWheelDown = Animation('y', easing.Linear(self.LeftWheel.pos.y, self.LeftWheel.pos.y+100), .5)
            rightWheelDown = Animation('y', easing.Linear(self.RightWheel.pos.y, self.RightWheel.pos.y+100), .5)
            self.Chassis.animate(chassisDown)
            self.LeftWheel.animate(leftWheelDown)
            self.RightWheel.animate(rightWheelDown)

    def endMoving(self):
        self.isMoving = 0

        
class miniMap(spyral.Sprite):
    def __init__(self, scene):
        super(miniMap, self).__init__(scene)

        self.image = spyral.Image(size=(20, 20))
        self.image.draw_circle(WHITE, (10, 10), 10)
        self.anchor = 'center'
