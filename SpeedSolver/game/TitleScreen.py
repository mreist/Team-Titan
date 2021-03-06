import spyral 
import MainScreen
import Model
from Model import resources
import pygame
import Player

from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
#pygame.mixer.pre_init(44100, -16, 2, 2048)
#pygame.mixer.init()
#seinfeld = pygame.mixer.Sound("seinfeld.wav")

#Creates Game Title image
class GameName(spyral.Sprite):
    def __init__(self, scene):
        super(GameName, self).__init__(scene)
        
        self.image = spyral.Image("images/Title.png")
        self.pos = (250, -1000)
        
        animation = Animation('y', easing.Linear(-1000, 200), duration = 4.0, loop = False)
        self.animate(animation)

#Creates a Title Screen scene
class Title(spyral.Scene):
    def __init__(self):
        super(Title, self).__init__(SIZE)

        #Initializes default car
        Model.loadResources()
        Model.LWtype = "Lwheel"
        Model.RWtype = "Rwheel"
        Model.Vtype = "blue"
        Model.Decal = "blank"
        Model.RaceSelect = "Day"

        #self.slapbass()
        self.loadLeaderBoard()
        
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Background.png")

        Name = GameName(self)


    #def slapbass(self):
        #seinfeld.play(0)
 
    #Loads in leaderboard from text file   
    def loadLeaderBoard(self):
        for board in Player.LeaderBoards:
            f = open(board[1] + 'LeaderBoard.txt', 'r')
            i = 0
            initials = True
            for line in f:
                line = line.rstrip()         
                if initials:
                    board[0][i][0] = line
                    print('read initials: ' + line)
                else:
                    board[0][i][1] = float(line)
                    print('read score: ' + line)
                    i += 1
                initials = not initials
            print('read!')
            f.close()

        #Clicking anywhere or pressing enter will pop the title sceen and push to the Main Menu
        spyral.event.register("input.mouse.down", self.GoToMainMenu)
        spyral.event.register("input.keyboard.down.return", self.GoToMainMenu)
		
    def GoToMainMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())  
