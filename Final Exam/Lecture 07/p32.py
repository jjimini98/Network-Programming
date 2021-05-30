# tcp_threaded_shared_number_server.py with lock 

from socket import *
import threading

port = 2500
BUFSIZE = 1024

sharedData = 0 

def handler(sock):
   global sharedData , lock 
   lock.acquire() 
   for _ in range(10000000):
      sharedData+=1
   lock.release() 
   print(sharedData)
   sock.send(str(sharedData).encode())
   sock.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('',port))
s.listen(5)
lock = threading.Lock() 

while True:
   client, addr = s.accept()
   print("Connected by {}".format(addr))

   th = threading.Thread(target = handler, args = (client,))
   th.start()
