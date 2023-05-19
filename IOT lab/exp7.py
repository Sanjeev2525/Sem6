import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

def readAllContacts():
        print ">>>"
	port.write("AT+CPBR=1,250"+"\r\n")
	#time.sleep(10)
        stat=port.read(50000)
	stat = stat.replace("+CPBR","Contact ")
	stat = stat.replace("OK","")
        print stat
        #time.sleep(5)
        print "\n"
            
def searchContact():
	print ">>>"
	
def addContact():
	print ">>>"
	port.write("AT+CPBW=,8489317681,128,vicky"+"\r\n")
	time.sleep(5)
	stat=port.read(50)
	print stat	


def writeAT():
        try:
                 #port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout$
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
                print "1.Read All Contacts."
		print "2.Dial Contact."
		print "3.Search a Contact."
		print "4.Add New Contact."
		print "5.Remove Contact."
		print "6.Exit."
		try:
			opt=input("Enter Option : ")
			if opt==1:
                		readAllContacts()
			if opt==2:
				print "Dial.."
			if opt==4:
				addContact()
			if opt==3:
				searchContact()			

			if opt==6:
				sys.exit(0)
		except:
			print "Wrong Input."
			sys.exit(0)
	

	else:
               	print "Reset The GSM Module and Try Again.."
               	exit()



menu()






