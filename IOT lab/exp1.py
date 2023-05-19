#Experiment 1 is used for checking the gsm module is ready to use using the AT command.
#Check Account Balance
#Check The Signal Strength with ASU and dBm
#Check The Network Provider Name

#GSM

import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB1", baudrate=115200, timeout=1)

def writeAT():
	try:
        	#port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)
        	port.write('AT'+'\r\n')
		print "Writing AT Command..."
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
		sys.exit(0)

status = writeAT()


def checkSig():
		print "\n"
		print "Finding Signal Strength"
		port.write("AT+CSQ\r\n")
	        #port.write("AT+CPBR="ALL"\r\n")
	        stat=port.read(50)
		stat = stat.replace("AT+CSQ","")
	        stat = stat.replace("+CSQ: ","")
		stat = stat.replace(",0","")
		stat = stat.replace("OK","")
		stat = stat.strip()		
		print "\nASU : "+stat
		stat = int(stat)				
		dbm = (2*stat)-113
		print "\nRSSI : "+str(dbm)+"dBm"+"\n"
		if stat>=20 and stat<=30:
			print "Signal Condition is Excellent."
		elif stat>=15 and stat<=19:
			print "Signal Condition is Good."
		elif stat>=10 and stat<=14:
			print "Signal Condition is OK."
		elif stat>=2 and stat<=9:
			print "Signal Condition is Marginal."
		

def checkNet():
		print "\n"
		print "Network Name\n"
		port.write("AT+COPS?\r\n")
	        #port.write("AT+CPBR="ALL"\r\n")
	        stat=port.read(50)
		stat = stat.replace("AT+COPS?","")
	        stat = stat.replace("+COPS: 0,0,","")
		stat = stat.replace("OK","")
		stat = stat.strip()
		print stat
		print "\n"

def checkB():
		print "\n"
		port.write('AT+CUSD=1'+'\r\n')
                #print "Writing AT Command..."
                rcv = port.read(500)
		#print rcv
		rcvList = list(rcv)	
		temp1 = ['A', 'T', '+', 'C', 'U', 'S', 'D', '=', '1', '\r', '\n', '\r', '\n', 'O', 'K', '\r', '\n']
		if rcvList == temp1:
			port.write('AT+CUSD=1,"*111#"'+'\r\n')
                	#print "Writing AT Command..."
			time.sleep(5)
			rcv = port.read(500)
			rcv = rcv.replace("AT+CUSD=1,","")
			rcv = rcv.replace("OK","")
			rcv = rcv.replace("+CUSD: 1,","")
			rcv = rcv.replace("*111*2#","")
			rcv = rcv.replace("*111#","")
			rcv = rcv.strip()			
			print rcv

		else:
			print "AT+CUSD=1 Error.."

if status=="ATOK":
                print "GSM SIM900 is Ready To Use..."
		checkB()
		checkSig()
		checkNet()

else:
                print "Reset The GSM Module and Try Again.."
                sys.exit(0)

#GSM



