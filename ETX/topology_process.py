fr = open('topology.txt','r')
fw = open('etx21.txt','w')
timedata = fr.read().split('\n\nok\n')
fr.close()
#30 50 80    1 5
src = '10.10.100.5'
dst = '10.10.30.20'
for item in timedata:
	lines = item.split('\n')
	time = lines[0]
	remaining = lines[1:]
	cost = ['100']
	mid = []
	midcost = {}
	floatcost = []
	totalcost = 0
	for line in remaining:
		if line.split('\t')[0] == dst and line.split('\t')[1] == src:
			cost.append(line.split('\t')[4])
	for line in remaining:
		if line.split('\t')[0] == dst and line.split('\t')[1] != src:
			mid.append(line.split('\t')[1])
			midcost[line.split('\t')[1]] = line.split('\t')[4]
	for line in remaining:
		for ip in mid:
						if ip == line.split('\t')[0]:
								if line.split('\t')[1] == src:
										totalcost = float(line.split('\t')[4]) + float(midcost[ip])
										cost.append(str(totalcost))
	for citem in cost:
		floatcost.append(float(citem))
	mincost = min(floatcost)
	fw.write(time + ' ' + str(mincost) + '\n')
fw.close()