#!/bin/bash
while true
do
	HOST="127.0.0.1"
	PORT=2006
	date| awk {'print $4'} | xargs echo >> topology.txt
	echo "/topo" | nc $HOST $PORT | tail -n +6 >> topology.txt
	echo ok >> topology.txt
	sleep 2s
done