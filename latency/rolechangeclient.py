from operator import attrgetter
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
from ryu.app import simple_switch_13
from ryu.controller import dpset
from ryu.lib import hub

class rolechanger(simple_switch_13.SimpleSwitch13):

    def __init__(self, *args, **kwargs):
        super(rolechanger, self).__init__(*args, **kwargs)
        #self.role_string_list = ['nochange', 'equal', 'master', 'slave', 'unknown']
        self.datapaths = {}
        self.monitor_thread = hub.spawn(self._monitor) # creating threads
        self.monitor_thread = hub.spawn(self._echomonitor)
        self.monitor_thread = hub.spawn(self._connmonitor)
        self.sendflag = {}
        self.gen_id = 0
        self.senttime = {}
        self.receivedtime = {}
        self.tooktime = {} # initialize
        self.timetaken = 0
        self.ping_self_data = {}
        self.ping_data = {} # initialize
        self.prevdecdic = {}
        self.decdic = {}
        self.decisionsend = {}
        self.decision = ''
        self.prevdecdic[48] = '' # add all switches and initialize

    @set_ev_cls(ofp_event.EventOFPStateChange,[MAIN_DISPATCHER, DEAD_DISPATCHER])
    def _state_change_handler(self, ev):
        datapath = ev.datapath
        if ev.state == MAIN_DISPATCHER:
            if not datapath.id in self.datapaths:
                                self.datapaths[datapath.id] = datapath
        elif ev.state == DEAD_DISPATCHER:
            if datapath.id in self.datapaths:
                                del self.datapaths[datapath.id]

        def _monitor(self): # receive decision from controller A
            count = 0
            host = "127.0.0.1" # set to IP address of target computer
            port = 12000
            addr = (host, port)
            buf = 1024
            UDPSock = socket(AF_INET, SOCK_DGRAM)
            while True:
                (decisiondata, addr) = UDPSock.recvfrom(buf)
                decision[decisiondata.split()[0]] = decisiondata.split()[1]

        def _echomonitor(self):
            while True:
                for item in self.datapaths:
                    try:
                        self.send_echo_request(self.datapaths[item])
                        print "********Echo Request Sent********"
                    except:
                        print "****Exception****"
                    hub.sleep(5)

        def _connmonitor(self): # send pingdata to controller A
            host = "127.0.0.1" # set to IP address of target computer
            port = 13000
            addr = (host, port)
            buf = 1024
            UDPSock = socket(AF_INET, SOCK_DGRAM)
            while True:
                for item in self.sendflag:
                    if self.sendflag[item] == 1:
                        pingdatafile = str(item) + " " + self.tooktime[item] + " "
                    pingdatafile = pingdatafile[:-1]
                    UDPSock.sendto(pingdatafile, addr)

        def send_role_request(self, datapath, role, gen_id):
                ofp_parser = datapath.ofproto_parser
                print "send a role change request"
                msg = ofp_parser.OFPRoleRequest(datapath, role, gen_id)
                datapath.send_msg(msg)


        def send_echo_request(self, datapath):
                data = '1234'
                ofp = datapath.ofproto
                ofp_parser = datapath.ofproto_parser
                req = ofp_parser.OFPEchoRequest(datapath, data)
                self.senttime[datapath.id] = time.time()
                datapath.send_msg(req)

        @set_ev_cls(ofp_event.EventOFPEchoReply,[HANDSHAKE_DISPATCHER, CONFIG_DISPATCHER, MAIN_DISPATCHER])
        def echo_reply_handler(self, ev):
                msg = ev.msg
                datapath = msg.datapath
                self.receivedtime[datapath.id] = time.time()
                self.timetaken = (self.receivedtime[datapath.id] - self.senttime[datapath.id])*1000
                print "********Received********"
                print self.tooktime[datapath.id] = str(self.senttime[datapath.id]) + " " + str(self.timetaken)
                