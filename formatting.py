#!/usr/bin/env python

import re

cluster_members = []
vip_members = []

node = {
    "role_name": "remote-access-vpn-controller",
    "name": "prn1-cmdf-ra-vpn1"
}

if re.search("^(htl)?remote-access-vpn-controller$", node['role_name']):
    pfx = node['name'][:3]
    if re.search("prn|frc|nrt", pfx):
        for idx in range(1, 5):
            hostname = pfx + "vpn" + str(idx).zfill(2)
            print("Hostname: " + hostname)
            cluster_members.append(hostname + ".corp.tfbnw.net")
            vip_members.append(hostname + ".thefacebook.com")


print(cluster_members)
print(vip_members)
