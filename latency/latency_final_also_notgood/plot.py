import matplotlib.pyplot as plt
pf = open('3',"r");
time = [];
rtt = [];
a = 0
for line in pf:
	a = line.split(':')
	time.append(float(a[0]))
	rtt.append(float(a[1]))

a = time[0]

for i in range(len(rtt)):
	time[i] = time[i] - a
	# if rtt[i]>9000:
	# 	rtt[i] = 1000
pf.close()
plt.plot(time, rtt)	
plt.plot(time, rtt, 'o')

pf = open("23","r");
time = [];
rtt = [];
a = 0
for line in pf:
	a = line.split(':')
	time.append(float(a[0]))
	rtt.append(float(a[1]))

a = time[0]

for i in range(len(rtt)):
	time[i] = time[i] - a
	# if rtt[i]>9000:
	# 	rtt[i] = 1000
pf.close()
plt.plot(time, rtt)	
plt.plot(time, rtt, 'o')

plt.xlabel('Time')
plt.ylabel('RTT')
plt.show()