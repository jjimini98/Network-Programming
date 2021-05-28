from socket import * 
import time

clients= []
s = socket(AF_INET , SOCK_STREAM)
s.bind(('', 2500))
print("Server is Started")

while True:
   data, addr = s.recvfrom(1024)
   if 'quit' in data.decode():
      if addr in clients:
         print(addr , "exited")
         clients.remove(addr)
         continue

   
   if addr not in clients:
      print("new clients", addr)
      clients.append(addr)

   print(time.asctime() + str(addr) + ":" + data.decode())

   for client in clients:
      if client != addr : 
         s.sendto