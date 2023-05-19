#Experiment 6 is for Check The Network Registration Status of the SIM Card.

#GSM

import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)


def checkSim():
	print ""
	port.write("AT+CPIN=?"+"\r\n")
	time.sleep(5)
	stat=port.read(100)
	stat = stat.replace("AT+CPIN=?","")
	stat = stat.strip()
	if stat=="OK":
		print "SIM is Ready."
	else:
		print "SIM is Not Ready."


def devinfo(at):
        print ""
        port.write(at+"\r\n")
        time.sleep(5)
        stat=port.read(2000)
        stat = stat.replace(at,"")
	stat = stat.replace("OK","")
        stat = stat.strip()
	print stat+"\n"
	return stat

def checkReg():
	print ""
        port.write("AT+CREG?\r\n")
        stat=port.read(50)
	#print stat
        stat = stat.replace("+CGREG:","")
	stat = stat.replace("OK","")
	stat = stat.replace("AT+CGREG?","")
	stat = stat.replace("AT+CREG?","")
	stat = stat.replace("+CREG:","")
	stat = stat.strip()
	print stat+"\n"
	if stat=="0,0":
		print "Not Registered, Searching a New Operator to Register to..\n"
	if stat=="0,1":
		print "Registered, and in Home Network..\n"
	if stat=="0,2":
		print "Searching..\n"		
	if stat=="0,3":
		print "Registration Denied..\n"
	if stat=="0,5":
		print "Registered But Not in Home Network(Roaming)..\n"
        
    

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
		print "Reset the GSM Module and Try Again.. "
		sys.exit(0)

status = writeAT()

if status=="ATOK":
                print "GSM SIM900 is Ready To Use..."
                #print ""
		checkSim()
		devinfo("AT+CGMI")
		devinfo("AT+CGMM")
		devinfo("AT+CGMR")
		stat = devinfo("AT+CFUN?")
		if stat=="+CFUN: 1":
			print "Device has Full Functionality.."
		
		
                checkReg()
else:
                print "Reset The GSM Module and Try Again.."
                sys.exit(0)



#GSM

