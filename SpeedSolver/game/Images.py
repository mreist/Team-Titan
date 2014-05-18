import spyral
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
