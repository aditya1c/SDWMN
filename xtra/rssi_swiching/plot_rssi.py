import matplotlib.pyplot as plt
pf = open("total_rssi_4.txt","r")
time = []
rssi = []
a = 0
time_sec = 0
for line in pf:
	a = line.split()
	time_sec_list = a[0].split(':')
	time_sec = float(time_sec_list[0]*3600) + float(time_sec_list[1]*60) + float(time_sec_list[2])
	time.append(time_sec)
	rssi.append(float(a[1]))

a = time[0]

for i in range(len(rssi)):
	time[i] = time[i] - a

pf.close()
plt.plot(time, rssi)
plt.xlabel('Time')
plt.ylabel('RSSI')
plt.show()