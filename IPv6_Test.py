from __future__ import unicode_literals
import ipaddress

address = u'2620:10d:c091:152:0:0:0:5'
network = u'2620:10d:c091:150::/60'
answer = ipaddress.ip_address(address) in ipaddress.ip_network(network, False)
print "IP: {}".format(ipaddress.ip_address(address))
print "Network: {}".format(ipaddress.ip_network(network, False))
print "Network Address: {}".format(ipaddress.ip_network(network, False).network_address)
print "Broadcast Address: {}".format(ipaddress.ip_network(network, False).broadcast_address)
print answer
