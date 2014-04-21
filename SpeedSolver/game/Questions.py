import spyral 
import random
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class Question(spyral.Sprite):
    def __init__(self, scene, operator, digits):
        spyral.Sprite.__init__(self, scene)
        self.anchor = 'midbottom'
        if digits == 1:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
        elif digits == 2:
            self.num1 = random.randint(10, 100)
            self.num2 = random.randint(10, 100)
        elif digits == 3:
            self.num1 = random.randint(100, 1000)
            self.num2 = random.randint(100, 1000)
        else:
            self.num1 = random.randint(1, 10000000)
            self.num2 = random.randint(1, 10000000)
            
        self.font = spyral.Font(DEF_FONT, 36)
        
        if operator == 'addition':
            self.answer = self.num1 + self.num2
            self.image = self.font.render(str(self.num1) + "+" + str(self.num2) + "= ?")
        elif operator == 'multiplication':
            self.answer = self.num1*self.num2
            self.image = self.font.render(str(self.num1) + "x" + str(self.num2) + "= ?")
        elif operator == 'subtraction':
            self.answer = self.num1-self.num2
            self.image = self.font.render(str(self.num1) + "-" + str(self.num2) + "= ?")
        elif operator == 'division':
            checkdivision(self.num1, self.num2)

    
      
        
    def checkdivision(self, num1, num2):
        if self.num1 % self.num2 == 0:
            self.answer = num1/num2
            self.image = self.font.render(str(self.num1) + "/" + str(self.num2) + "= ?")
        else:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
            checkdivision(num1, num2)
       
