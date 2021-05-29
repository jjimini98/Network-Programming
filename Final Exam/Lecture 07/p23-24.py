# UDP로 다중채팅프로그램 만들기 server version 

from socket import * 
import time

clients= []
s = socket(AF_INET , SOCK_DGRAM)
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
         s.sendto(data,client)