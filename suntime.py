
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

#-----------------------------------------------------------
#Fixed Constant for all moving squares:
fixedWidth = 20
fixedHeight = 20 
    
#-----------------------------------------------------------
#Task: For the millisecond time component, propel rectangle across screen
#in accordance to visual timekeeping of milliseconds with limit of seconds
    
#Setup According Constants in section
#ms stands for milliseconds
current_time = datetime.datetime.now()
currentDateAndTime = datetime.datetime.now()
hour = int(currentDateAndTime.hour)
y1 = 60 #Fixed
y2 = 80 #Fixed
colorID = "#ffff33" #Yellow
    
    #-----------------------------------------------------------


while True:
    
    #If Bottom botton is pressed, show sunrise
    if buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill="#FF0000")
        currentDateAndTime = datetime.datetime.now()
        hour = int(currentDateAndTime.hour)
        print("Press the Top button to see sunset time")
        y = 100
        x = 25
        s1 = 6
        print(hour)
        tdiff = s1 - hour
        #tdiff = -11
        print(tdiff)
        
        if tdiff > 0:
           draw.text((x, y-20), str(tdiff), font=font, fill="#00FF00")
           draw.text((x+25, y-20), "hours to sunrise", font=font, fill="#00FF00")
           draw.text((x-20, y-40), "-----------------------------------", font=font, fill="#00FF00")
           draw.text((x+20, y-50), "East", font=font, fill="#00FF00")
           draw.text((x+150, y-50), "West", font=font, fill="#00FF00")

        if -6 < tdiff < 0:
           draw.text((x, y-20), str(-tdiff), font=font, fill="#00FF00")
           draw.text((x+25, y-20), "hours since sunrise", font=font, fill="#00FF00")
           draw.text((x-20, y-40), "-----------------------------------", font=font, fill="#00FF00")
           draw.text((x+20, y-50), "East", font=font, fill="#00FF00")
           draw.text((x+150, y-50), "West", font=font, fill="#00FF00")

           #Dynamically move the shape with respect to time element:    
           scaleFactorx = ((-tdiff)*(width-fixedWidth))/12 
           X1 = 0 + scaleFactorx #dynamic
           x2 = X1 + 20 #dynamic
           scaleFactory = ((-tdiff)*((height/2)-fixedHeight))/6
           y1 = 60 + scaleFactory #dynamic
           #y2 = fixedHeight + scaleFactory #dynamic
           y2 = y1 + 20 #dynamic
           print(scaleFactory)
           print(y1)
           print(y2)
           print(scaleFactorx)
           print(X1)
           print(x2)

           #shape = [x0, y0, x1, y1]
           shape = [X1,y1,x2,y2] 
           draw.rectangle(shape, outline=0, fill=colorID)
        
        if tdiff <= -6:
           draw.text((x, y-20), str(-tdiff), font=font, fill="#00FF00")
           draw.text((x+25, y-20), "hours since sunrise", font=font, fill="#00FF00")
           draw.text((x-20, y-40), "-----------------------------------", font=font, fill="#00FF00")
           draw.text((x+20, y-50), "East", font=font, fill="#00FF00")
           draw.text((x+150, y-50), "West", font=font, fill="#00FF00")

           #Dynamically move the shape with respect to time element:    
           scaleFactorx = ((-tdiff)*(width-fixedWidth))/12 
           X1 = 0 + scaleFactorx #dynamic
           x2 = X1 + 20 #dynamic
           scaleFactory = ((18-hour)*((height/2)-fixedHeight))/6
           y1 = 60 + scaleFactory #dynamic
           #y2 = fixedHeight + scaleFactory #dynamic
           y2 = y1 + 20 #dynamic
           print(scaleFactory)
           print(y1)
           print(y2)
           print(scaleFactorx)
           print(X1)
           print(x2)

           #shape = [x0, y0, x1, y1]
           shape = [X1,y1,x2,y2] 
           draw.rectangle(shape, outline=0, fill=colorID)
        
        
        if tdiff == 0:
           draw.text((x+25, y-20), "It's sunrise time", font=font, fill="#00FF00")
           draw.text((x-20, y-40), "-----------------------------------", font=font, fill="#00FF00")
           draw.text((x+20, y-50), "East", font=font, fill="#00FF00")
           draw.text((x+150, y-50), "West", font=font, fill="#00FF00")

            #Dynamically move the shape with respect to time element:    
           scaleFactorx = ((-tdiff)*(width-fixedWidth))/12 
           X1 = 0 + scaleFactorx #dynamic
           x2 = X1 + 20 #dynamic
           scaleFactory = ((-tdiff)*((height/2)-fixedHeight))/6
           y1 = 60 + scaleFactory #dynamic
           #y2 = fixedHeight + scaleFactory #dynamic
           y2 = y1 + 20 #dynamic
           print(scaleFactory)
           print(y1)
           print(y2)
           print(scaleFactorx)
           print(X1)
           print(x2)

           #shape = [x0, y0, x1, y1]
           shape = [X1,y1,x2,y2] 
           draw.rectangle(shape, outline=0, fill=colorID)

     #If Top botton is pressed, show sunset
    if buttonB.value and not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill="#00FF00")
        currentDateAndTime = datetime.datetime.now()
        hour = int(currentDateAndTime.hour)
        print("Press the bottom button to see sunrise time")
        y = 100
        x = 25
        s2 = 18
        tdiff = s2 - hour
        if tdiff > 0:
           draw.text((x, y-20), str(tdiff), font=font, fill="#FF0000")
           draw.text((x+25, y-20), "hours to sunset", font=font, fill="#FF0000")
           draw.text((x-20, y-40), "-----------------------------------", font=font, fill="#FF0000")
        if tdiff < 0:
           draw.text((x, y-20), str(-tdiff), font=font, fill="#FF0000")
           draw.text((x+25, y-20), "hours since sunset", font=font, fill="#FF0000")
           draw.text((x-20, y-40), "-----------------------------------", font=font, fill="#FF0000")
        if tdiff == 0:
           draw.text((x+25, y-20), "It's sunset time", font=font, fill="#00FF00")
           draw.text((x-20, y-40), "-----------------------------------", font=font, fill="#FF0000")


    # Display image.
    disp.image(image, rotation)
    time.sleep(.0001)
