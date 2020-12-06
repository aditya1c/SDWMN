while true;do
sudo tcpdump -i wlan0 -w wlan0.dump &
pid=$!
sleep 5s
sudo kill $pid
tshark -i -<wlan0.dump -t e -T fields -E separator=/s -e frame.time -e wlan.sa -e wlan.da -e radiotap.dbm_antsignal>wlan0.txt
python rssi.py
# python save_rssi_1.py
# python save_rssi_2.py
# python save_rssi_3.py
python save_rssi_4.py
done