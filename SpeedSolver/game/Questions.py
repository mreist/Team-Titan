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

Operands = ["+", "-", "*", "/"]

FirstString = ["costs $ ","Bob has ","Bob sells "]
SecondString = [", he has $ ", " , If he used ", (", if he charges $ ")]
ThirdString = [".how many can he buy?", " in his shop, How many will he have left?", ", What is his profit?"]  
WordOperands = ["/", "-", "*"]
Nouns = ["paint buckets", "wheels", "cars", "decals", "rims"]

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
        elif digits == 'OO_Easy':
            self.num1 = random.randint(1, 4)
            self.num2 = random.randint(1, 4)            
            self.num3 = random.randint(1, 4)
            self.num4 = random.randint(1, 4)
            self.num5 = random.randint(1, 4)
            self.op1 = random.choice(Operands)  
            self.op2 = random.choice(Operands)  
            if (self.op1 == '/'):
                self.num1 = self.num2 * self.num4
            if(self.op2 == '/'):
                self.num2 = self.num3 * self.num4
            if(self.op1 == '/' and self.op2 == '/'):
                self.op1 = random.choice(['+', '-', '*'])
        elif digits == 'OO_Med':
            self.num1 = random.randint(2, 8)
            self.num2 = random.randint(2, 8)            
            self.num3 = random.randint(2, 8)
            self.num4 = random.randint(2, 8)
            self.num5 = random.randint(2, 8)
            self.op1 = random.choice(Operands)  
            self.op2 = random.choice(Operands)  
            if (self.op1 == '/'):
                self.num1 = self.num2 * self.num4
            if(self.op2 == '/'):
                self.num2 = self.num3 * self.num4
            if(self.op1 == '/' and self.op2 == '/'):
                self.op1 = random.choice(['+', '-', '*'])
        elif digits == 'OO_Hard':
            self.num1 = random.randint(3, 12)
            self.num2 = random.randint(3, 12)            
            self.num3 = random.randint(3, 12)
            self.num4 = random.randint(1, 5)
            self.op1 = random.choice(Operands)  
            self.op2 = random.choice(Operands)  
            if (self.op1 == '/'):
                self.num1 = self.num2 * self.num4
            if(self.op2 == '/'):
                self.num2 = self.num3 * self.num4
            if(self.op1 == '/' and self.op2 == '/'):
                self.op1 = random.choice(['+', '-', '*'])
                
        elif digits == 'WordProb':
            self.num1 = random.randint(2, 15)
            self.num2 = random.randint(2, self.num1)            
            self.num3 = random.randint(0, 2)
            self.num4 = random.randint(2,15)
            self.font = spyral.Font(DEF_FONT, 12, WHITE)
        else:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)

            
        if(Model.RaceSelect == 'Snow'):
            self.font = spyral.Font(DEF_FONT, 32, (70,175,175))
        elif digits == 'WordProb': 
            self.font = spyral.Font(DEF_FONT, 18, WHITE)
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
        elif operator == 'OrOfOp':
            self.answer = eval(str(self.num1) + str(self.op1) + str(self.num2) + str(self.op2) + str(self.num3))
            self.image = self.font.render(str(self.num1) + str(self.op1) + str(self.num2) + str(self.op2) + str(self.num3) + "= ?")
            self.output = (str(self.num1) + str(self.op1) + str(self.num2) + str(self.op2) + str(self.num3) + "=" + str(self.answer))


        elif operator == 'WordProb':
            constant = self.num3
            self.num4 = self.num1 * self.num2
            if(constant == 0):
                self.noun1 = random.choice(Nouns)
                self.answer = eval(str(self.num4) + WordOperands[constant] + str(self.num2))
                self.image = self.font.render(self.noun1 + " "+ FirstString[constant] + str(self.num2) + SecondString[constant] + str(self.num4) + ThirdString[constant])
                self.output = (str(self.num4) + WordOperands[constant] + str(self.num2) + "=" + str(self.answer))
            
            elif(constant == 1):
                self.noun2 = random.choice(Nouns)
                self.answer = eval(str(self.num1) + WordOperands[constant] + str(self.num2))
                self.image = self.font.render(FirstString[constant] + str(self.num1) + " "+ self.noun2 + SecondString[constant] + str(self.num2) + ThirdString[constant])
                self.output = (str(self.num1) + WordOperands[constant] + str(self.num2) + "=" + str(self.answer))
                
            elif(constant == 2):
                self.noun3 = random.choice(Nouns)
                self.answer = eval(str(self.num1) + WordOperands[constant] + str(self.num2))
                self.image = self.font.render(FirstString[constant]  + str(self.num1) + " "+self.noun3 + SecondString[constant] + str(self.num2) + ThirdString[constant])
                
                self.output = (str(self.num1) + WordOperands[constant] + str(self.num2) + "=" + str(self.answer))                        
            

