import spyral
import Race
import Player
import TextInterface
import MainScreen
import pygame
import LeaderBoard
import Model

WIDTH = 1200
HEIGHT = 900
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
yay = pygame.mixer.Sound("yay.wav")
fanfare = pygame.mixer.Sound("fanfare.wav")
reward = None

class ResultsScreen(spyral.Scene):
    def __init__(self):
        super(ResultsScreen, self).__init__(SIZE)
        global reawrd
        

        if Model.RaceSelect == "Day":
            top10 = Player.DayTop10
        elif Model.RaceSelect == "Night":
            top10 = Player.NightTop10
        elif Model.RaceSelect == "Snow":
            top10 = Player.SnowTop10
        elif Model.RaceSelect == "Beach":
            top10 = Player.BeachTop10
        elif Model.RaceSelect == "PreHist":
            top10 = Player.PreHistTop10
        else:
            top10 = Player.RRTop10
         
        if(Model.RaceSelect == "Day" or Model.RaceSelect == "Night"):
            reward = 1
        elif(Model.RaceSelect == "Snow" or Model.RaceSelect == "Beach"):
            reward = 2
        elif(Model.RaceSelect == "PreHist" or Model.RaceSelect == "RR"):
            reward = 3

        fanfare.play(0)
        
        intials = ''
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            RetryButton = spyral.widgets.Button("Race Again")
            InitialsInput = spyral.widgets.TextInput(150, "Enter your initials", text_length = 3)
        
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH/2), (HEIGHT-50))
        self.my_form.RetryButton.pos = ((WIDTH/2 - 200), (HEIGHT-50))
        fontsize = 30
        self.my_form.InitialsInput.pos = ((WIDTH/2 - 200), (HEIGHT-100))
        TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)),((WIDTH/2 - 200), (HEIGHT-200)), 'Enter your initials and press Enter!')



        
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        spyral.event.register("form.RegisterForm.RetryButton.clicked", self.retry)
        spyral.event.register("input.keyboard.down.return", self.enterInitials)
        self.background = spyral.Image("images/Background.png")
        time = Player.currentTime
        locx = WIDTH/2 - 250
        
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)), (locx, 100), 'You did it!! Your time was %.2f.' %time)
        
        if time < top10[0][1]:
            lasttime = Player.bestTime
            yay.play(0)
            Player.bestTime = time
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)), (locx, 200), 'Wow! You beat the fastest time is ' + str(lasttime) + '.')
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)), (locx, 300), 'You got your prize plus an extra token. Nice!')
            Player.tokens += (reward + 1)
        else:
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)), (locx, 200), 'The fastest time is ' + str(Player.bestTime) + '.')
            
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)), (locx, 300), 'Try to beat it next time!')
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)), (locx, 400), 'You received a prize for your speedy racing.')

            Player.tokens += reward

        
        TextInterface.TextInterface(self, spyral.Font(DEF_FONT, fontsize, (255, 255, 255)), (locx, 500), 'Total tokens: ' + str(Player.tokens))


    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
    
    def retry(self):
        spyral.director.pop
        spyral.director.push(Race.RaceScene())

    def enterInitials(self):
        if Model.RaceSelect == "Day":
            top10 = Player.DayTop10
        elif Model.RaceSelect == "Night":
            top10 = Player.NightTop10
        elif Model.RaceSelect == "Snow":
            top10 = Player.SnowTop10
        elif Model.RaceSelect == "Beach":
            top10 = Player.BeachTop10
        elif Model.RaceSelect == "PreHist":
            top10 = Player.PreHistTop10
        else:
            top10 = Player.RRTop10
        i = 0
        playerAdded = False
        newplayer = [(self.my_form.InitialsInput.value).upper(), Player.currentTime]
        for player in top10:
            if (player[1] == 1000000) and not playerAdded:
                top10[i] = newplayer
                playerAdded = True
            i += 1 
        if not playerAdded:
            top10[len(top10)-1] = newplayer
        top10.sort(key=lambda player: player[1])
        self.writeLeaderboardToFile()
        spyral.director.pop
        spyral.director.push(LeaderBoard.LeaderboardScene())
        
    def writeLeaderboardToFile(self):
        if Model.RaceSelect == "Day":
            top10 = Player.DayTop10
        elif Model.RaceSelect == "Night":
            top10 = Player.NightTop10
        elif Model.RaceSelect == "Snow":
            top10 = Player.SnowTop10
        elif Model.RaceSelect == "Beach":
            top10 = Player.BeachTop10
        elif Model.RaceSelect == "PreHist":
            top10 = Player.PreHistTop10
        else:
            top10 = Player.RRTop10
        f = open(Model.RaceSelect + 'LeaderBoard.txt', 'w')
        for player in top10:
            f.write(player[0] + '\n' + str(player[1]) + '\n')
        print('wrote!')
        f.close()

