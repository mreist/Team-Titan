import spyral 
import random
import operator
import math
import Model

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

opsKeys = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
Operands = ["+", "-", "*", "/"]



class Question(spyral.Sprite):
    def __init__(self, scene, operator, digits):
        spyral.Sprite.__init__(self, scene)
        self.anchor = 'midbottom'
        if digits == 'AS_Easy':
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
        elif digits == 'AS_Med':
            self.num1 = random.randint(10, 50)
            self.num2 = random.randint(10, 50)
        elif digits == 'AS_Hard':
            self.num1 = random.randint(50, 150)
            self.num2 = random.randint(50, 150)
        elif digits == 'MD_Easy':
            self.num1 = random.randint(1, 6)
            self.num2 = random.randint(1, 6) 
        elif digits == 'MD_Med':
            self.num1 = random.randint(6, 12)
            self.num2 = random.randint(1, 12)
        elif digits == 'MD_Hard':
            self.num1 = random.randint(10, 20)
            self.num2 = random.randint(1, 12) 
        elif digits == 'OrderOps':
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10) 
            self.num3 = random.randint(1, 10) 
            self.op1 = random.choice(Operands)  
            self.op2 = random.choice(Operands)            

        else:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)
            
        if(Model.RaceSelect == 'Snow'):
            self.font = spyral.Font(DEF_FONT, 32, (70,175,175))
        else:
            self.font = spyral.Font(DEF_FONT, 32, WHITE)
        
        
        if operator == 'addition':
            self.answer = self.num1 + self.num2
            self.image = self.font.render(str(self.num1) + "+" + str(self.num2) + "= ?")
            self.output = (str(self.num1) + "+" + str(self.num2) + "=" + str(self.answer))
        elif operator == 'multiplication':
            self.answer = self.num1*self.num2
            self.image = self.font.render(str(self.num1) + "x" + str(self.num2) + "= ?")
            self.output = (str(self.num1) + "*" + str(self.num2) + "=" + str(self.answer))
        elif operator == 'subtraction':
            self.answer = self.num1-self.num2
            self.image = self.font.render(str(self.num1) + "-" + str(self.num2) + "= ?")
            self.output = (str(self.num1) + "-" + str(self.num2) + "=" + str(self.answer))
        elif operator == 'division':
            self.num3 = self.num1*self.num2
            self.answer = self.num3/self.num1
            self.image = self.font.render(str(self.num3) + "/" + str(self.num1) + "= ?")
            self.output = (str(self.num3) + "/" + str(self.num1) + "=" + str(self.answer))
#        elif operator == 'OrOfOp':

            

