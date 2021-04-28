import ipaddress

net = ipaddress.ip_network("114.71.220.0/24")
print(net) 

print(net.with_netmask)  # 114.71.220.0/255.255.255.0 (255.255.255.0 == 24) 

print(net.num_addresses) # 256
print(net.netmask) #IPv4Address('255,255,255,0')
print(net.hostmask) #IPv4Address('0.0.0.255')  netmask와 hostmask의 결과가 반대 