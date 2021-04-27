import ipaddress 

addr4 = ipaddress.ip_address('192.0.0.1')
print(addr4)

addr6 = ipaddress.ip_address("2001:A8::1")
print(addr6)

print(addr4.version) #4 ipv4라는 의미 
print(addr6.version) #6 ipv6라는 의미 