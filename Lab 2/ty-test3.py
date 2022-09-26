
import time
from time import strftime, sleep, strptime
import datetime
#import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
#import random


# Configuration for CS and DC pins for Raspberry Pi
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

#Configure Button:
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 255, 255))
#draw.text((100,100),"Do you know when the sunrises and sets?", font = font, fill=(255,255,255)) 
#disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
#padding = -2
#top = padding
#bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
#x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
#draw.text((100,100),"Do you know when the sunrises and sets?", font = font, fill=(100,100,0))
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# button state tracking
buttonA_lastState = False

hexVal = '#%02x%02x%02x' % (0,0,0)
draw.rectangle((0, 0, width, height), outline=0, fill=hexVal) 
draw.text((10,10),"Top button for sunset", font = font, fill=(255,255,255))
draw.text((10,100),"Bottom botton for sunrise", font = font, fill=(255,255,255))

while True:
    
    #Obtain the distance from the prox to determine fill color
   # proxValue = apds.proximity
    #hexVal = '#%02x%02x%02x' % (proxValue*random.randint(0,2),proxValue,round(proxValue/random.randint(1,10)))
    #hexVal = '#%02x%02x%02x' % (0,0,0)
    #print(hexVal)
    #Draw the initial background color
    #draw.rectangle((0, 0, width, height), outline=0, fill=hexVal)  
    
    #If A button is pressed, show the time
    if buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill="#FF0000")
        #datetime = strftime("%m/%d/%Y %H:%M:%S")
        #print(buttonA.value)
        currentDateAndTime = datetime.datetime.now()
        st = int(currentDateAndTime.hour)
        print(st)
        y = 100
        x = 25
        s1 = 4
        tdiff = s1 - st
        print(tdiff)
        if tdiff > 0:
           draw.text((x+35, y-25), str(tdiff), font=font, fill="#00FF00")
           draw.text((x+3, y), "hours to sunrise", font=font, fill="#00FF00")
        if tdiff < 0:
           draw.text((x+35, y-25), str(-tdiff), font=font, fill="#00FF00")
           draw.text((x+3, y), "hours since sunrise", font=font, fill="#00FF00")
        if tdiff == 0:
           draw.text((x+3, y), "It's sunrise time", font=font, fill="#00FF00")
        #hexVal = '#%02x%02x%02x' % (200,0,0)
        #draw.rectangle((0, 0, width, height), outline=0, fill=hexVal)

    #If B  button is pressed, show the time
    if buttonB.value and not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill="#00FF00")
        currentDateAndTime = datetime.datetime.now()
        st = int(currentDateAndTime.hour)
        #dateTime = strftime("%H")
        #print(dateTime)
        print(st)
        #dateTime2 = int(dateTime)
        #current_time = datetime.datetime.now()
        #print(buttonB.value)
        #current_time = datetime.datetime.now()
        y = 100
        x = 25
        #draw.text((x, y), st, font=font, fill="#FF0000")
        s2 = 19
        #FMT = '%H'
        #sunset = time.strptime(s2, FMT)
        #dateTime2 = int(dateTime)
        tdiff = s2 - st
        print(tdiff)
        if tdiff > 0:
           draw.text((x+35, y-25), str(tdiff), font=font, fill="#FF0000")
           draw.text((x+3, y), "hours to sunset", font=font, fill="#FF0000")
        if tdiff < 0:
           draw.text((x+35, y-25), str(-tdiff), font=font, fill="#FF0000")
           draw.text((x+3, y), "hours since sunset", font=font, fill="#FF0000")
        if tdiff == 0:
           draw.text((x+3, y), "It's sunset time", font=font, fill="#00FF00")
        #draw.text((x+35, y-25), str(tdiff), font=font, fill="#FF0000")
        #draw.text((x+3, y), "hours since sunset", font=font, fill="#FF0000")
        #hexVal = '#%02x%02x%02x' % (200,0,0)
        #draw.rectangle((0, 0, width, height), outline=0, fill=hexVal)



    #Isolate hours, minutes, and seconds.
    #current_time = datetime.datetime.now()
    #hour = current_time.hour
    #minute = current_time.minute
    #second = current_time.second
    #milliSecond = current_time.microsecond/1000
    #uSecond = current_time.microsecond

    # Display image.
    disp.image(image, rotation)
    time.sleep(.0001)
