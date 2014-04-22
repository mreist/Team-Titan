import spyral 
import random
import math
import MainScreen
import Vehicle
import Questions
import time

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class RaceScene(spyral.Scene):
    def __init__(self):
        super(RaceScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")
        self.level = 1
        
        playerVehicle = Vehicle.Vehicles(self)
        playerVehicle.pos = (WIDTH/4, (HEIGHT/2)+200)
        
        self.currentQuestion = Questions.Question(self, 'addition', 1)
        self.currentQuestion.pos = (WIDTH/2, (HEIGHT/2)+435)
        
        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            AnswerInput = spyral.widgets.TextInput(100, "Answer")
            
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))
        self.my_form.AnswerInput.pos = ((WIDTH/2 + 30), (HEIGHT/2)+400)
        
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        
        spyral.event.register("input.keyboard.down.space", self.checkAnswer)

    def checkAnswer(self):
        if int(self.my_form.AnswerInput.value) == self.currentQuestion.answer:
            print "CORRECT"
            self.feedback = TextInterface(self, spyral.Font(DEF_FONT, 50, (255,0,0)), (WIDTH/2, 50), "Correct!")
            self.feedback.kill()
        else:
            print "INCORRECT"
            self.feedback = TextInterface(self, spyral.Font(DEF_FONT, 50, (0,255,0)), (WIDTH/2, 50), "Incorrect!")
            self.feedback.kill()
        print ("previous answer: " + str(self.currentQuestion.answer))
        self.currentQuestion.kill()
        self.currentQuestion = Questions.Question(self, 'addition', 1)
        self.currentQuestion.pos = (WIDTH/2, (HEIGHT/2)+435)
        print ("new answer: " + str(self.currentQuestion.answer))
        self.my_form.focus()
        self.level += 1
        print str(self.level)
        if self.level > 10:
            print 'gameover'
            self.goToMenu
            #eventually: go to score screen

            
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
        
class TextInterface(spyral.Sprite):
	def __init__(self, scene, font, position, string):
		super(TextInterface, self).__init__(scene)
		self.font = font
		self.pos = position
		self.text = string
		self.anchor = 'topleft'
		self.image = self.font.render(self.text)

	def update(self, string):
		self.text = string
		self.image = self.font.render(self.text)
