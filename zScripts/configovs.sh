ovs-vsctl del-br br0
ovs-vsctl add-br br0 -- set Bridge br0 fail-mode=secure
ovs-vsctl set bridge br0 other-config:datapath-id=0000000000000003
ovs-vsctl add-port br0 wlan0
ifconfig wlan0 0
ifconfig br0 10.10.70.20 netmask 255.255.0.0
route add default gw 10.10.1.1 br0
ovs-vsctl set-controller br0 tcp:10.10.100.1:6633 tcp:10.10.100.5:6633
