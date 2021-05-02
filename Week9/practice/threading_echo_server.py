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
sock.bind(('', port))
sock.listen(5)

while True:
   conn, (remotehost, remoteport) = sock.accept()
   print("Connected by :" , remotehost, remoteport)
   th  = threading.Thread(target=echo_task, args= (conn,))
   th.start()