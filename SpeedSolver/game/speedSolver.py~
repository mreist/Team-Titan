import spyral
import random
import math
import pygame

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class Vehicle(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        
        self.image = spyral.Image(size=(300, 100))
        #Based on which vehicle they select use a switch statement to select self.image
        self.image = spyral.Image("libraries/spyral/resources/images/car.png")
        self.anchor = 'center'     #Default anchor is 'topleft'

        self.speed = 0

class Question(spyral.Sprite):
    def __init__(self, scene, location):
        spyral.Sprite.__init__(self, scene)
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.answer = self.num1 + self.num2
        self.font = spyral.Font(DEF_FONT, 36)

        self.image = self.font.render(str(self.num1) + "+" + str(self.num2) + "= ?")

class SpeedSolver(spyral.Scene):
    def __init__(self, *args, **kwargs):
        #What is this?
        #global manager
        spyral.Scene.__init__(self, SIZE)
        #self.background = spyral.Image(size=SIZE).fill(BG_COLOR)

        #Replace with real background
        self.background = spyral.Image("libraries/spyral/resources/images/testBackground.png")

        self.playerVehicle = Vehicle(self)
        self.playerVehicle.pos = (WIDTH/2, HEIGHT/2)

        spyral.event.register('input.keyboard.down.esc', spyral.director.pop)
        spyral.event.register("system.quit", spyral.director.pop)
