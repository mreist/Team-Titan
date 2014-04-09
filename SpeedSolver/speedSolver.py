import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class Question(spyral.Sprite):
	def __init__(self, scene, location):
		spyral.Sprite.__init__(self, scene)
		self.num1 = random.randint(1, 10)
		self.num2 = random.randint(1, 10)
		self.answer = self.num1 + self.num2
		self.font = spyral.Font(DEF_FONT, 36)

		self.image = self.font.render(str(self.num1) + "+" + str(self.num2) + "= ?")

class Player(spyral.Sprite):
    def __init__(self, scene, location):
        spyral.Sprite.__init__(self, scene)
        self.color = 'pink'
        self.name = 'NO_NAME'
        
class Race(spyral.Sprite):
    def __init__(self, scene, location):
        spyral.Sprite.__init__(self, scene)
        self.distance = 0
        self.Difficulty = 0

class Store(spyral.Sprite):
    def __init__(self, scene, location):
        spyral.Sprite.__init__(self, scene)
        self.parts = 'lasers'

        
class Car(spyral.Sprite):
    def __init__(self, scene, location):
        spyral.Sprite.__init__(self, scene)
        self.speed = 0
        self.color = player.color

class SpeedSolver(spyral.Scene):
    def __init__(self, *args, **kwargs):
        #What is this?
        #global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE).fill(BG_COLOR)

        spyral.event.register("system.quit", spyral.director.pop)
