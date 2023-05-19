#Experiment 6 is for delete  a Particual SMS using the Message Index or all Messages

#GSM

import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

def delSMS():
        print ""
	try:
		temp=input("Enter the Message Index Number You want to Delete (OR) 0 to delete all messages :  ")
		if temp<=15 and temp>=1 or temp==0:
			if temp==0:
				temp="1,4"
			port.write("AT+CMGD="+str(temp)+"\r")
        		stat=port.read(20)
        		#print stat
        		#time.sleep(5)
			print "\n"
			print "Messages deleted successfully"
		else:
			sys.exit(0)
	except:
		print "Wrong Input."
		sys.exit(0)
def writeAT():
	try:
        	#port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
        	port.write('AT'+'\r\n')
        	#print "Writing AT Command..."
        	rcv = port.read(10)
        	#print "Response "
        	print ""
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
                #print ""
                delSMS()
else:
                print "Reset The GSM Module and Try Again.."
                exit()


#GSM

