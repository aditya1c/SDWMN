import socket
import glob
import os
import sys
buf = 512
SERVER_IP = "10.30.0.5"
SERVER_UDP_PORT = 9001
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_udp.bind(("", SERVER_UDP_PORT))
message = str(1) + ' ' + 'Handoverinitiation'
s_udp.sendto(message, (SERVER_IP, SERVER_UDP_PORT))
decisiondata, (SERVER_IP, SERVER_UDP_PORT) = s_udp.recvfrom(buf)
print decisiondata
s_udp.close()