fr = open('wlan0.txt','r')
fw = open('rssi.txt','w')
for line in fr:
	a = line.split(' ')
	fw.write(a[4]+" "+a[6]+" "+a[7]+" "+a[8])
	# if a[6] == '00:0b:6b:02:0d:13':
	# 	print a[8]
fw.close()
fr.close()