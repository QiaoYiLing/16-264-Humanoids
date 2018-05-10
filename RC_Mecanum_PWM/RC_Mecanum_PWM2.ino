/*********************************************************

Quad-Wheel Mecanum Vectoring Robot with RC Control
Brent Clay
SuperDroid Robots
December 1, 2015

This code uses an Arduino Uno mounted on a Quad-Wheel Mecanum Vectoring
platform (TP-152-004, TP-095-004, or TP-252-004). The Arduino commands
two dual channel Sabertooth motor controllers to drive four independent
Mecanum wheels. Sabertooths are set to serial mode with addresses 128
and 129.

This firmware allows vectoring RC control of the robot's motion

Code is written for a Spektrum remote + receiver but could easily be reused
for other RC approaches

Platforms:
http://www.superdroidrobots.com/shop/item.aspx/programmable-mecanum-wheel-vectoring-robot-ig52-db/1788/
http://www.superdroidrobots.com/shop/item.aspx/programmable-mecanum-wheel-vectoring-robot-ig32-sb/1713/
http://www.superdroidrobots.com/shop/item.aspx/programmable-mecanum-wheel-vectoring-robot-ig32-dm/1487/

Motor Controller:
http://www.superdroidrobots.com/shop/item.aspx/sabertooth-dual-12a-motor-driver/1155/

Vectoring Robot Support Page:
http://www.superdroidrobots.com/shop/custom.aspx/vectoring-robots/44/

Spektrum DX5e:
http://www.superdroidrobots.com/shop/item.aspx/spektrum-dx5etransmitter-with-ar610-receiver/992/

***********************************************************/

// ****************************************************
// Libraries
// ****************************************************
#include "hardware.h"
#include "MecanumPWM.h"

// *********************
// RC Vars
// *********************
unsigned long DRIVE_PULSE_WIDTH;
unsigned long TURN_PULSE_WIDTH;
unsigned long STRAFE_PULSE_WIDTH;
float pulseLow = 1051, pulseHigh = 1890;
float mByte = 0, bByte = 0;
float mFloat = 0, bFloat = 0;

//initializing variable to read from python script
char inByte [2] = "5";

//initializing for sensor data
int distData;
int distVal;
int redpin=0;

// Drive commands

float spdMax = 254;

// Initialize motor control
MecanumPWM mecPWM(PwmFRpin, PwmFLpin, PwmRRpin, PwmRLpin, InaFRpin, InbFRpin, InaFLpin, InbFLpin, InaRRpin, InbRRpin,
     InaRLpin, InbRLpin, spdMax);

void setup() {
  pinMode(redpin,OUTPUT);
  Serial.begin(9600); 
  Serial.println("setup");
// Command all motors to stop
   mecPWM.allStop();
// slope/intercept for converting RC signal to range [-1,1]
  mFloat = (float)2 / (pulseHigh - pulseLow);
  bFloat = -1*pulseLow*mFloat;
}

void loop() {
  float driveVal;
  float turnVal;
  float strafeVal;
  int index;
  int a;
  float b;
  float c;
  float val1 = 0;
  float val2 = 0;
  float val3 = 0;
  // Read in the RC pulses
  DRIVE_PULSE_WIDTH = pulseIn(drivePinRC, HIGH);//, PULSEIN_TIMEOUT);
  TURN_PULSE_WIDTH  = pulseIn(turnPinRC, HIGH);//, PULSEIN_TIMEOUT);
  STRAFE_PULSE_WIDTH  = pulseIn(strafePinRC, HIGH);//, PULSEIN_TIMEOUT);
 
  if (DRIVE_PULSE_WIDTH <900 || DRIVE_PULSE_WIDTH > 2000 ) driveVal = 0;
  else (driveVal = convertRCtoFloat(DRIVE_PULSE_WIDTH));
  
  if (TURN_PULSE_WIDTH <900 || TURN_PULSE_WIDTH > 2000) turnVal  = 0;
  else turnVal  = convertRCtoFloat(TURN_PULSE_WIDTH);
  
  if (STRAFE_PULSE_WIDTH <900 || STRAFE_PULSE_WIDTH > 2000) strafeVal = 0;
  else strafeVal = convertRCtoFloat(STRAFE_PULSE_WIDTH);


  if(Serial.available()){ // only send data back if data has been sent
    for (index = 0; index < 1; index = index + 1) {
        inByte[index] = Serial.read(); // read the incoming data and fill up array
    }
  Serial.println(inByte);
  a = atoi(&inByte[0]);
  switch(a){
    case 1: {val1 = 0; val2 = 0; val3 = 1; break;}
    case 2: {val1 = 0; val2 = 0; val3 = -1; break;}
    case 3: {val1 = 0; val2 = -1; val3 = 0; break;}
    case 4: {val1 = 0; val2 = 1; val3 = 0; break;}
    case 5: {val1 = 0; val2 = 0; val3 = 0; break;}
    case 6: {val1 = 0; val2 = 0; val3 = 0; break;}
    default: break;
    }
  
  //a = atof(&inByte[0]); //driveVal
  //b = atof(&inByte[1]); //turnVal
  //c = atof(&inByte[2]); //strafeVal
  //val1 = (a-b)/100;
  //val2 = (b-c)/1;
  //val3 = c;
  }

  //read sensor data
  distData=analogRead(redpin);
  distVal=(6762/(distData-9))-4; //converts from voltage to cm?


  
 /* Old code from website
  Serial.println("drive pulse");
  Serial.println(driveVal);
  Serial.println("turn pulse");  
  Serial.println(turnVal);
  Serial.println("strafe pulse");
  Serial.println(strafeVal);
  calculate and apply pulse width to PWM outputs to motor controllers
  
  mecPWM.commandMotors(1,0,1);
  delay(3000);
  mecPWM.commandMotors(0,0,0);
  delay(2000);
  mecPWM.commandMotors(1, 0.5, 1);
  delay(1000);
  mecPWM.commandMotors(1,0,1);
  delay(3000);
  mecPWM.commandMotors(0,0,0);
  */
//  if (distVal <= 25){
//    mecPWM.commandMotors(0,0,0);
//  }
//  Serial.println(distVal);
  //else {
    //fix driveVal, turnVal, strafeVal depending on user input
  mecPWM.commandMotors(val1, val2, val3);
  if (a == 1) {
    delay(1500);
    mecPWM.commandMotors(0,0,0);
  }
  else if (a == 2) {
    delay(1000);
    mecPWM.commandMotors(0,0,0);
  }
  else if (a == 3 or a == 4) {
    delay(1000);
    mecPWM.commandMotors(0,0,0);
  }
  
  //}
  
  /*by trial and error found fixed following vectors for direction:
   * right = 1, 0, 1
   * left = 0, 1, 0
   * forward = 1, 1, 1
   * reverse = 0, 1, 0
  */
  
  //mecPWM.commandMotors(0,0,1);//forward
  
  /*
  mecPWM.commandMotors(2,1,2);//forward
  delay(3000);
  mecPWM.commandMotors(0,0,0);//stop
  delay(2000);
  mecPWM.commandMotors(1, 0, 1);//right
  delay(2000);
  mecPWM.commandMotors(2,1,2);//forward
  delay(3000);
  mecPWM.commandMotors(-1,0,-1);//left
  delay(3000);
  mecPWM.commandMotors(0,1,0);//reverse
*/
  //mecPWM.debugMotorPrint();
}

float convertRCtoFloat(unsigned long pulseWidth)
{
  // deadband
  if(pulseWidth > 1450 && pulseWidth < 1550) { pulseWidth = (float)(pulseHigh + pulseLow) / 2; }
  
  float checkVal = mFloat*pulseWidth + bFloat - 1;
  checkVal = checkVal < -1 ? -1 : checkVal;
  checkVal = checkVal >  1 ?  1 : checkVal;
  if (pulseWidth = 0) checkVal = 0;
  return checkVal;
}




