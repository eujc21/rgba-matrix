#Transform an 8 bit image into voltage signals that can be sent out to a RGB board.
#Have a transparent board of 500x500 rgb led behind it.

import os, os.path
from PIL import Image
from time import sleep
#from gpiozero import LED
from decouple import config

# Pulse Width Modulation will control the varying voltages per RGB LED
# There will be a need to know a color diagram of how the picture of values
# create specific colors.

def translateGridToVoltages():
    # Each pixel should be referenced to a voltage value. We will need
    # to send this value to a controller that will select the colors in the right order
    return False

def sendVoltageGridValuesToRGBBoard():
    # Take the array of values and send to the board.
    return False

def connectToRGBBoard():
    # figure out what interface needs to conenct to the board
    return False

def testBoardComponents():
    """
    Testing RGBA component from microcontroller.
    """
    return False

def main():
    """main loop
    1) Test connection with microcontroller.
    2) Initialize default animation.
    3) Display Configured animation.
    """
    img = Image.open('images/cassette.png')
    pix = img.load()
    xImgSize = img.size[0]
    yImgSize = img.size[1]
    imageList= []
    for x in range(xImgSize):
        for y in range(yImgSize):
            imageList.extend(pix[x,y])

    print(imageList[1])

main()
