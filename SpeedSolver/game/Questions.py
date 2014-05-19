import spyral 
import random
import operator
import math
import Model

WIDTH = 1200
HEIGHT = 900
WHITE = (255, 255, 255)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

#Array of operands
Operands = ["+", "-", "*", "/"]

FirstString = ["costs $ ","Bob has ","Bob sells "]
SecondString = [", he has $ ", ", if he used ", (", if he charges $ ")]
ThirdString = [".how many can he buy?", " in his shop, how many will he have left?", ", what is his profit?"]  
WordOperands = ["/", "-", "*"]
Nouns = ["paint buckets", "wheels", "cars", "decals", "rims"]


class Question(spyral.Sprite):
    def __init__(self, scene, operator, digits):
        spyral.Sprite.__init__(self, scene)
        self.anchor = 'midbottom'

        #Addition and Subtraction number ranges for Easy, Medium, and Hard
        if digits == 'AS_Easy':
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, self.num1)
        elif digits == 'AS_Med':
            self.num1 = random.randint(10, 30)
            self.num2 = random.randint(10, self.num1)
        elif digits == 'AS_Hard':
            self.num1 = random.randint(30, 99)
            self.num2 = random.randint(30, self.num1)

        #Multiplication and Division number ranges for Easy, Medium, and Hard
        elif digits == 'MD_Easy':
            self.num1 = random.randint(1, 6)
            self.num2 = random.randint(1, 6) 
        elif digits == 'MD_Med':
            self.num1 = random.randint(6, 12)
            self.num2 = random.randint(1, 12)
        elif digits == 'MD_Hard':
            self.num1 = random.randint(10, 20)
            self.num2 = random.randint(1, 12) 

        #Negative number ranges for Easy Medium and Hard
        elif digits == 'NEG_Easy':
            self.num1 = random.randint(1, 4)
            self.num2 = random.randint(-4, -1)
            self.num3 = random.randint(1, 4)
            self.op1 = random.choice(Operands)

            #This line makes sure that the Dividend is ALWAYS a multiple of the Divisor to produce whole number Quotients
            if(self.op1 == '/'):
                self.num1 = self.num3*self.num2  
        elif digits == 'NEG_Med':
            self.num1 = random.randint(2, 8)
            self.num2 = random.randint(-8, -2)
            self.num3 = random.randint(2, 8)
            self.op1 = random.choice(Operands)
            if(self.op1 == '/'):
                self.num1 = self.num3*self.num2
        elif digits == 'NEG_Hard':
            self.num1 = random.randint(3, 12)
            self.num2 = random.randint(-12, -3)
            self.num3 = random.randint(3, 12)
            self.op1 = random.choice(Operands)
            if(self.op1 == '/'):
                self.num1 = self.num3*self.num2 

        #Order Of Operations number ranges for Easy, Medium, and Hard
        elif digits == 'OO_Easy':
            self.num1 = random.randint(1, 4)
            self.num2 = random.randint(1, 4)            
            self.num3 = random.randint(1, 4)
            self.num4 = random.randint(1, 4)
            self.num5 = random.randint(1, 4)

            #Gets 2 random Operators
            self.op1 = random.choice(Operands)  
            self.op2 = random.choice(Operands)  
            if (self.op1 == '/'):
                self.num1 = self.num2 * self.num4
            if(self.op2 == '/'):
                self.num2 = self.num3 * self.num4
            
            #Prevents dividing twice, the only way this worked with whole numbers was to create very large Dividends. If it divides twice, it will instead replace the first op with a new operand
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
            self.num1 = random.randint(6, 25)
            self.num2 = random.randint(6, self.num1)            
            self.num3 = random.randint(0, 2)
            self.font = spyral.Font(DEF_FONT, 12, WHITE)

        else:
            self.num1 = random.randint(1, 10)
            self.num2 = random.randint(1, 10)

        #Changes font color for snow level since white did not appear well            
        if(Model.RaceSelect == 'Snow'):
            self.font = spyral.Font(DEF_FONT, 32, (70,175,175))
        elif digits == 'WordProb': 
            self.font = spyral.Font(DEF_FONT, 18, WHITE)
        else:
            self.font = spyral.Font(DEF_FONT, 32, WHITE)
        
        #Determines answers, draws questions on road, and draws feedback
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
        elif operator == 'negative':
            self.answer = eval(str(self.num1) + str(self.op1) + str(self.num2))
            self.image = self.font.render("(" + str(self.num1) + ")" + str(self.op1) + "(" + str(self.num2) + ")= ?")
            self.output = "(" + (str(self.num1) + ")" + str(self.op1) + "(" + str(self.num2) + ")=" + str(self.answer))
            
        elif operator == 'WordProb':
            constant = self.num3
            self.num4 = self.num1 * self.num2
            if(constant == 0):
                self.noun1 = random.choice(Nouns)
                self.answer = eval(str(self.num4) + WordOperands[constant] + str(self.num2))
                self.image = self.font.render(self.noun1.title() + " "+ FirstString[constant] + str(self.num2) + SecondString[constant] + str(self.num4) + ThirdString[constant])
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

