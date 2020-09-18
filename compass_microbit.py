from microbit import *

compass.calibrate()

while True:
    if compass.heading() < 45 or compass.heading () > 315:
        display.show("N")
    elif compass.heading() < 135:
        display.show("E")
    elif compass.heading() < 225:
        display.show("S")
    else:
        display.show("W")