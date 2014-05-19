import spyral
resources  = {}
# Model class stores image files so they can be loaded when a certain type is selected.
#For example we use Vtype for our Vehicle selection, so if Vtype is set to red then the RedCar.png will display 
class Model:        
    Vtype = ""
    LWtype = ""
    RWtype = ""
    Decal = ""
    RaceSelect = ""
    
    #Either Race or LeaderBoard
    SelectMode = ""


def loadResources():
    #Cars and their colors
    resources["red"] = spyral.image.Image("images/RedCar.png")
    resources["blue"] = spyral.image.Image("images/BlueCar.png")
    resources["green"] = spyral.image.Image("images/GreenCar.png")
    resources["black"] = spyral.image.Image("images/BlackCar.png")
    resources["white"] = spyral.image.Image("images/WhiteCar.png")
    resources["purple"] = spyral.image.Image("images/PurpleCar.png")
    resources["pink"] = spyral.image.Image("images/PinkCar.png")
    resources["orange"] = spyral.image.Image("images/OrangeCar.png")
    resources["yellow"] = spyral.image.Image("images/YellowCar.png")
	    
    #Car Wheels
    resources["Lwheel"] = spyral.image.Image("images/Wheel.png")
    resources["Rwheel"] = spyral.image.Image("images/Wheel.png")
    resources["LFwheel"] = spyral.image.Image("images/FancyWheel.png")
    resources["RFwheel"] = spyral.image.Image("images/FancyWheel.png")

    #Decals
    resources["blank"] = spyral.image.Image("images/Blank.png")
    resources["fire"] = spyral.image.Image("images/Fire.png")
    resources["flower"] = spyral.image.Image("images/Flower.png")
    resources["lightning"] = spyral.image.Image("images/Lightning.png")
    resources["heart"] = spyral.image.Image("images/Heart.png")

    #Race Backgrounds
    resources["Night"] = spyral.image.Image("images/NightBackground.png")
    resources["Day"] = spyral.image.Image("images/Background.png")
    resources["Snow"] = spyral.image.Image("images/SnowBackground.png")
    resources["Beach"] = spyral.image.Image("images/BeachBackground.png")
    resources["PreHist"] = spyral.image.Image("images/PrehistoricBackground.png")
    resources["RR"] = spyral.image.Image("images/RainbowRoad.png")
    resources["Garage"] = spyral.image.Image("images/Garage.png")
    
    #Main Character Bob
    resources["Bob"] = spyral.image.Image("images/Bob.png")
	    
	    
	    
