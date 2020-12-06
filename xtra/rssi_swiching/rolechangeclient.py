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

    def _monitor(self): # receive decision from controller A
        count = 0
        host = "10.30.0.5" # set to IP address of server
        port = 12000
        addr = (host, port)
        buf = 1024
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        while True:
            (role_data, addr) = UDPSock.recvfrom(buf)
            roles = role_data.split()
            for item in roles:
                dp = self.datapaths[item]
                ofp = dp.ofproto
                self.gen_id = random.randint(0, 10000)
                self.send_role_request(dp, ofp.OFPCR_ROLE_MASTER, self.gen_id)

    def send_role_request(self, datapath, role, gen_id):
        ofp_parser = datapath.ofproto_parser
        print "send a role change request", datapath.id
        msg = ofp_parser.OFPRoleRequest(datapath, role, gen_id)
        datapath.send_msg(msg)
