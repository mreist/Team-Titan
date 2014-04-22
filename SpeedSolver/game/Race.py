import spyral 
import random
import math
import MainScreen
import Vehicle
import pygame
import time
import TextInterface
import Questions

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class RaceScene(spyral.Scene):
    def __init__(self):
        super(RaceScene, self).__init__(SIZE)
        
        global timeStart
        timeStart = time.time() 

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")
        self.level = 1
        
        playerVehicle = Vehicle.Vehicles(self)
        playerVehicle.pos = (WIDTH/4, (HEIGHT/2)+200)

        self.currentQuestion = Questions.Question(self, 'addition', 1)
        self.currentQuestion.pos = (WIDTH/2, (HEIGHT))
        

        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            AnswerInput = spyral.widgets.TextInput(100, "Answer")
        
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))
        self.my_form.AnswerInput.pos = ((WIDTH/2 + 150), (HEIGHT/2)+400)

        spyral.event.register('director.update', self.update)
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH - 300, 100), str(time.time() - timeStart))

        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        spyral.event.register("input.keyboard.down.space", self.checkAnswer)


    def checkAnswer(self):
        if int(self.my_form.AnswerInput.value) == self.currentQuestion.answer:
            print "CORRECT"
            self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 50, (255,0,0)), (WIDTH/2, 50), "Correct!")
            self.feedback.kill()
        else:
            print "INCORRECT"
            self.feedback = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 50, (0,255,0)), (WIDTH/2, 50), "Incorrect!")
            self.feedback.kill()
        print ("previous answer: " + str(self.currentQuestion.answer))
        self.currentQuestion.kill()
        self.currentQuestion = Questions.Question(self, 'addition', 1)
        self.currentQuestion.pos = (WIDTH/2, (HEIGHT))
        print ("new answer: " + str(self.currentQuestion.answer))
        self.my_form.focus()
        self.level += 1
        print str(self.level)
        if self.level > 10:
            print 'gameover'
            self.goToMenu
            #eventually: go to score screen
    

    def update(self): 
        self.timeText.update("Current Time: %.2f" % (time.time() - timeStart)) 
       
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())


        
