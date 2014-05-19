import spyral 
import Images
import Instructions
import Race
import Garage
import LeaderBoard
import RaceSelection

from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

#Draws Garage Image on Main Screen
class drawGarageImage(spyral.Sprite):
    def __init__(self, Scene):
	    spyral.Sprite.__init__(self, Scene)

	    self.anchor = 'center'
	    self.image = spyral.image.Image("images/Garage.png")
	    self.pos = ((WIDTH/2), (HEIGHT/2)-200)

        #Upon click goes into Garage Scene
	    spyral.event.register("input.mouse.down.left", self.handle_clicked)	

    def handle_clicked(self, pos):
        if self.collide_point(pos):
            spyral.director.pop
            spyral.director.push(Garage.GarageScene())

class MainMenu(spyral.Scene):
    def __init__(self):
        super(MainMenu, self).__init__(SIZE)
        

        #Allows users to quit game via quit button or esc key
        spyral.event.register('input.keyboard.down.esc', spyral.director.quit)
        spyral.event.register("system.quit", spyral.director.quit)

        #Sets Main MenuBackground and places Garage image
        self.background = spyral.Image("images/Background.png")
        self.GarageImage = drawGarageImage(self.scene)

        #Sets main menu buttons
        self.leftButton = Images.Instructions_But(self.scene)
        self.midButton = Images.SelectRace_But(self.scene)
        self.rightButton = Images.Leaderboards_But(self.scene)

        spyral.event.register("form.RegisterForm.SoundButton.clicked", self.SwitchSound)
        
    def SwitchSound(self):
        Race.Background_Music
        
        if(Race.Background_Music == True):
            Race.Background_Music = False
        elif(Race.Background_Music == False):
            Race.Background_Music = True
