#GSM
import sys
import serial
import os, time

port = serial.Serial("/dev/ttyUSB1", baudrate=115200, timeout=1)

def task():
         print "1.Send"
         print "2.Recieve"
         print "3.Exit"
         opt = input("Enter Option :")
         if opt==1:
	         gprs("AT+CIPSEND","Starts to Send the Data to  Server..")
	         send()
         if opt==2:
                 while True:
                       recieve()
         if opt==3:
                 menu()
                 sys.exit(0)


def recieve():
	while 1:
		rcv = port.read(50000)
		if list(rcv)==['b', 'a', 'c', 'k', '\r', '\n']:
			task()
			#break
		if len(rcv)==0:
			pass
		else:
			print rcv

def send():

	while 1:
		data=raw_input("->")
		if data=="back":
			task()
		port.write(data+chr(26))
		time.sleep(3)
		print port.read(50000)
		#print "Message Send Successfully."
                port.write("AT+CIPSEND"+"\r\n")
		time.sleep(1)
		print port.read(1000)

			
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


def gprs(at,msg):

        print ""
        port.write(at+"\r")
        time.sleep(3)
        stat=port.read(5000)
	#print stat
	stat = stat.replace(at,"")
	stat = stat.replace("SHUT","")
	#stat = stat.replace("OK","")
        stat = stat.strip()
        #print stat+"\n"
	#print len(stat)
	if stat=="OK" or len(stat)>=10 and len(stat)<=20 or stat==">":	
		print msg+"\n"
		if len(stat)>=10 and len(stat)<=20:
			print stat+"\n"	
	else:
		print "Error  "+at

	

status = writeAT()

if status=="ATOK":
                print "GSM SIM900 is Ready To Use..."
		gprs("AT+CIPSHUT","Previous GPRS Connections are Shutdown OK.")
		gprs("AT+CIPMUX=0","Setup The Single Connection Mode OK.")
		gprs("AT+CGATT=1","Attach to the GPRS OK.")
		gprs("""AT+CSTT="www","",""""","Setup the APN,Username,Password  OK.")
		gprs("AT+CIICR","Bring up the GPRS Connection OK.")
		gprs("AT+CIFSR","IP Address is Assigned OK.")

		def connect():
			#try:
				cmd=""
				cType=raw_input("Enter The Connection Type : ")
				host=raw_input("Enter The Server IP Addres :")
				port=raw_input("Enter The PORT Number :")
				cmd = "AT+CIPSTART="+cType+","+host+","+port
				gprs(cmd,"Make Connection To Server OK.")
				#gprs("AT+CIPSEND","Starts to Send the Data to  Server..")
				while True:
					#data = raw_input(" ->")
					#recv = port.read(10000)
					#print recv
					#if data!="close":
						#gprs(data,"Message Send OK.")
						#gprs("#026","EOL OK.")
					#if data=="close":
						#gprs("AT+CIPSHUT","Connection Closed From the Server OK.")
					
					task()


			#except:
				#print "Wrong Input.."	
				#menu()
			
		
		def menu():

			#try:
				print "1.Create New Connection to a Server."
				print "2.Shutdown The GPRS Connections."
				print "3.Exit."
				int=input("Choose Option :")
				if int==1:
					connect()
				if int==2:
					gprs("AT+CIPSHUT","Previous GPRS Connections are Shutdown OK.")
				if int==3:
					sys.exit(0)

			#except:
				#print "Wrong Input.."
				#sys.exit(0)


		menu()
			

else:
                print "Reset The GSM Module and Try Again.."
                sys.exit(0)

#GSM



