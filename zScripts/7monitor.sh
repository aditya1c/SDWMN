#!/bin/sh
echo "Set date in router"
cd /home/vamsi/
mkdir chan
cd /home/vamsi/chan
iwconfig wlan0 chan 1
tcpdump -i wlan0 -C 100 -w data.pcap &
date >> log.txt
rawname=data.pcap
prevname=data.pcap
nowname=data.pcap1
count=2
if [ -f $nowname ];
	then
		date >> log.txt
		mv $prevname procdata.pcap
		echo "Operation on procdata.pcap file"
		rm procdata.pcap
		prevname=$nowname
		nowname=$rawname
		nowname+=$count
		count='expr $count + 1'
	else
		sleep 10s
fi