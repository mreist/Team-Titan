import spyral 
import random
import math
import MainScreen
import model
from model import resources


from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class GameName(spyral.Sprite):
    def __init__(self, scene):
        super(GameName, self).__init__(scene)

        
        self.image = spyral.Image("images/Title.png")
        self.pos = (250, -1000)

        animation = Animation('y', easing.Linear(-1000, 200), duration = 4.0, loop = False)
        self.animate(animation)

#Creates a Title Screen scene
class Title(spyral.Scene):
    def __init__(self):
        super(Title, self).__init__(SIZE)

        model.loadResources()
        model.LWtype = "Lwheel"
        model.RWtype = "Rwheel"
        model.Vtype = "blue"

        
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")

        Name = GameName(self)




#Clicking anywhere will pop the title sceen and push to the Main Menu
        spyral.event.register("input.mouse.down", self.GoToMainMenu)
		
    def GoToMainMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())  
