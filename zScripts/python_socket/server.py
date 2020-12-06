import os
import time
import getpass
import commands
import subprocess
from socket import *

def ping_switch(ip_list):
	for ip in ip_list:
		status, output = commands.getstatusoutput("ping -c 2 %s -w 4" %ip)
		lines = output.split('\n')
		try:
			rtt_line = lines[-1]
			avg_rtt = rtt_line.split()[3].split('/')[1]
		except:
			avg_rtt = "10000"
			dev_rtt = "10000"
		ping_self_data[ip] = ip + " " + str(time.time()) + " " + str(avg_rtt)


def file_write(decision_data):
	try:
		f = open('/home/%s/Desktop/roles.txt' %user, 'w') #changed directory
		f.write(decision_data)
		f.close()
	except:
		print "****************************************"
		print "Decision Data Write to file failed"
		print "****************************************"

def decision_maker(ip_list, ping_data, ping_self_data):
	for ip in ip_list:
		if (int((ping_data[ip].split())[2]) >= int((ping_self_data[ip].split())[2])):
			decision_data = decision_data + str(int(((ip.split('.'))[2]))*16/10) + " " + "master" + "\n"
		else:
			decision_data = decision_data + str(((ip.split('.'))[2])*16/10) + " " + "slave" + "\n"
	decision_data = decision_data[:-1]

user = getpass.getuser()
ping_self_data = {}
ping_data = {}
decision_data = ''
ip_list = ['10.10.30.20']
count = 0
host = ""
port = 13000
buf = 1024
timestart = 0
timeend = 0
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
while True:
	print "Waiting to Receive Messages..."
    (pingdatafile, addr) = UDPSock.recvfrom(buf)
    print "Received Message: " + pingdatafile
    for i in range((len(pingdatafile.split())/3)):
    	ping_data[pingdatafile.split()[count]] = pingdatafile.split()[count+1] + " " + pingdatafile.split()[count+2] + " "+ pingdatafile.split()[count+3]
    	count = count + 3
    count = 0
    print "************WooHoo***********"
    ping_switch(ip_list)
    try:
    	decision_maker(ip_list, ping_data, ping_self_data)
    except:
    	print "Decision Maker Exception"
    UDPSock.sendto(decision_data, addr)
    file_write(decision_data)
    time.sleep(5)
UDPSock.close()
os._exit(0)