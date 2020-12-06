import time
import os.path
import commands
a = 0
host = ""
port = 20000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
data = "stop"
#status, output = commands.getstatusoutput(ps -A | grep python)
status, output = commands.getstatusoutput('pidof python')
pids = output.split()
pid = pids[-2]
#pid = (output.split())[-2]
while a==0:
	#a = time()
	prevtime = time.time()
	status, output = commands.getstatusoutput('pidof python')
	if pid not in output.split():
		UDPSock.sendto(data, addr)
		stoptime = time.time()
		a = 1
print stoptime-prevtime
print "Program Executed"