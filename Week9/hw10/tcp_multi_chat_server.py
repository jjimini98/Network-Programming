import time
from socket import *
import threading

client = []

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2500))
s.listen(10)

print("Server started")

def recvTask(sock): 
   while True : 
      conn, addr = s.accept()
      data = conn.recv(1024)
      
      if 'quit' in data.decode():
         if addr in client:
            print(addr, 'exited')
            client.remove(addr)
            continue
         
      if addr not in client:
         print("new client", addr)
         client.append(addr)
      
      print(time.asctime() + str(addr) + ":" + data.decode())

   for c in client:
      if c !=addr:
         conn.send(data)

th1 = threading.Thread(target=recvTask, args=(sock,))
th1.start()


# from socket import *
# import threading
# import time

# port = 3333
# BUFFSIZE = 1024
# client = []

# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('',port))
# s.listen(1)

# print("Server started")

# def sendTask(sock):
#    while True:
#       data = input()
#       print(time.asctime() + str(addr) + ":" + data.decode())
   
# def recvTask(sock):
#    while True:
#       data = sock.recv(BUFFSIZE)
#       print(time.asctime() + str(addr) + ":" + data.decode())


# th1 = threading.Thread(target=sendTask, args=(sock,))
# th2 = threading.Thread(target=recvTask, args=(sock,))

# th1.start()
# th2.start()


# while True : 
#    conn, addr = s.accept()
#    data = conn.recv(1024)
#    if 'quit' in data.decode():
#       if addr in client:
#          print(addr, 'exited')
#          client.remove(addr)
#          continue
   
#    if addr not in client:
#       print("new client", addr)
#       client.append(addr)
   
#    print(time.asctime() + str(addr) + ":" + data.decode())

#    for c in client:
#       if c !=addr:
#          conn.send(data)

