#Experiment 3 is for send an sms to a number.

#GSM
import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

def sendSMS():

	print ""
        try:
                num=input("Enter Phone Number to Send SMS ")
        except:
                print "Wrong Input"
                sys.exit(0)
        print ">>>"
        #print type(num)
        if len(str(num))<10 or len(str(num))==0 or len(str(num))>10:
                print "Please Check the Phone Number !"
                sys.exit(0)
        else:
		msg=raw_input("Enter Message Content  \n\n")
                port.write('ATZ\r')
                time.sleep(0.5)
                port.write('AT+CMGF=1\r')
                time.sleep(0.5)
                port.write('''AT+CMGS="''' +str(num) + '''"\r''')
                time.sleep(0.5)
                port.write(msg + "\r")
                time.sleep(0.5)
                port.write(chr(26))
                time.sleep(0.5)
		print "\n"
		resp = port.read(2000)
		#print resp
		num = resp.count("OK")
		#print num
		if num==2:
                	print "Message Send Successfully..."
		else:
			print "Failed To Send Message..."

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
		sendSMS()
		
else:
                print "Reset The GSM Module and Try Again.."
                exit()

#GSM


