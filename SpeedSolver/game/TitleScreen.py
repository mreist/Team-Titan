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

class Title(spyral.Scene):
    def __init__(self):
        super(Title, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Title_Menu.png")

        spyral.event.register("input.mouse.down", self.GoToMainMenu)
		
    def GoToMainMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())  
