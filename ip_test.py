import ipaddress
import pprint

address = ipaddress.IPv4Network('172.24.9.1/26', strict=False)

print(address.network_address)
print(address.broadcast_address)
print("-----")
print(address.network_address + 1)
print(address.broadcast_address - 1)
