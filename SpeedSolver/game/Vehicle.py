import spyral 
import random
import math
from spyral import Animation, easing

class Car(spyral.Sprite):
    def __init__(self, scene):
        super(Car, self).__init__(scene)

        self.image = spyral.Image("images/CarNoWheels.png")
        self.anchor = 'center'

class Wheels(spyral.Sprite):
    def __init__(self, scene):
        super(Wheels, self).__init__(scene)

        self.image = spyral.Image("images/Wheel.png")
        self.anchor = 'center'

class Vehicles(spyral.Sprite):
    def __init__(self, scene):
        super(Vehicles, self).__init__(scene)

        #Based on which vehicle they select use a switch statement to select self.image
        Chassis = Car(self)
        LeftWheel = Wheels(self)
        RightWheel = Wheels(self)
        LeftWheel.pos.x = Chassis.pos.x + 10
        RightWheel.pos.x = Chassis.pos.x + 100
        self.anchor = 'center'
        self.speed = 0

#        animation = Animation('x', easing.Linear(0, 600), duration = 3.0, loop = True)
#        self.animate(animation)
