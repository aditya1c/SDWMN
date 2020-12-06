import socket
from socket import *
import time
host = ""
port = 12000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
while True:
	(pingdatafile, addr) = UDPSock.recvfrom(buf)
	print pingdatafile