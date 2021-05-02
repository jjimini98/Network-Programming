import time
from socket import *

client = []

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 2500))

print("Server started")

while True : 
   data , addr = s.recvfrom(1024)
   if 'quit' in data.decode():
      if addr in client:
         print(addr, 'exited')
         client.remove(addr)
         continue
   
   if addr not in client:
      print("new client", addr)
      client.append(addr)
   
   print(time.asctime() + str(addr) + ":" + data.decode())

   for c in client:
      if c !=addr:
         s.sendto(data, client)

   