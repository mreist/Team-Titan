import spyral 
import random
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class TextInterface(spyral.Sprite):
	def __init__(self, scene, font, position, string):
		super(TextInterface, self).__init__(scene)
		self.font = font
		self.pos = position
		self.text = string
		self.anchor = 'topleft'
		self.image = self.font.render(self.text)

	def update(self, string):
		self.text = string
		self.image = self.font.render(self.text)
