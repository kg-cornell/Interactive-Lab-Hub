
# from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
espeak -ven+f1 -k3 -s150 -a35 --stdout  "Hello,  what do you want to know?" | aplay
arecord -D hw:1,0 -f cd -c1 -r 48000 -d 3 -t wav recorded_mono.wav
#aplay recorded_mono.wav
python3 Kalyan_awesomeScript.py recorded_mono.wav

#echo "some data for the file" >> fileName.txt
