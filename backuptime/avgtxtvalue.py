f = open('rolechangetime.txt','r')
total = float(0)
count = 0
# lines = f.read().split('\n')
for line in f:
	total = total + float(line)
	count+= 1
avg = float(total)/float(count)
print avg
print count