#!/usr/bin/env python3

var = '192.168.1.1,2620:10d:c081:ffff::0'
ip_adds = var.split(',')

print(len(ip_adds))

var = '192.168.1.1'
ip_adds = var.split(',')

print(ip_adds[0])
