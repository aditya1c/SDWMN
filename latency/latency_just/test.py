fr = open('24','r')
fw = open('34','w')
for line in fr:
	a = line.split(':')
	time = float(a[0]) + 2
	fw.write(str(time) + ':' + a[1])
fr.close()
fw.close()