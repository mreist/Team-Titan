import spyral 
import random
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class Vehicles(spyral.Sprite):
    def __init__(self, scene):
		super(Vehicles, self).__init__(scene)
        
		#self.image = spyral.Image(size=(300, 100))
        #Based on which vehicle they select use a switch statement to select self.image
		self.image = spyral.Image("images/Car.png")
		self.anchor = 'center'     #Default anchor is 'topleft'

		self.speed = 0
