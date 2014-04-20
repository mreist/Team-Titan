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

        playerVehicle = Vehicle.Vehicles(self)
        playerVehicle.pos = (WIDTH/4, (HEIGHT/2)+200)
        
        currentQuestion = Questions.Question(self, 'addition', 1)
        currentQuestion.pos = (WIDTH/2, (HEIGHT/2)+435)
        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            
        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH-100), (HEIGHT-50))

        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)

    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
