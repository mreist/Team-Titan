import spyral
import Race
import Player
import TextInterface
import MainScreen

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)
DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class ResultsScreen(spyral.Scene):
    def __init__(self):
        super(ResultsScreen, self).__init__(SIZE)
        
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)
        class RegisterForm(spyral.Form):
            QuitButton = spyral.widgets.Button("Quit")
            RetryButton = spyral.widgets.Button("Race Again")
        
        self.my_form = RegisterForm(self)
        self.my_form.focus()
        self.my_form.QuitButton.pos = ((WIDTH/2), (HEIGHT-50))
        self.my_form.RetryButton.pos = ((WIDTH/2 - 200), (HEIGHT-50))


        
        spyral.event.register("form.RegisterForm.QuitButton.clicked", self.goToMenu)
        spyral.event.register("form.RegisterForm.RetryButton.clicked", self.retry)
        self.background = spyral.Image("images/Background.png")
        time = Player.currentTime
        
        self.timeText = TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 100), 'You did it!! Your time was ' + str(time) + '.')
        if (time < Player.bestTime):
            lasttime = Player.bestTime
            Player.bestTime = time
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 200), 'Wow! You beat your previous best time of ' + str(lasttime) + '.')
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 300), 'You got 2 tokens. Nice!')
            Player.tokens += 2
        else:
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 200), 'Your best time is ' + str(Player.bestTime) + '.')
            TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 300), 'You received a token for your speedy racing.')
            Player.tokens += 1
        TextInterface.TextInterface(self, spyral.Font(DEF_FONT, 24, (255, 255, 255)), (WIDTH/2, 400), 'Total tokens: ' + str(Player.tokens))

        

    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
    
    def retry(self):
        spyral.director.pop
        spyral.director.push(Race.RaceScene())