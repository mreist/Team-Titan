import spyral 
import random
import math
import MainScreen

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)


class OptionScene(spyral.Scene):
    def __init__(self):
        super(OptionScene, self).__init__(SIZE)

#style that allows custom checkboxes
        self.load_style("game/style.spys")

#Quit button or escape stops the game
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

#Option Scene Background
        self.background = spyral.Image("images/Option_Menu.png")


#Generates the Operand Checkboxes
        class RegisterForm(spyral.Form):
            BackButton = spyral.widgets.Button("Go Back")
            AdditionBox = spyral.widgets.Checkbox()
            SubtractionBox = spyral.widgets.Checkbox()
            MultiplicationBox = spyral.widgets.Checkbox()
            DivisionBox = spyral.widgets.Checkbox()

        my_form = RegisterForm(self)
        my_form.focus()


#Sets the Checkbox positions
        my_form.AdditionBox.pos = (50, 450)
        my_form.SubtractionBox.pos = (50, 650)
        my_form.MultiplicationBox.pos = (600, 450)
        my_form.DivisionBox.pos = (600, 650)
        my_form.BackButton.pos = (1100, 800)


#Goes back to the main menu screen when button is clicked
        spyral.event.register("form.RegisterForm.BackButton.clicked", self.goToMenu)
	
    def goToMenu(self):
        spyral.director.pop
        spyral.director.push(MainScreen.MainMenu())
