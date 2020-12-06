import os
import time
import getpass
import commands
import subprocess
from socket import *

def ping_switch(ip_list):
	for ip in ip_list:
		status, output = commands.getstatusoutput("ping -c 2 %s" %ip)
		lines = output.split('\n')
		try:
			rtt_line = lines[-1]
			avg_rtt = rtt_line.split()[3].split('/')[1]
			dev_rtt = rtt_line.split()[3].split('/')[3]
		except:
			avg_rtt = "10000"
			dev_rtt = "10000"
		ping_self_data[ip] = ip + " " + str(time.time.now()) + " " + avg_rtt + " " + dev_rtt
	for data in ping_self_data:
		pingdatafile = pingdatafile + data + " "
	pingdatafile = pingdatafile[:-1]

def file_write(decision_data):
	try:
		f = open('/home/%s/Desktop/rolec.txt' %user, 'w') #changed directory
		f.write(decision_data)
		f.close()
	except:
		print "****************************************"
		print "Decsion Data Write to file failed"
		print "****************************************"

user = getpass.getuser()
ping_self_data = {}
pingdatafile = ''
decision_data = ''
ip_list = ['172.20.0.211'] #changed ip list

host = "127.0.0.1" # set to IP address of target computer
port = 13000
addr = (host, port)
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)
avg_rtt = ''
dev_rtt = ''
while True:
	UDPSock.sendto(pingdatafile, addr)
	time.sleep(5)
	(decisiondata, addr) = UDPSock.recvfrom(buf)
UDPSock.close()
os._exit(0)