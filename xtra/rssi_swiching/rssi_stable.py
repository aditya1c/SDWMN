fr = open('wlan0.txt','r')
fw = open('rssi.txt','w')
for line in fr:
	a = line.split(' ')
	if a[6] == '00:0b:6b:02:0d:13':
		fw.write(a[4]+" "+a[8]+)
fw.close()
fr.close()