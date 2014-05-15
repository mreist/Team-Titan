import spyral 
import random
import math
import MainScreen
import Player
import TextInterface

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"
#Creates a leaderboard scene so that we can display the fastest student
#Not sure if we are going to display an image or text list of the students
class LeaderboardScene(spyral.Scene):
    def __init__(self):
        super(LeaderboardScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        i = 0
        n = 1
        TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (0, 0, 0)), (WIDTH/2 - 225, 40), "Initials")
        TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (0, 0, 0)), (WIDTH/2 + 100, 40), "Time (seconds)")
        
        for player in Player.top10:
            name = player[0]
            time = str(player[1])
            if time == '1000000':
                time = ''
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (0, 0, 0)), (WIDTH/2 - 225, 110 + i), str(n) + ". " + name)
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (0, 0, 0)), (WIDTH/2 + 100, 110 + i), time)
            i += 70
            n += 1
        self.background = spyral.Image("images/LeaderboardBackground.png")

        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
		
        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.BackButton.pos = ((WIDTH/2)-50, (HEIGHT/2) + 350)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)

	
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())