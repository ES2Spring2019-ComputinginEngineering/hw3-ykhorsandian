#Created by Yassi Khorsandian & Allison Choi

from microbit import *
import math

while True:
    sleep(100)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    rad1 = math.atan2(x, z) #Tilt in x-direction
    rad2 = math.atan2(y, z) #Tilt in y-direction

    deg1 = rad1 / math.pi * 180 #Converting x-tilt from radians to angles
    deg2 = rad2 / math.pi * 180 #Converting y-tilt from radians to angles

    print("x", deg1)
    print("y", deg2)

    if deg1 > 170: #Tilt in x-dimension is negligible
        if deg2 > 170:
            display.show(Image.HAPPY)
        elif deg2 > 0:
            display.show(Image.ARROW_S)
        else:
            display.show(Image.ARROW_N)
    elif deg2 > 170: #Tilt in y-dimension is negligible
        if deg1 > 170:
            display.show(Image.HAPPY)
        elif deg1 > 0:
            display.show(Image.ARROW_E)
        else:
            display.show(Image.ARROW_W)
    elif deg1 < 0: #Tilted in the West direction
        if deg2 > 0:
            display.show(Image.ARROW_SW)
        else:
            display.show(Image.ARROW_NW)
    elif deg1 > 0: #Tilted in the East direction
        if deg2 > 0:
            display.show(Image.ARROW_SE)
        else:
            display.show(Image.ARROW_NE)
    else:
        blank = Image("00000:"
                      "00000:"
                      "00000:"
                      "00000:"
                      "00000:")
        display.show(blank)