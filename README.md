# CMU 16-264-Humanoids: SmartWheels

## Instructors
Professor [Christopher Atkeson](http://www.cs.cmu.edu/~cga/)

Professor [Mike Taylor](https://www.ri.cmu.edu/ri-people/michael-d-taylor/)

## Team Members
Tanushree Mediratta, Yiling Qiao, Lena Li, Krithika Veerappan

## Goals
Our initial goal was to create a self-driving delivery robot. We wanted to achieve this by integrating object detection, and wifi localization to enable the robot to move independently. However, we soon realised that this idea was very ambitious. So, we modified our idea and decided to build a robot that we could control through command line instructions but also had the ability to detect obstacles in its vicinity using distance sensors.

## Motivation
We were really trying to build off of what the users wanted. During the beginning of our project when we were still deciding what we wanted to do, we went around campus asking people what they would like in a robot. The vast majority of people mentioned chores like doing laundry or giving something to someone on the other side of campus, etc. Essentially, routine tasks that this robot can potentially help with. Building based off of what other people wanted and addressing market pull was important to us. 

## Technical Problems Encountered and Fixed
One of the first issues we encountered was the fact that none of us had worked with hardware components before. Thus, we had to familiarize ourselves with Arduino and Raspberry Pi as we went along. 
The second major problem we ran into was when two of the motors stopped responding to any kind of input we would provide the encoders. We spent hours trying to fix this issue by changing the pin allocations and power supply connections of each of the encoders, but nothing seemed to work. Thus, we decided to move on and make the best use of the two remaining wheels to figure out a way to make the robot move in all four directions. We were able to accomplish this by providing the encoders appropriate bit vectors based on which direction we wanted the robot to move in. 
Lastly, we had a lot of issues trying to integrate all the different components together. Following are the three different parts of this project that we got to work individually- 
* The robot could be controlled using command line instructions
* The distance sensors worked correctly- we were able to read the voltage we received from the sensors and convert it into distance in centimeters.
* Facial recognition worked- the robot was able to correctly identify the person it was asked to find and then move towards it. (self-driving in a sense)

Though, we were able to integrate facial recognition with the part of the code that managed the motors of our robot vehicle, we were not able to integrate the code that manipulated the distance sensor data. We figured that this was potentially happening due to interfering analog pin signals. Unfortunately, we ran out of time before we could fix this problem.

## Next Steps
If we had more time, we would have liked to work on the following:
* A  wireless way of communicating with the robot by finding a way to interface the Raspberry Pi with the Arduino. This would eliminate our current issue of having to walk along with the robot as it moved since the Arduino was directly plugged into our laptop. 
* We would have tried to replace the two motors that stopped responding so that the robot could achieve its goal of being a four-wheeled robot. 
* Make the distance sensors work along with the rest of the code that moves the robot. This would have served as a good first step towards implementing a rudimentary method of detecting obstacles.
* Make the robot taller for practical purposes
* Lastly, we would have liked to sync our code with a database that contained a specific set of directions that would trace the path for the robot, given a destination.

With all of these modifications, we could potentially create a semi-autonomous robot that could move independently in a known environment that remains mostly static and doesn’t receive much moving traffic. Examples of real world applications include- food runner at a restaurant, library assistant, hotel room service, etc.

## Lessons Learnt
We learnt a lot by working on this project. We not only gained technical knowledge, but also gained certain soft skills like learning when to move on and to stay motivated despite many things not working out the way you planned. The biggest takeaway for us was how to deliver a product with the same basic functionality despite the various technical issues we face. We were proud of the fact that even though some of the most vital components broke down and stopped working, we were able to build a working robot.

## Materials Used
* Hardware         : The car, distance sensor, Raspberry PI    
* Communication: Wi-Fi (better not CMU Wi-Fi) or hot-spot (from an Android phone)
* PC                    : Arduino IDE, Python3
* Raspberry PI    : OpenCV, python package (facial-recognition, dlib)

## Tips
- Remember to charge the battery.
- Connect all the wires, including the connections of Raspberry PI to laptop and Arduino to laptop.
- Choose __Auino nano__ in the IDE.
- To run the distance sensor, upload the __./distance/sketch_apr26a.ino__ through Arduino IDE and you can see the distance in centimeter.
- To run the remote control, upload __./RC_Mecanum_PWM/RC_Mecanum_PWM2.ino__ to your Arduino

## Instructions on How to Use the Code
* if you have any question, please contact yilingq97@gmail.com

* First you might want to pip install some packages related to Wi-Fi and serial. Just follow the warning and error information.

* Modify __./wpa_supplicant.config__ according to your own Wi-Fi account and put the __./wpa_supplicant.config__ and __./ssh__ into your PI's SD card.

* Make sure your laptop and Pi are on the same Wi-Fi network, and find your PI's IP address py by typing in your laptop:
`$ ping raspberry.local`

* Put __./facRec/test1.py__ into Raspberry Pi __/home/pi/jovi/16-264-Humanoids/faceRec/test1.py__ (It's already there!) by running in your laptop:
`$ scp ./facRec/test1.py  pi@ip:/home/pi/jovi/16-264-Humanoids/faceRec/`
`password: humanoids`
* Also, put your own photo with name in your Pi: __/home/pi/jovi/16-264-Humanoids/pics/__

* Modify __./run.py__, change the IP address into your current IP (it will change once you are in a new Wi-Fi). Run in your laptop:
`$ python run.py`
and your laptop will connect to your Pi, and run __test1.py__ remotely.

* Follow the instructions, type `face` to go into the self-driving modem or `command` to go to remote control mode.

## Youtube
<a href="http://www.youtube.com/watch?feature=player_embedded&v=WkZyevzvqoY
" target="_blank"><img src="http://img.youtube.com/vi/WkZyevzvqoY/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

Link: https://www.youtube.com/watch?feature=player_embedded&v=WkZyevzvqoY

## Github 
https://github.com/QiaoYiLing/16-264-Humanoids


