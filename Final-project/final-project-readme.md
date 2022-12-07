# Voice Controlled Car (VC Car)

Team: Calvin Tirrell, Jason Kwan, Kalyan Gautham

## Concept

We all may have used Remote Controlled Cars, which are controlled by a physical console. However, not everyone would be able to use their hands (owing to disabilities) for controlled these cars. We have built Voice Controlled Car for these people. This car is controlled by voice commands.

## How does it work?


## Work in progress pictures/videos


## How was it built?
1. Chassis and 4 wheels were purchased as a kit
2. Motors and controller were purchased from Amazon
3. Partial wiring was used from IDD kit that was supplied to all students
4. Some wiring and screws were procured from Maker Lab
5. Soldering and crafting the body where needed were done in Maker Lab
6. Niti Parikh and Tyler Bershad guided us in some of the car building activities
7. We referred to online resources for building the motor controld with a controller and raspberry pi. Below are a couple of those liks that helped us build the car
    A. https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
    B. https://www.jameco.com/jameco/workshop/circuitnotes/raspberry-pi-circuit-note.html
    

## What works well?
1. The controller is well connected to the four motors.
2. The car moves smoothly.
3. The car takes 4 voice commands well in a quite environment even at a distance.
4. The parts of the car are placed sturdily and stay intact during mild collusions.


## What didn't work as expected?
1. The voice commands are not recognized well when around a noisy environment.
2. Raspberry Pi needs a stronger batter source which could not fit well on the chassis of the car. Hence, we used a power cord.
3. The voice commands do not recognize all accents.
4. There is a delay between the time the command is delivered by the user and the time the action is executed by the Pi.
5. The battery back for the controller and motors drains out quickly.

## Iterations that failed
1. Initially, we tried to use two controllers for different commands and for two each motors. However, we realized that using only one controller is more efficient.
2. We used a battery pack for the Pi but that couldn't power it enough and using two large batter packs, one for motors and another for Pi was consuming a lot of space that could not be accommodated.
3. We tried to build a two layered chassis for better utility of the space in the car. However, the top layer was not structurally working out. Hence, we had to remove it.


## What are our learnings?
1. The voice controlls can be complicated when it's not enabled to recognize only one person's voice as multiple people can give similar commands or the car can take commands from voices that are not meant to be commands.
2. The voice controlls can be tough if the car moves farther from the user.
3. Speed control commands with voices may not be user friendly.
4. Voice commands become unrealiable wehn given too close or too far from the mic.


## Next steps for improvements
1. Have a more powerful batter for the Pi to make it truly wireless
2. Have the mic placed on the user instead of being mounted on the car and keep the range of voice commands very low so that the voice of only the user is recognized.
3. The speed of the car should be determined by simpler commands such as speed up or speed down with increments of 2 miles/hr speed.
4. The range of the car should be determined so that the car does not move beyond certain distance from the user.
5. The base location should be determined so that the car returns to the base when no further commands or delivered or when the battery is about to drain.
