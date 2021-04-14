import ipaddress

net = ipaddress.ip_network('114.71.220.0/24')
addr = ipaddress.ip_address("114.71.220.95")

print(addr in net)

addr = ipaddress.ip_address('192.168.0.1')
print(addr in net)
