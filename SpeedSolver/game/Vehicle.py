import spyral 
import random
import math
from spyral import Animation, easing

class Vehicles(spyral.Sprite):
    def __init__(self, scene):
        super(Vehicles, self).__init__(scene)

        #Based on which vehicle they select use a switch statement to select self.image
        self.image = spyral.Image("images/Car.png")
        self.anchor = 'center'
        self.speed = 0

#        animation = Animation('x', easing.Linear(0, 600), duration = 3.0, loop = True)
#        self.animate(animation)
