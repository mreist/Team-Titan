import spyral
import MainScreen

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)

class InstructionScene(spyral.Scene):
    def __init__(self):
        super(InstructionScene, self).__init__(SIZE)

        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        self.background = spyral.Image("images/Tutorial.png")

        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")

        self.my_form = RegisterForm(self)

        self.my_form.focus()
        self.my_form.BackButton.pos = ((WIDTH/2) - 50, (HEIGHT/2) + 350)

        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)


    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
