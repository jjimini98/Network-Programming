from socket import *
import threading

port = 2500
BUFSIZE = 1024

def echo_task(sock):
   while True:
      data= sock.recv(BUFSIZE)
      if not data : break 
      print("Received Message : " , data.decode())
      sock.send(data)

   sock.close()




sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost',port))

while True:
   msg = input()
   print("->", msg)
   sock.send(msg.encode)