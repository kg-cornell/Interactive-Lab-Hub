#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import subprocess
import board
import digitalio
from subprocess import call

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)
    
#Temperature Rip
cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}'" 
Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")
print(Temp)

model = Model("model")
# You can also specify the possible word list
#choices = 'fifty sixty seventy'
rec = KaldiRecognizer(model, wf.getframerate())


while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        #print("test")
        print(rec.Result())
        
    #else:
        #print(rec.PartialResult())

number = rec.Result()
print("-----------------------------------------------")
print(number)
#print(number)
correctedTemp = round((float(Temp[-6:-2]))/10)*10 
print(correctedTemp)
call(["espeak","-s100 -ven+18 -z",Temp])
call(["espeak","-s100 -ven+18 -z","CALCULATING BURN TEMPERATURE DISTANCE"])
call(["espeak","-s100 -ven+18 -z","I am"])
call(["espeak","-s100 -ven+18 -z",str(100-correctedTemp)])
call(["espeak","-s100 -ven+18 -z","Degrees from burning up"])

