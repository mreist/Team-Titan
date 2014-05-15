import spyral
resources  = {}

class Model:        
    Vtype = ""
    LWtype = ""
    RWtype = ""
    RaceSelect = ""


def loadResources():
	    resources["red"] = spyral.image.Image("images/RedCar.png")
	    resources["blue"] = spyral.image.Image("images/BlueCar.png")
	    resources["Lwheel"] = spyral.image.Image("images/Wheel.png")
	    resources["Rwheel"] = spyral.image.Image("images/Wheel.png")
	    resources["LFwheel"] = spyral.image.Image("images/FancyWheel.png")
	    resources["RFwheel"] = spyral.image.Image("images/FancyWheel.png")
	    resources["Night"] = spyral.image.Image("images/NightBackground.png")
	    resources["Day"] = spyral.image.Image("images/Background.png")
	    resources["Snow"] = spyral.image.Image("images/SnowBackground.png")
	    resources["Beach"] = spyral.image.Image("images/BeachBackground.png")
	    resources["PreHist"] = spyral.image.Image("images/PrehistoricBackground.png")
	    resources["RR"] = spyral.image.Image("images/RainbowRoad.png")
	    
	    
	    
	    
