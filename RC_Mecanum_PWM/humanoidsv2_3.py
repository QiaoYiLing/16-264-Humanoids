import serial
from time import sleep

ser = serial.Serial('/dev/cu.usbserial-A505T9I4', 9600) #always check if listening to correct serial port
#direction = {"forward" : "111", "back" : "010", "right" : "101", "left" : "100", "stop" : "000", "start" : "000"}
direction = {"forward" : "1", "back" : "2", "right" : "3", "left" : "4", "stop" : "5", "start" : "6"}
while (1):
	
	x = raw_input('give a command: ')
	if (x != "quit"):
		if (("stop" not in x) and ("start" not in x)):
			key = x[ : x.find(" ")]
			wait_time = int(x[x.find(" ") + 1 : ])
		else:
			key = x
			wait_time = 0

		print "key", direction[key]

		ser.write(direction[key])
		sleep(0.2)
		print ser.readline()
		sleep(0.2)
		# if (key == "right" or key == "left"):
		# 	ser.write("111")

		# print ser.readline()
		sleep(wait_time*2) #enough time to print everything out
		# index = x.find(" ") + 1 #find the last character which is a number
		# wait_time = float(x[index:])
		# sleep(wait_time * 5)
		# ser.write("000") #stop motion after specified time, wait till next command
		# print "waited"
		# print ser.readline()
		# sleep(0.5)
	else:
		print("Exiting...") #"quit" command exits the function
		ser.write("000")
		break	
	
