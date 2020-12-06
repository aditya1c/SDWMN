from __futre__ import __division__
import matplotlib.pyplot as plt
pf = open("total_role_4.txt","r");
time = [];
role = [];
a = 0
time_sec = 0
for line in pf:
	a = line.split()
	time_start_list = a[0].split(':')
	time_start = float(time_start_list[0]*3600) + float(time_start_list[1]*60) + float(time_start_list[2])
	time_end_list = a[1].split(':')
	time_end = float(time_end_list[0]*3600) + float(time_end_list[1]*60) + float(time_end_list[2])
	time.append(time_start)
	time.append(time_end)
	if role == 'master':
		role.append(90)
		role.append(90)
	else:
		role.append(20)
		role.append(20)

a = time[0]

for i in range(len(role)):
	time[i] = time[i] - a

pf.close()
plt.plot(time, role)	
plt.plot(time, role)
plt.xlabel('Time')
plt.ylabel('Role')
plt.show()