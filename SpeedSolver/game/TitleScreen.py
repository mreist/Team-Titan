import spyral 
import random
import math
import MainScreen
import Model
from Model import resources
import pygame
import time


from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
seinfeld = pygame.mixer.Sound("seinfeld.wav")

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

        Model.loadResources()
        Model.LWtype = "Lwheel"
        Model.RWtype = "Rwheel"
        Model.Vtype = "blue"
        
        self.slapbass()
        
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")

        Name = GameName(self)


    def slapbass(self):
        seinfeld.play(0)

#Clicking anywhere will pop the title sceen and push to the Main Menu
        spyral.event.register("input.mouse.down", self.GoToMainMenu)
		
    def GoToMainMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())  
