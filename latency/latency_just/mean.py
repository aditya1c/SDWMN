import numpy as np
fr = open('1','r')
rtt1 = []
a = 0
for line in fr:
	a = line.split(':')[1]
	rtt1.append(float(a))
	# print a
fr.close()
print "Mean is ", np.mean(rtt1)
print "Variance is ", np.var(rtt1)

fr = open('21','r')
rtt2 = []
a = 0
for line in fr:
	a = line.split(':')[1]
	rtt2.append(float(a))
	# print a
fr.close()
print "Mean is ", np.mean(rtt2)
print "Variance is ", np.var(rtt2)
# print len(rtt1)
# print len(rtt2)
# total = 0
for i in range(219):
	print "Cross Correlation is ", np.corrcoef(rtt1[i:i+3],rtt2[i:i+3])
# total += (np.corrcoef(rtt1[i:i+3],rtt2[i:i+3])[0][1]
# print float(total)/219.0