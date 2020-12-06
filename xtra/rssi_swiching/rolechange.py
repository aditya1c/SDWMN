from operator import attrgetter # all check
import sys
import time
import random
import time
from socket import *
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import DEAD_DISPATCHER
from ryu.controller.handler import HANDSHAKE_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.app import oldsimple_switch_13
from ryu.controller import dpset
from ryu.lib import hub #imported check

class rolechanger(oldsimple_switch_13.SimpleSwitch13):

	def __init__(self, *args, **kwargs):
		super(rolechanger, self).__init__(*args, **kwargs)
		#self.role_string_list = ['nochange', 'equal', 'master', 'slave', 'unknown']
		self.datapaths = {}
		self.monitor_thread = hub.spawn(self._filemonitor) # creating threads


	@set_ev_cls(ofp_event.EventOFPStateChange,[MAIN_DISPATCHER, DEAD_DISPATCHER])
	def _state_change_handler(self, ev):
		datapath = ev.datapath
		if ev.state == MAIN_DISPATCHER:
			if not datapath.id in self.datapaths:
                                self.datapaths[datapath.id] = datapath
                                print "*************"
                                print datapath.id, "Entered"
                                print "*************"
		elif ev.state == DEAD_DISPATCHER:
			if datapath.id in self.datapaths:
                                del self.datapaths[datapath.id]
                                print "*************"
                                print datapath.id, "Left"
                                print "*************"

	def _filemonitor(self):
		host = ""
		port = 12000
		buf = 1024
		addr = (host, port)
		UDPSock = socket(AF_INET, SOCK_DGRAM)
		UDPSock.bind(addr)
		while True:
			for item in self.datapaths:
				file_name = total_role_ + item + .txt
				fr_role = open(file_name, 'r')
				role = (fr_role.read().split('\n'))[-1].split()[1]
				fr_role.close()
				dp = self.datapaths[item]
				ofp = dp.ofproto
				self.gen_id = random.randint(0, 10000)
				if role = 'master':
					self.send_role_request(dp, ofp.OFPCR_ROLE_MASTER, self.gen_id)
				else:
					role_data = item + ''
			if role_data != NULL:
                                UDPSock.sendto(role_data[:-1], addr)
			hub.sleep(4)

	def send_role_request(self, datapath, role, gen_id):
		ofp_parser = datapath.ofproto_parser
		print "send a role change request", datapath.id
		msg = ofp_parser.OFPRoleRequest(datapath, role, gen_id)
		datapath.send_msg(msg) #role request check
