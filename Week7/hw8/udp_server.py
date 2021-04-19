from socket import *
from collections import deque

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',70))
print("Server is running.....")

dic_msg = {}   
deq = deque()

while True:
   c,addr = s.recvfrom(1024)
   msg = c.decode()
   msg = msg.split(" ")    


   
   if not msg:
      s.sendto("No Messages".encode(),addr)
      break 

   elif msg[0] == "send":
      dic_msg[msg[1]]= deq
      deq.append(msg[2])
      s.sendto("OK".encode(),addr)

   elif msg[0] == "quit":
      break 

   elif "receive" in msg[0] : 
      if len(deq) == 0:
         s.sendto("No Messages".encode(),addr)
      else : 
         s.sendto(str(deq[0]).encode(),addr)
         deq.popleft()
   
s.close()