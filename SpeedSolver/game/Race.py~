import spyral 
import random
import math
import MainScreen
import Vehicle

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
