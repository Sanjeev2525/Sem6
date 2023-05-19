#Experiment 4 is for reading  the inbox messages

import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

def SendCommand(command, getline=True):
        port.write(command)
        data = ''
        if getline:
              data = ReadLine()
        return data

def ReadLine():

        data = port.readline()
        #print data
        return data

def readSMS():
	        
       	 	#print "Read SMS"
	        port.flushInput()
	        port.flushOutput()
		opt=raw_input("Enter ALL To Read all messages (or) Leave this as Empty : ")
		if len(opt)==3 and opt=="ALL":
	                command = 'AT+CMGL="ALL"\r\n' #reads all sms
		elif len(opt)==0:
			try:	
				print "\n"
				index=input("Enter Message Index Number You want to Read :")
                        	command = "AT+CMGR="+str(index)+"\r\n" #reads a sms using index
			except:
				print "\n"
				print "Wrong Input"
				sys.exit(0)
		else:
			print "\n"
			print "Wrong Input"
			sys.exit(0)
			
        	SendCommand(command,getline=True)
        	data = port.readall()
       	 	data = data.replace("+CMGL","Message: ")
		if opt!="ALL":
			data = data.replace("+CMGR:","Message: "+str(index))
        	data = data.replace("OK"," ")
		dataList = ['\r', '\n', 'E', 'R', 'R', 'O', 'R', '\r', '\n']
		temp  = list(data)
		if temp == dataList:
			print "\n"
			print "Message Index Out of Range"
			sys.exit(0)
		print "\n"

		print data
        
def writeAT():
	try:
		#port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
        	port.write('AT'+'\r\n')
        	rcv = port.read(10)
        	#print rcv
        	rcv_list = list(rcv)
        	status = rcv_list[0]+rcv_list[1]+rcv_list[6]+rcv_list[7]
        	return status
        	#print list
        	#print rcv

	except:
		print "Reset The GSM Module and Try Again.."
                exit()


status = writeAT()

if status=="ATOK":
                print "GSM SIM900 is Ready To Use..."
		print "\n"
		readSMS()
		
else:
                print "Reset The GSM Module and Try Again.."
                exit()

#GSM

