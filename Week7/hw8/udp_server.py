from socket import *
from collections import defaultdict

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',70))
print("Server is running.....")


dic_msg = defaultdict(list)


while True:
   c,addr = s.recvfrom(1024)
   print("Connection from : " , addr)


   msg = c.decode()

   msg = msg.split(" ")

   if not msg:
      s.sendto("No Messages".encode(),addr)
      break

   elif msg[0] == "send":

      dic_msg[msg[1]].append(msg[2:])
      s.sendto("OK".encode(), addr)
      print(dic_msg)
   elif msg[0] == "quit":
      continue

   elif msg[0] == 'receive' :
      if len(dic_msg) == 0:
         s.sendto("No Messages".encode(),addr)
      else :
         s.sendto(str(dic_msg[msg[1][0]]).encode(),addr)
         del dic_msg[msg[1]][0]
         # print(dic_msg)
         break
         
