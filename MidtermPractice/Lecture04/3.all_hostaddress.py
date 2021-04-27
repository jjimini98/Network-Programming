import ipaddress

net = ipaddress.ip_network("114.71.220.0/24")

for x in net.hosts():
	print(x) #0~254 