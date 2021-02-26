from guizero import *
from gpiozero import *
from time import *
from threading import *


#Traffic Lights
GPIOTG = LED(17)
GPIOTY = LED(27)
GPIOTR = LED(22)

#Walking Lights
GPIOWG = LED(5)
GPIOWR = LED(6)
GPIOW_Button = Button(26)

    
def Pedestrian():
    GPIOWR.on()
    GPIOTG.on()
    WStop.bg = "red"
    TGreen.bg = "green"
    GPIOW_Button.when_released = WalkGUI
        
   
def WalkGUI():
    GPIOTG.off()
    GPIOTY.on()
    TGreen.bg = "white"
    TYellow.bg = "yellow"
    sleep(5)
    GPIOTY.off()
    GPIOTR.on()
    GPIOWG.on()
    GPIOWR.off()
    TYellow.bg = "white"
    TRed.bg = "red"
    WGo.bg = "blue"
    WStop.bg = "white"
    sleep(10)
    GPIOTR.off()
    GPIOWG.off()
    GPIOWR.on()
    GPIOTG.on()
    TRed.bg = "white"
    WGo.bg = "white"
    WStop.bg = "red"
    TGreen.bg = "green"


if __name__=='__main__':
    app = App("Traffic Light", height  = 500)
    TrafficHeader = Text(app, text = "Traffic Light", align = "top")
    TRed = TextBox(app, width = 10)
    TYellow = TextBox(app, width = 10)
    TGreen = TextBox(app, width = 10)
    WalkHeader = Text(app, text = "Walk Light", align = "top")
    WGo = TextBox(app, width = 10)
    WStop = TextBox(app, width = 10)

    t2 = Thread(target = Pedestrian)

    t2.start()
    app.display()

