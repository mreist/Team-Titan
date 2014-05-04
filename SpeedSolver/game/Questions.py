import spyral 
import random
import math
from array import *

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class Question(spyral.Sprite):
    nums = array('i', [0,0,0])
    operands = array('c', ['a','s','m','d'])
    ops = array('c', [' ', ' '])
    def __init__(self, scene, operator, digits):
        spyral.Sprite.__init__(self, scene)
        self.anchor = 'midbottom'  
        self.font = spyral.Font(DEF_FONT, 36)
        # for beta: have multiple operators for order of op problems
        self.ops[0] = operator 
        if digits == 1:
            self.nums[0] = random.randint(1, 10)
            self.nums[1] = random.randint(1, 10)
        elif digits == 2:
            self.nums[0] = random.randint(10, 100)
            self.nums[1] = random.randint(10, 100)
        elif digits == 3:
            self.nums[0] = random.randint(100, 1000)
            self.nums[1] = random.randint(100, 1000)
        else:
            self.nums[0] = random.randint(1, 10000000)
            self.nums[1] = random.randint(1, 10000000)
        if self.ops[0] == 'a':
            self.answer = self.nums[0] + self.nums[1]
            self.image = self.font.render(str(self.nums[0]) + "+" + str(self.nums[1]) + "= ?")
        elif self.ops[0] == 'm':
            self.answer = self.nums[0]*self.nums[1]
            self.image = self.font.render(str(self.nums[0]) + "x" + str(self.nums[1]) + "= ?")
        elif self.ops[0] == 's': #students know about negative numbers, but can't manipulate them yet
	    if (self.nums[0] < self.nums[1]):
                self.answer = self.nums[1]-self.nums[0]
                self.image = self.font.render(str(self.nums[1]) + "-" + str(self.nums[0]) + "= ?")
            else:
                self.answer = self.nums[0]-self.nums[1]
                self.image = self.font.render(str(self.nums[0]) + "-" + str(self.nums[1]) + "= ?")
        elif self.ops[0] == 'd': #guarantees int division for now
            self.checkdivision(self, self.nums[0], self.nums[1], digits)

            
                
    
      
        
    def checkdivision(self,num1, num2,digits):#continuously generates numbers until answer is int
        if (num1 % num2 == 0):
            self.answer = num1/num2
            self.image = self.font.render(str(num1 + "/" + str(num2) + "= ?"))
        elif(num1 % num2 != 0):
            if digits == 1:
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
            elif digits == 2:
                num1 = random.randint(10, 100)
                num2 = random.randint(10, 100)
            elif digits == 3:
                num1 = random.randint(100, 1000)
                num2 = random.randint(100, 1000)
            else:
                num1 = random.randint(1, 10000000)
                num2 = random.randint(1, 10000000)
            self.checkdivision(self, num1, num2, digits)
       
