import spyral 
import random
import math
import MainScreen
import Vehicle
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
            EnterButton = spyral.widgets.Button("Enter")
            AnswerInput = spyral.widgets.TextInput(100, "Answer")
            
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))
        self.my_form.EnterButton.pos = ((WIDTH/2 + 150), (HEIGHT/2)+400)
        self.my_form.AnswerInput.pos = ((WIDTH/2 + 30), (HEIGHT/2)+400)
        
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
    
        spyral.event.register("form.RegisterForm.EnterButton.clicked", self.checkAnswer)
    
       

    def checkAnswer(self):
        if int(self.my_form.AnswerInput.value) == self.currentQuestion.answer:
            print "CORRECT"
        else:
            print "INCORRECT"
            
        print ("previous answer: " + str(self.currentQuestion.answer))
        del self.currentQuestion
        self.currentQuestion = Questions.Question(self, 'addition', 1)
        print ("new answer: " + str(self.currentQuestion.answer))
        self.level += 1
        if self.level > 10:
            self.goToMenu
            #eventually: go to score screen
            
#     def newQuestion(self):
#         p
            
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
