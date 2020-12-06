ifconfig wlan0 down
echo "Enter channel you want to start open_mesh in:"
read channel
iwconfig wlan0 mode ad-hoc essid open_mesh freq $channel
ifconfig wlan0 10.10.70.20 netmask 255.255.0.0 up
