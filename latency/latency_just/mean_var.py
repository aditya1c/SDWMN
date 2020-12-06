import numpy as np
fr = open('1','r')
rtt = []
a = 0
for line in fr:
	a = line.split(':')[1]
	rtt.append(float(a))
	# print a
fr.close()
print np.mean(rtt)
print np.var(rtt)