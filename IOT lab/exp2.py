#Experiment 2 is used for Making a Voice Call
#Redial 
#Attend a Incoming Calls
#Hangup a Call
#GSM

import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

def reDial():
        print ""
        temp=raw_input("Enter 'redial' for Redial the Last Dialed Number : ")
        if temp=="redial":
                print "OK"
        else:
                print "Wrong Input"
                sys.exit(0)
        port.write("ATDL"+";"+"\r\n")
        stat=port.read(20)
        #print stat
        #time.sleep(5)
	cut()
def cut():
	temp=raw_input("Enter 'cut' to Terminate the Call ")
        print ">>>"
        if temp=="cut":
                port.write("ATH"+"\r\n")
                print "Call Terminated"
		print ">>>"
	menu()
def atCall():
        print ">>>"
        port.write("AT"+"\r\n")
	time.sleep(3)
	stat1=port.read(100)
	print len(stat1)
	print stat1.find("RING")
	if stat1.find("RING")==2 or stat1.find("RING")==12 or stat1.find("RING")==16:
		print "Incomming Call.."
	else:
		print "No Incoming Calls.."
	

def mkCall():
	print ""
	try:
		num=input("Enter Phone Number to Make Call ")
	except:
		print "Wrong Input"
		sys.exit(0)
	print ">>>"
	#print type(num)
	if len(str(num))<10 or len(str(num))==0 or len(str(num))>10 :
		print "Please Check the Phone Number !"
		sys.exit(0)
	#print num
	port.write("ATD0"+str(num)+";"+"\r\n")
        stat=port.read(20)
        #print stat
	#time.sleep(5)
	cut()
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
		sys.exit()

status = writeAT()

def menu():

	if status=="ATOK":
                print "GSM SIM900 is Ready To Use..."
		print "1.Make a New Call."
		print "2.Redial For Last Dialed Number."
		print "3.Attend The Incoming Call."
		print "4.Exit"

		try:
			opt=input("Enter The Option : ")
			if opt==1:
				mkCall()
			if opt==2:
				reDial()
			if opt==3:
				atCall()
			if opt==4:
				port.close()
			
				sys.exit(0)
		except:
			print "Wrong Input.."
			sys.exit(0)
			
			
	else:
                print "Reset The GSM Module and Try Again.."
                exit()


menu()


#GSM




