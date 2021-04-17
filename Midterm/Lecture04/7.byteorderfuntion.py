import socket

a = 1234
print(hex(a))

b = socket.htons(a)
print(hex(b))

c = socket.ntohs(b)
print(hex(c))
