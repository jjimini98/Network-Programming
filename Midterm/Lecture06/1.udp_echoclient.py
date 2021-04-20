from socket import *

sock = socket(AF_INET, SOCK_DGRAM)

while True:

   msg = input("input message : ")
   if msg == 'q': break 
   sock.sendto(msg.encode(), ('localhost', 9999))
   data , addr = sock.recvfrom(1024)
   print("server says : ", data.decode())
sock.close()
   