import spyral
import Instructions
import Race
import RaceSelection
import LeaderBoard
WIDTH = 1200
HEIGHT = 900

#Creates Tree Image
class Tree(spyral.Sprite):
    def __init__(self, scene):
        super(Tree, self).__init__(scene)

        self.image = spyral.Image("images/Pine-Tree.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/4)

#Creates Large Cloud Image
class LargeCloud(spyral.Sprite):
    def __init__(self, scene):
        super(LargeCloud, self).__init__(scene)

        self.image = spyral.Image("images/Large-Cloud.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/13)

#Creates Small Cloud Image
class SmallCloud(spyral.Sprite):
    def __init__(self, scene):
        super(SmallCloud, self).__init__(scene)

        self.image = spyral.Image("images/Small-Cloud.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/7)

#Creates Road Line Images
class RoadLines(spyral.Sprite):
    def __init__(self, scene):
        super(RoadLines, self).__init__(scene)

        self.image = spyral.Image("images/Line.png")
        self.anchor = 'center'

#Creates City Image
class City(spyral.Sprite):
    def __init__(self, scene):
        super(City, self).__init__(scene)

        self.image = spyral.Image("images/City.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, (HEIGHT/4)+50)

#Creates Snowman Image
class Snowman(spyral.Sprite):
    def __init__(self, scene):
        super(Snowman, self).__init__(scene)

        self.image = spyral.Image("images/Snowman.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/4 +150)

#Creates Crab Image
class Crab(spyral.Sprite):
    def __init__(self, scene):
        super(Crab, self).__init__(scene)

        self.image = spyral.Image("images/Crab.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/4 +200)

#Creates Bob Image
class Bob(spyral.Sprite):
    def __init__(self, scene):
        super(Bob, self).__init__(scene)

        self.image = spyral.Image("images/Bob.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 150, HEIGHT/4 +125)

#Creates Face Image
class RRFace(spyral.Sprite):
    def __init__(self, scene):
        super(RRFace, self).__init__(scene)

        self.image = spyral.Image("images/RRFace.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 150, HEIGHT/4+25)

#Creates Star Image
class RRStar(spyral.Sprite):
    def __init__(self, scene):
        super(RRStar, self).__init__(scene)

        self.image = spyral.Image("images/RRStars.png")
        self.anchor = 'midleft'
        self.pos = (0, HEIGHT/2 - 90)

#Creates Instructions Button
class Instructions_But(spyral.Sprite):
    def __init__(self, scene):
        super(Instructions_But, self).__init__(scene)

        self.image = spyral.Image("images/InstructionsButton.png")
        self.anchor = 'topleft'
        self.pos = (100, 600)

        spyral.event.register("input.mouse.down.left", self.goToInstructions)	

    def goToInstructions(self, pos):
        if self.collide_point(pos):
            spyral.director.pop
            spyral.director.push(Instructions.InstructionScene())

#Creates Select Race Button
class SelectRace_But(spyral.Sprite):
    def __init__(self, scene):
        super(SelectRace_But, self).__init__(scene)
        
        self.image = spyral.Image("images/SelectRaceButton.png")
        self.anchor = 'topleft'
        self.pos = (450, 575)

        spyral.event.register("input.mouse.down.left", self.goToRace)	

    def goToRace(self, pos):
        if self.collide_point(pos):
            spyral.director.pop
            spyral.director.push(RaceSelection.RaceSelection())

#Creates Leaderboard Button
class Leaderboards_But(spyral.Sprite):
    def __init__(self, scene):
        super(Leaderboards_But, self).__init__(scene)
        
        self.image = spyral.Image("images/LeaderboardsButton.png")
        self.anchor = 'topleft'
        self.pos = (900, 600)

        spyral.event.register("input.mouse.down.left", self.goToLeaderboard)	

    def goToLeaderboard(self, pos):
        if self.collide_point(pos):
            spyral.director.pop
            spyral.director.push(LeaderBoard.LeaderboardScene())
