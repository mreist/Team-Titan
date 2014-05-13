import spyral
WIDTH = 1200
HEIGHT = 900

class Tree(spyral.Sprite):
    def __init__(self, scene):
        super(Tree, self).__init__(scene)

        self.image = spyral.Image("images/Pine-Tree.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/4)



class LargeCloud(spyral.Sprite):
    def __init__(self, scene):
        super(LargeCloud, self).__init__(scene)

        self.image = spyral.Image("images/Large-Cloud.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/13)



class SmallCloud(spyral.Sprite):
    def __init__(self, scene):
        super(SmallCloud, self).__init__(scene)

        self.image = spyral.Image("images/Small-Cloud.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, HEIGHT/7)

class RoadLines(spyral.Sprite):
    def __init__(self, scene):
        super(RoadLines, self).__init__(scene)

        self.image = spyral.Image("images/Line.png")
        self.anchor = 'center'

class City(spyral.Sprite):
    def __init__(self, scene):
        super(City, self).__init__(scene)

        self.image = spyral.Image("images/City.png")
        self.anchor = 'center'
        self.pos = (WIDTH + 100, (HEIGHT/4)+50)

class Snowman(spyral.Sprite):
    def __init__(self, scene):
        super(Snowman, self).__init__(scene)

        self.image = spyral.Image("images/Snowman.png")
        self.anchor = (WIDTH + 100, HEIGHT/4 +100)
