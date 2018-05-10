import serial
from time import sleep
import paramiko

ser = serial.Serial('/dev/cu.usbserial-A505T9I4', 9600) 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.43.191', port=22, username='pi', password='humanoids')
cmd = 'python -u /home/pi/jovi/16-264-Humanoids/faceRec/test1.py'
stdin, stdout, stderr = ssh.exec_command(cmd)


direction = {"f" : "1", "b" : "2", "r" : "3", "l" : "4", "stop" : "5", "start" : "6"}
all_keys = ['f','b','r','l','stop','break']
cmd = 'python -u /home/pi/jovi/16-264-Humanoids/faceRec/test1.py'


while True:
	x = input('choose a mode (face or command): ')
	#if x=='initialface':
	if (x=='face'):
		while True:
			x = input('type the name you want to find:')
			while True:
				camList = []
				flag=False
				for line in stdout:
					txt = line.rstrip()
					print(txt)
					if(txt[0]=='!'):
						pass
					elif txt.split(',')[4]==x:
						flag=True
						break
					camList.append(txt)
					print('time: ',len(camList))
					if len(camList)>20:
						break
				if flag:
					ser.write(direction["f"].encode())
					sleep(0.2) 
					ser.write(direction["stop"].encode())
					sleep(0.2) 
				else:
					ser.write(direction["b"].encode())
					sleep(0.3) 
					ser.write(direction["stop"].encode())
					sleep(0.2) 

	elif (x=='command'):
		while True:
			x = input('type in a command (forward or back or right or left or stop or break): ').split(' ')
			key=x[0]
			if key not in all_keys:
				print('wrong command, please try again')
				continue
			if key=='break':
				break
			if len(x)<2:
				print('please type in run time')
				continue
			wait_time = int(x[1])
			print("key", direction[key])
			ser.write(direction[key].encode())
			sleep(wait_time*2)
			ser.write(direction['stop'].encode())
			sleep(0.01)
			y = ser.readline()
			print(y.decode())
			#sleep(wait_time*2) 
			#.write(direction['stop'].encode())
			#sleep(0.2)
	else:
		print('wrong mode!')
