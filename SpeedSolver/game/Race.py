import spyral 
import random
import math
import MainScreen
import Vehicle
import pygame
import time
import TextInterface
import Questions
from spyral import Animation, easing
import Garage


WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
Background_Music = True;

class RaceScene(spyral.Scene):
    def __init__(self):
        super(RaceScene, self).__init__(SIZE)
        
        global timeStart
        timeStart = time.time() 

        self.isMoving = 0

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        
        #pygame.mixer.init()
        #Game_music = pygame.mixer.Sound("SandStorm.wav")
        #if(Background_Music == True):
        #   Game_music.play(10)
        
        self.background = spyral.Image("images/Background.png")
        self.level = 0

        self.Chassis = Vehicle.Car(self)
        self.LeftWheel = Vehicle.Wheels(self)
        self.RightWheel = Vehicle.Wheels(self)        

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
        
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))
        self.my_form.AnswerInput.pos = ((WIDTH/2 + 150), (HEIGHT/2)+400)

        spyral.event.register('director.update', self.update)
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH - 300, 100), str(time.time() - timeStart))

        #Not sure why this is Car.y.animation and not Chassis.y.animation, but it works?
        spyral.event.register('Car.y.animation.end', self.endMoving)
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        spyral.event.register("input.keyboard.down.space", self.checkAnswer)
        spyral.event.register("input.keyboard.down.down", self.moveDown)
        spyral.event.register("input.keyboard.down.up", self.moveUp)

    def checkAnswer(self):
        if int(self.my_form.AnswerInput.value) == self.currentQuestion.answer:
            print "CORRECT"
            self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 50, (255,0,0)), (WIDTH/2, 50), "Correct!")
            self.level += 1
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

        #When 3 questions are answered correctly        
        if self.level >= 3:
            finishTime = time.time() - timeStart                      
            print "Finish Time = %.2f" % finishTime            
            self.goToMenu()

    def update(self): 
        self.timeText.update("Current Time: %.2f" % (time.time() - timeStart)) 

    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())

    def moveUp(self):
        if(self.Chassis.pos.y >= (HEIGHT/2 + 200) and self.isMoving == 0):
            isMoving = 1
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
