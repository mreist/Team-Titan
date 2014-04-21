import spyral 
import random
import math
import MainScreen

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

#Box dimensions are 85x 80
class EasyBox(spyral.Sprite):
    def __init__(self, scene):
        super(EasyBox, self).__init__(scene)
        
        self.image = spyral.Image("images/EasyBox.png")
        self.pos = (50, 350)

class MediumBox(spyral.Sprite):
    def __init__(self, scene):
        super(MediumBox, self).__init__(scene)
        
        self.image = spyral.Image("images/MediumBox.png")
        self.pos = (50, 500)

class HardBox(spyral.Sprite):
    def __init__(self, scene):
        super(HardBox, self).__init__(scene)
        
        self.image = spyral.Image("images/HardBox.png")
        self.pos = (50, 700)

class AdditionBox(spyral.Sprite):
    def __init__(self, scene):
        super(AdditionBox, self).__init__(scene)
        
        self.image = spyral.Image("images/AdditionBox.png")
        self.pos = (550, 200)

class SubtractionBox(spyral.Sprite):
    def __init__(self, scene):
        super(SubtractionBox, self).__init__(scene)
        
        self.image = spyral.Image("images/SubtractionBox.png")
        self.pos = (550, 350)

class MultiplicationBox(spyral.Sprite):
    def __init__(self, scene):
        super(MultiplicationBox, self).__init__(scene)
        
        self.image = spyral.Image("images/MultiplicationBox.png")
        self.pos = (550, 500)

class DivisionBox(spyral.Sprite):
    def __init__(self, scene):
        super(DivisionBox, self).__init__(scene)
        
        self.image = spyral.Image("images/DivisionBox.png")
        self.pos = (550, 700)

class CheckMark(spyral.Sprite):
    def __init__(self, scene, location):
        super(CheckMark, self).__init__(scene)

        self.image = spyral.Image("images/CheckMark.png")
        #self.anchor = 'center'
        self.pos = location

class OptionScene(spyral.Scene):
    def __init__(self):
        super(OptionScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Option_Menu.png")

        mediumCheck = CheckMark(self.scene, (75, 450))
        easy = EasyBox(self)
        medium = MediumBox(self)
        hard = HardBox(self)
        addition = AdditionBox(self)
        subtraction = SubtractionBox(self)
        multiplication = MultiplicationBox(self)
        division = DivisionBox(self)
        self.background = spyral.Image("images/Option_Menu.png")

        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
            EasyBox = spyral.widgets.Checkbox()

        my_form = RegisterForm(self)

        my_form.focus()
       # my_form.EasyBox {
       #     image_up: "images/EasyBox.png"
       #     image_up_hovered: "images/EasyBox.png"
       #     image_up_focuses: "images/EasyBox.png"
       #     image_down: "images/EasyBox.png"
       #     image_down_hovered: "images/EasyBox.png"
       #     image_down_focuses: "images/EasyBox.png"
       # }
        my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 300)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)
        spyral.event.register("input.mouse.down", self.makeMark)
	
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu()) 

    def makeMark(self, pos):
        pos = spyral.Vec2D(pos)
        easyCheck = CheckMark(self.scene, (75, 310))
        easyCheck.visible = False
        if pos.x > 35 and pos.x < 120 and pos.y > 230 and pos.y < 310:
            if easyCheck.visible == False:
                easyCheck.visible = True
            elif easyCheck.visible == True:
                easyCheck.visible = False;
        if pos.x > 35 and pos.x < 120 and pos.y > 330 and pos.y < 410:
            CheckMark(self.scene, (75, 450))
        if pos.x > 35 and pos.x < 120 and pos.y > 465 and pos.y < 545:
            CheckMark(self.scene, (75, 650))        
        if pos.x > 410 and pos.x < 495 and pos.y > 130 and pos.y < 210:
            CheckMark(self.scene, (575, 150))
        if pos.x > 410 and pos.x < 495 and pos.y > 230 and pos.y < 310:
            CheckMark(self.scene, (575, 310))
        if pos.x > 410 and pos.x < 495 and pos.y > 330 and pos.y < 410:
            CheckMark(self.scene, (575, 450))
        if pos.x > 410 and pos.x < 495 and pos.y > 465 and pos.y < 545:
            CheckMark(self.scene, (575, 650))


