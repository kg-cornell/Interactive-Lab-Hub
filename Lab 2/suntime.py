
import time
from time import strftime, sleep, strptime
import datetime
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


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

# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
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
    
    #If Bottom botton is pressed, show sunrise
    if buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill="#FF0000")
        currentDateAndTime = datetime.datetime.now()
        st = int(currentDateAndTime.hour)
        print("Press the Top button to see sunset time")
        y = 100
        x = 25
        s1 = 6
        tdiff = s1 - st
        if tdiff > 0:
           draw.text((x+35, y-25), str(tdiff), font=font, fill="#00FF00")
           draw.text((x+3, y), "hours to sunrise", font=font, fill="#00FF00")
        if tdiff < 0:
           draw.text((x+35, y-25), str(-tdiff), font=font, fill="#00FF00")
           draw.text((x+3, y), "hours since sunrise", font=font, fill="#00FF00")
        if tdiff == 0:
           draw.text((x+3, y), "It's sunrise time", font=font, fill="#00FF00")

     #If Top botton is pressed, show sunset
    if buttonB.value and not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill="#00FF00")
        currentDateAndTime = datetime.datetime.now()
        st = int(currentDateAndTime.hour)
        print("Press the bottom button to see sunrise time")
        y = 100
        x = 25
        s2 = 19
        tdiff = s2 - st
        if tdiff > 0:
           draw.text((x+35, y-25), str(tdiff), font=font, fill="#FF0000")
           draw.text((x+3, y), "hours to sunset", font=font, fill="#FF0000")
        if tdiff < 0:
          draw.text((x+35, y-25), str(-tdiff), font=font, fill="#FF0000")
           draw.text((x+3, y), "hours since sunset", font=font, fill="#FF0000")
        if tdiff == 0:
           draw.text((x+3, y), "It's sunset time", font=font, fill="#00FF00")

    # Display image.
    disp.image(image, rotation)
    time.sleep(.0001)


