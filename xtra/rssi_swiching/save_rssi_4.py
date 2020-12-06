# Start
import time

mac = '00:0b:6b:02:0d:13'
ctrlmac = '00:0b:6b:02:0d:55' # add controller mac id

rssi_list = []
rssi_state_list = []

fr_rssi = open('rssi.txt','r') # open rssi.txt means all rssi data of all
fw_total = open('total_rssi_4','a')

for line in fr_rssi:
	a = line.split(' ')
	if (a[1] == mac):
		rrsi_pos_value = ((-1)*float(a[3]))
		rssi_list.append(rrsi_pos_value)
		
		fw_total.write(a[0] + ' ' + a[3])

fr_rssi.close() # close rssi.txt
fw_total.close()

fr2_rssi = open('rssi.txt','r')
lines = fr2_rssi.read().split('\n')
timestart = lines[0].split()[0]
timeend = lines[-1].split()[0]
fr2_rssi.close()

fr_count = open('rssi_count_4.txt','r')
line = fr_count.read().split()
prev_trans1 = int(line[0])
prev_trans2 = int(line[1])
trans_121 = int(line[2])
trans_123 = int(line[3])
trans_321 = int(line[4])
trans_323 = int(line[5])
trans_12 = int(line[6])
trans_21 = int(line[7])
trans_23 = int(line[8])
trans_32 = int(line[9])
prev_state = int(line[10])
fr_count.close()

thr1_left = 25 #30 #45 25
thr1_right = 45 #50 #55 45
thr2_left = 55 #60 #65 55
thr2_right = 65 #70 #70 70
thr3_left = 75 #80 #80 80
thr3_right = 100 #100 #90 100

#Alloting States to RSSI Values
for rssi in rssi_list:
	if rssi <= thr1_right:
		rssi_state_list.append(1)
		prev_state = 1
	if (rssi >= thr2_left and rssi <= thr2_right):
		rssi_state_list.append(2)
		prev_state = 2
	if rssi >= thr3_left:
		rssi_state_list.append(3)
		prev_state = 3
	if (rssi > thr1_right and rssi < thr2_left):
		if prev_state == 1:
			rssi_state_list.append(1)
			prev_state = 1
		elif prev_state == 2:
			rssi_state_list.append(2)
			prev_state = 2
		else:
			rssi_state_list.append(1)
			prev_state = 1
	if (rssi > thr2_right and rssi < thr3_left):
		if prev_state == 3:
			rssi_state_list.append(3)
			prev_state = 3
		elif prev_state == 2:
			rssi_state_list.append(2)
			prev_state = 2
		else:
			rssi_state_list.append(3)
			prev_state = 3

#Count Transitions and make decision
for count in range(len(rssi_state_list)):

	if rssi_state_list[count] == 1:
		if prev_trans1 == 2:
			prev_trans1 = 1
			trans_21 += 1
			if prev_trans2 == 12:
				prev_trans2 = 21
				trans_121 += 1 # 121
			if prev_trans2 == 32:
				prev_trans2 = 21
				trans_321 += 1 # 321
		elif prev_trans1 == 3:
			prev_trans1 = 1
		else:
			prev_trans1 = 1
		role = 'master'

	if rssi_state_list[count] == 2:
		if prev_trans1 == 1:
			prev_trans1 = 2
			prev_trans2 = 12
			trans_12 += 1
			if trans_121 >= trans_123:
				role = 'master'
			else:
				role = 'slave'
		elif prev_trans1 == 3:
			prev_trans1 = 2
			prev_trans2 = 32
			trans_32 += 1
			if trans_321 >= trans_323:
				role = 'master'
			else:
				role = 'slave'
		elif prev_trans1 == 2:
			prev_trans1 = 2
		else:
			prev_trans1 = 2
			role = 'master'

	if rssi_state_list[count] == 3:
		if prev_trans1 == 2:
			prev_trans1 = 3
			trans_23 += 1
			if prev_trans2 == 12:
				prev_trans2 = 23
				trans_123 += 1 # 123
			if prev_trans2 == 32:
				prev_trans2 = 23
				trans_323 += 1 # 321
		elif prev_trans1 == 1:
			prev_trans1 = 3
		else:
			prev_trans1 = 3
		role = 'slave' 

# Write Role Data to file with time start and end of capture
fw_role = open('total_role_4.txt','a')
fw_role.write(timestart + ' ' + timeend + ' ' + role + '\n')
fw_role.close()

# Write transitions happened till now
fw_count = open('rssi_count_4','w')
fw_count.write(str(prev_trans1) + ' ' + str(prev_trans2) + ' ' + str(trans_121) + ' ' + str(trans_123) + ' ' + str(trans_321) + ' ' + str(trans_323) + ' ' + str(trans_12) + ' ' + str(trans_21) + ' ' + str(trans_23) + ' ' + str(trans_32) + ' ' + str(prev_state))
fw_count.close()