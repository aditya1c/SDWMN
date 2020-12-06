import numpy as np
from scipy.optimize import curve_fit
A = [1, 2, 3, 4, 5]
x = np.array(A)
role = []
v = [0.2, 0.2, 0.2, 0.2, 0.2]

#################################################Extract values from file etx1
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
##################################################Extract values from etx21.txt

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
# print future1
# print future21
print role