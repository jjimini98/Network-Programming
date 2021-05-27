# p.18 thread_class_echo_server

from socket import *
import threading

port = 9000
BUFSIZE = 1024

class ClientThread(threading.Thread):
   def __init__(self,sock):
      threading.Thread.__init__(self)
      self.sock = sock
   
   def run(self):
      while True:
         data = self.sock.recv(BUFSIZE)
         if not data : break
         print("Received Message : %s" %data.decode())
         self.sock.send(data)
      
      self.sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost',port))
sock.listen(5)

while True: 
   conn, (remotehost, remoteport ) = sock.accept()
   print("Connected by : ", remotehost, remoteport)
   th = ClientThread(conn)
   th.start()