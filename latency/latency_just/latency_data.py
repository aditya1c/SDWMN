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
		self.monitor_thread = hub.spawn(self._echomonitor)
		self.senttime = {}
		self.receivedtime = {} # initialized in state change handler
		self.tooktime = {}

	@set_ev_cls(ofp_event.EventOFPStateChange,[MAIN_DISPATCHER, DEAD_DISPATCHER])
	def _state_change_handler(self, ev):
		datapath = ev.datapath
		if ev.state == MAIN_DISPATCHER:
			if not datapath.id in self.datapaths:
                                self.datapaths[datapath.id] = datapath
                                print "************************"
                                print datapath.id , "Entered"
                                print "************************"
		elif ev.state == DEAD_DISPATCHER:
			if datapath.id in self.datapaths:
                                del self.datapaths[datapath.id]
                                print "************************"
                                print datapath.id , "Left"
                                print "************************"

        def _echomonitor(self):
                while True:
                        for item in self.datapaths:
                                try:
                                        self.send_echo_request(self.datapaths[item])
                                        print "********Echo Request Sent to ********", item
                                except:
                                        print "****Exception to ****", item
                        hub.sleep(5) # echo check

        def send_echo_request(self, datapath):
                data = '1234'
                ofp = datapath.ofproto
                ofp_parser = datapath.ofproto_parser
                req = ofp_parser.OFPEchoRequest(datapath, data)
                self.senttime[datapath.id] = time.time()
                datapath.send_msg(req) # echo request check

        @set_ev_cls(ofp_event.EventOFPEchoReply,[HANDSHAKE_DISPATCHER, CONFIG_DISPATCHER, MAIN_DISPATCHER])
        def echo_reply_handler(self, ev):
                msg = ev.msg
                datapath = msg.datapath
                self.receivedtime[datapath.id] = time.time()
                self.tooktime[datapath.id] = (self.receivedtime[datapath.id] - self.senttime[datapath.id])
                print "********Received from ********", datapath.id
                fw_data = open(str(datapath.id),'a')
                fw_data.write('%16.6f' % self.senttime[datapath.id])
                fw_data.write(':')
                fw_data.write('%7.6f' % self.tooktime[datapath.id])
                fw_data.write('\n')
                fw_data.close()