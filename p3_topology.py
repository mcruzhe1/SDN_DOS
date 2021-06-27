#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
# Marco: Add RemoteController to allow use of POX instance as controller
from mininet.node import Controller, RemoteController
from mininet.log import info, setLogLevel
from mininet.topo import Topo

setLogLevel('info')

class Quad(Topo):
    def build(self):
        info('*** Adding docker containers\n')
        # Marco: Add contrainers with 192.168.2.X0 IP addresses
        d1 = self.addHost('h1', ip='192.168.2.10', dimage="ubuntu:trusty", mac="00:00:00:00:00:01")
        d2 = self.addHost('h2', ip='192.168.2.20', dimage="ubuntu:trusty", mac="00:00:00:00:00:02")
        d3 = self.addHost('h3', ip='192.168.2.30', dimage="ubuntu:trusty", mac="00:00:00:00:00:03")
        d4 = self.addHost('h4', ip='192.168.2.40', dimage="ubuntu:trusty", mac="00:00:00:00:00:04")
        info('*** Adding switch\n')
        # Marco: single switch
        s1 = self.addSwitch('s1')
        info('*** Creating links\n')
        # Marco: connect all hosts to the switch
        self.addLink(d1, s1)
        self.addLink(d2, s1)
        self.addLink(d3, s1)
        self.addLink(d4, s1)

topos = {"quad": (lambda: Quad())}
