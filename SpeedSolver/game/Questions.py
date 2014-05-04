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
    operands = array('c', ['a','s','m',' '])
    ops = array('c', [' ', ' '])
    def __init__(self, scene, operator, digits):
        spyral.Sprite.__init__(self, scene)
        self.anchor = 'midbottom'  
        self.font = spyral.Font(DEF_FONT, 36)
        # for beta: have multiple operators for order of op problems
        for (i = 0; i < operator; i++): #selects the operator(s) to be used in the question
            self.temp = random.randint(1, 4)
            while (self.operands[self.temp] == ' '):
                self.temp = random.randint(1, 4)
            self.ops[i] = self.operands[self.temp]
        for (i = 0; i < 4, i++): #fills the int array
            if digits == 1:
                self.nums[i] = random.randint(1, 10)
            elif digits == 2:
                self.nums[i] = random.randint(10, 100)
            elif digits == 3:
                self.nums[i] = random.randint(100, 1000)
            else:
                self.nums[i] = random.randint(1, 10000000)
                
        if self.ops[1] == ' ':
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
        elif self.ops[1] == 'd' or self.ops[1] == 'm':
            if self.ops[1] == 'm':
                if self.ops[0] == 'a':
                    self.answer = self.nums[0] + self.nums[1] * self.nums[2]
                    self.wrongans = (self.nums[0] + self.nums[1]) * self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "+" + str(self.nums[1]) + "x" + str(self.nums[2]) + "= ?")
                if self.ops[0] == 's':
                    self.answer = self.nums[0] - self.nums[1] * self.nums[2]
                    self.wrongans = (self.nums[0] - self.nums[1]) * self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "-" + str(self.nums[1]) + "x" + str(self.nums[2]) + "= ?")
                if self.ops[0] == 'm':
                    self.answer = self.nums[0] * self.nums[1] * self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "x" + str(self.nums[1]) + "x" + str(self.nums[2]) + "= ?")
                if self.ops[0] == 'd':
                    self.answer = self.nums[0] / self.nums[1] * self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "/" + str(self.nums[1]) + "x" + str(self.nums[2]) + "= ?")
            elif self.ops[1] == 'd':
                if self.ops[0] == 'a':
                    self.answer = self.nums[0] + self.nums[1] / self.nums[2]
                    self.wrongans = (self.nums[0] + self.nums[1]) / self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "+" + str(self.nums[1]) + "/" + str(self.nums[2]) + "= ?")
                if self.ops[0] == 's':
                    self.answer = self.nums[0] - self.nums[1] / self.nums[2]
                    self.wrongans = (self.nums[0] - self.nums[1]) / self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "-" + str(self.nums[1]) + "/" + str(self.nums[2]) + "= ?")
                if self.ops[0] == 'm':
                    self.answer = self.nums[0] * self.nums[1] / self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "*" + str(self.nums[1]) + "/" + str(self.nums[2]) + "= ?")
                if self.ops[0] == 'd':
                    self.answer = self.nums[0] / self.nums[1] / self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "/" + str(self.nums[1]) + "/" + str(self.nums[2]) + "= ?")
        else:
            if self.ops[0] == 'a':
                if self.ops[1] == 'a':
                    self.answer = self.nums[0] + self.nums[1] + self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "+" + str(self.nums[1]) + "+" + str(self.nums[2]) + "= ?")
                elif self.ops[1] == 's':
                    self.answer = self.nums[0] + self.nums[1] - self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "+" + str(self.nums[1]) + "-" + str(self.nums[2]) + "= ?")
            elif self.ops[0] == 's':
                if self.ops[1] == 'a':
                    self.answer = self.nums[0] - self.nums[1] + self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "-" + str(self.nums[1]) + "+" + str(self.nums[2]) + "= ?")
                elif self.ops[1] == 's':
                    self.answer = self.nums[0] - self.nums[1] - self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "-" + str(self.nums[1]) + "-" + str(self.nums[2]) + "= ?")
            elif self.ops[0] == 'm':
                if self.ops[1]=='a':
                    self.answer = self.nums[0] * self.nums[1] + self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "x" + str(self.nums[1]) + "+" + str(self.nums[2]) + "= ?")
                elif self.ops[1] == 's':
                    self.answer = self.nums[0] * self.nums[1] - self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "x" + str(self.nums[1]) + "-" + str(self.nums[2]) + "= ?")
            elif self.ops[0] == 'd':
                if self.ops[1]=='a':
                    self.answer = self.nums[0] / self.nums[1] + self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "/" + str(self.nums[1]) + "+" + str(self.nums[2]) + "= ?")
                elif self.ops[1] == 's':
                    self.answer = self.nums[0] / self.nums[1] - self.nums[2]
                    self.image = self.font.render(str(self.nums[0]) + "/" + str(self.nums[1]) + "-" + str(self.nums[2]) + "= ?")



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
       
