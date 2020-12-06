import time
import commands
timestart = 0
timeend = 0
while True:
	timestart = time.time()
	status, output = commands.getstatusoutput("ping -c 1 10.10.80.20 -w 4")
	lines = output.split('\n')
	try:
		rtt_line = lines[-1]
		avg_rtt = rtt_line.split()[3].split('/')[1]
		dev_rtt = rtt_line.split()[3].split('/')[3]
	except:
		avg_rtt = "1000"
		dev_rtt = "1000"
	f = open('pingdata3.txt','a')
	data = str(timestart) + " " + str(avg_rtt) + "\n"
	f.write(data)
	f.close()
	print data
	timeend = time.time()
	time.sleep(5 - timeend + timestart)