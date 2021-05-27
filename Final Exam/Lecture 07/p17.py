# p.17 멀티스레드 에코 서버 = threading.Thread 클래스 사용

import threading
from socket import *

port = 9000
BUFSIZE = 1024

def echoTask(sock):
   while True:
      data = sock.recv(BUFSIZE)
      if not data:break
      print("Received Message : ", data.decode())
      sock.send(data)

   sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',port))
sock.listen(5)

while True:
   conn, (remotehost,remoteport) = sock.accept()
   print("connected by",remotehost)
   th = threading.Thread(target=echoTask, args=(conn,))
   th.start() 
