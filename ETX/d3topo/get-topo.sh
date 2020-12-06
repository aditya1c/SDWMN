#!/bin/bash
while true
do
	HOST="127.0.0.1"
	PORT=2006
	echo "/topo" | nc $HOST $PORT | tail -n +6 > topo.txt
	python cut.py
	date| awk {'print $4'} | xargs echo -n >> ett1.txt
	date| awk {'print $4'} | xargs echo -n >> ett2.txt
	date| awk {'print $4'} | xargs echo -n >> ett3.txt
	echo -n ' ' >> ett1.txt
	echo -n ' ' >> ett2.txt
	echo -n ' ' >> ett3.txt
	less topo.txt | grep 10.10.50.20 | awk {'print $5'} | xargs echo -n >> ett1.txt
	less topo.txt | grep 10.10.30.20 | awk {'print $5'} | xargs echo -n >> ett2.txt
	less topo.txt | grep 10.10.80.20 | awk {'print $5'} | xargs echo -n >> ett3.txt
	echo ok >> ett1.txt
	echo ok >> ett2.txt
	echo ok >> ett3.txt
	sleep 1s
done