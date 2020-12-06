import matplotlib.pyplot as plt
import numpy
pf = open("etx1.txt","r")
time = []
etx = []
eetx = []
prev = 0
a = 0
time_sec = 0
#define axes
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
for line in pf:
	a = line.split()
	time_sec_list = a[0].split(':')
	time_sec = float(time_sec_list[0])*3600 + float(time_sec_list[1])*60 + float(time_sec_list[2])
	time.append(time_sec)
	etx.append(float(a[1]))
# Remove Offset in time
remove = time[0]
for i in range(len(etx)):
	time[i] = time[i] - remove
#EWMA
for i in range(len(etx)):
	eetx.append(0.4*prev + 0.6*float(etx[i]))
#MA
v = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
conetx = numpy.convolve(etx,v)
conetx = conetx[:-9]
#Plot
pf.close()
# plt.plot(time, etx)
# plt.plot(time, eetx)
line1, = ax1.plot(time, conetx, label="Controller 1", linewidth=1.0)
##################################################################################################
pf = open("etx21.txt","r")
time = []
etx = []
eetx = []
prev = 0
a = 0
time_sec = 0
for line in pf:
	a = line.split()
	time_sec_list = a[0].split(':')
	time_sec = float(time_sec_list[0])*3600 + float(time_sec_list[1])*60 + float(time_sec_list[2])
	time.append(time_sec)
	etx.append(float(a[1]))
# Remove Offset in time
remove = time[0]
for i in range(len(etx)):
	time[i] = time[i] - remove
#EWMA
for i in range(len(etx)):
	eetx.append(0.4*prev + 0.6*float(etx[i]))
#MA
v = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
conetx1 = numpy.convolve(etx,v)
conetx1 = conetx1[:-9]
#Plot
pf.close()
# plt.plot(time, etx)
# plt.plot(time, eetx)
line2, = ax1.plot(time, conetx1, label="Controller 2", linewidth=4)

#####################################################################################################
role = []
for i in range(len(conetx)):
	if float(conetx[i]) >= float(conetx1[i]):
		role.append(5)
	else:
		role.append(1)
line3, = ax2.plot(time, role, label="Role", linestyle='--')

#####################################################################################################
#Labels
plt.rcParams.update({'font.size': 15})
ax1.set_xlabel('Time in seconds')
ax1.set_ylabel('ETX')
ax2.set_ylabel('Role of Controller A')
plt.title('Role of Controller--Switch 1 versus Time')
plt.legend()
plt.show()