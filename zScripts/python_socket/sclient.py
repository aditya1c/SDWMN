import socket
from socket import *
import time
host = "127.0.0.1" # set to IP address of target computer
port = 12000
addr = (host, port)
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
	pingdatafile = 'hi'
	UDPSock.sendto(pingdatafile, addr)
	time.sleep(1)