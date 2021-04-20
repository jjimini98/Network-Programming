import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('',9999))

while True:
   msg, addr = socket.recvfrom(1024)
   print("Connection : ", addr)

   socket.sendto(msg, addr) 


   