import spyral
resources  = {}

class Model:        
    Vtype = ""
    LWtype = ""
    RWtype = ""


def loadResources():
	    resources["red"] = spyral.image.Image("images/redcar.jpg")
	    resources["blue"] = spyral.image.Image("images/CarNoWheels.png")
	    resources["Lwheel"] = spyral.image.Image("images/Wheel.png")
	    resources["Rwheel"] = spyral.image.Image("images/Wheel.png")
