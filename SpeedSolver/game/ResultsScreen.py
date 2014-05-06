import spyral
import Race
import Player
import TextInterface
import MainScreen
import pygame
import LeaderBoard

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
yay = pygame.mixer.Sound("yay.wav")
fanfare = pygame.mixer.Sound("fanfare.wav")


class ResultsScreen(spyral.Scene):
    def __init__(self):
        super(ResultsScreen, self).__init__(SIZE)
        
       
        fanfare.play(0)
        
        intials = ''
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            RetryButton = spyral.widgets.Button("Race Again")
            InitialsInput = spyral.widgets.TextInput(150, "Enter your initials")
            EnterButton = spyral.widgets.Button("Enter")
        
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH/2), (HEIGHT-50))
        self.my_form.RetryButton.pos = ((WIDTH/2 - 200), (HEIGHT-50))

        self.my_form.InitialsInput.pos = ((WIDTH/2 - 200), (HEIGHT-100))
        self.my_form.EnterButton.pos = ((WIDTH/2 - 50), (HEIGHT-100))



        
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        spyral.event.register("form.RegisterForm.RetryButton.clicked", self.retry)
        spyral.event.register("form.RegisterForm.EnterButton.clicked", self.enterInitials)
        self.background = spyral.Image("images/Background.png")
        time = Player.currentTime
        
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 100), 'You did it!! Your time was %.2f.' %time)
        if Player.firstPlay == True:
            Player.bestTime = Player.currentTime
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 200), 'Try to beat it next time!')
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 300), 'You received a token for your speedy racing.')
            Player.tokens += 1
            Player.firstPlay = False
        elif (time < Player.bestTime):
            lasttime = Player.bestTime
            yay.play(0)
            Player.bestTime = time
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 200), 'Wow! You beat your previous best time of ' + str(lasttime) + '.')
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 300), 'You got 2 tokens. Nice!')
            Player.tokens += 2
        else:
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 200), 'Your best time is ' + str(Player.bestTime) + '.')
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 300), 'You received a token for your speedy racing.')
            Player.tokens += 1
        
        if time < Player.top10[0][1]:
            
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), ((WIDTH/2 - 400), (HEIGHT-200)), 'Wow! You got a high score! 2 extra tokens 4U! Enter your initials.')
            Player.tokens += 2


    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
    
    def retry(self):
        spyral.director.pop
        spyral.director.push(Race.RaceScene())

    def enterInitials(self):
        i = 0
        playerAdded = False
        newplayer = [self.my_form.InitialsInput.value, Player.currentTime]
        for player in Player.top10:
            if (player[1] == 1000000) and (playerAdded == False):
                Player.top10[i] = newplayer
                playerAdded = True
            i += 1   
        Player.top10.sort(key=lambda player: player[1])
        spyral.director.pop
        spyral.director.push(LeaderBoard.LeaderboardScene())
