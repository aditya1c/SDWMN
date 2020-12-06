from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

time = []
etx = []
prev = 0
a = 0
sum1 = 0
sum2 = 0
avg1 = 0
avg2 = 0
after = []
before = []
time_sec = 0

##################################################################################################
pf = open("etx1.txt","r")
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
#MA
# v = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
v = [0.2,0.2,0.2,0.2,0.2]
conetx = np.convolve(etx,v)
conetx = conetx[:-4]
#Plot
pf.close()
# plt.plot(time, etx)
line1, = plt.plot(time[425:575], conetx[425:575], label="Controller A", linewidth=1.0)
#Average for 260 samples
# for i in range(200):
# 	sum1 += conetx[i]
# avg1 = sum1/200
# print avg1
##################################################################################################
pf = open("etx21.txt","r")
time = []
etx = []
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
#MA
# v = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
v = [0.2,0.2,0.2,0.2,0.2]
conetx1 = np.convolve(etx,v)
conetx1 = conetx1[:-4]
#Plot
pf.close()
# plt.plot(time, etx)
line2, = plt.plot(time[425:575], conetx1[425:575], label="Controller B")
#Average for 260 samples
# for i in range(200):
# 	sum2 += conetx1[i]
# avg2 = sum2/200
# print avg2
#####################################################################################################
# role = []
# for i in range(len(conetx)):
# 	if float(conetx[i]) >= float(conetx1[i]):
# 		role.append(4.5)
# 		after.append(conetx1[i])
# 	else:
# 		role.append(1)
# 		after.append(conetx[i])
# line3, = plt.plot(time[600:], after[600:], label="After Handoff")
# # line3, = plt.plot(time, after, label="Role of Controller A", linestyle='--')

#####################################################################################################
#Prediction Graph
A = [1, 2, 3, 4, 5]
x = np.array(A)
role = []
v = [0.2, 0.2, 0.2, 0.2, 0.2]

###################################Extract values from file etx1
fr1 = open('etx1.txt', 'r')
etx1_time = fr1.read().split('\n')
etx1 = []
for i in range(len(etx1_time)):
	etx1.append(float(etx1_time[i].split()[1]))
conetx1 = np.convolve(etx1,v)
conetx1 = conetx1[:-4]
##############
fr21 = open('etx21.txt', 'r')
etx21_time = fr21.read().split('\n')
etx21 = []
for i in range(len(etx21_time)):
	etx21.append(float(etx21_time[i].split()[1]))
conetx21 = np.convolve(etx21,v)
conetx21 = conetx21[:-4]
##################################Extract values from etx21.txt

pr_num = 7.5
for i in range(len(etx1))[4:]:
	B1 = [conetx1[i-4], conetx1[i-3], conetx1[i-2], conetx1[i-1], conetx1[i]]
	B21 = [conetx21[i-4], conetx21[i-3], conetx21[i-2], conetx21[i-1], conetx21[i]]
	y1 = np.array(B1)
	y21 = np.array(B21)
	z1 = np.polyfit(x, y1, 1)
	z21 = np.polyfit(x, y21, 1)
	# future1 = z1[0]*(pr_num**2) + z1[1]*(pr_num) + z1[2]
	# future21 = z21[0]*(pr_num**2) + z21[1]*(pr_num) + z21[2]
	future1 = z1[0]*(pr_num) + z1[1]
	future21 = z21[0]*(pr_num) + z21[1]
	if future1 >= future21:
		role.append("SLAVE")
	else:
		role.append("MASTER")
for i in range(len(role)):
	if role[i] == "MASTER":
		after.append(1)
	else:
		after.append(3)
predict_time = time[4:]
line3, = plt.plot(predict_time[425:575], after[425:575], label="Role of Controller A", linestyle='--')
# print role
#####################################################################################################
#Labels
plt.rcParams.update({'font.size': 30})
plt.xlabel('Time in seconds')
plt.ylabel('ETX')
plt.title('ETX of Switch-1 with Anticipation')
plt.legend(prop={'size':20})
plt.show()