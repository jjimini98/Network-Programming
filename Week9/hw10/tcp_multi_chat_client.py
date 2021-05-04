from socket import *
import threading

def handler(sock):
   while True: 
      msg = sock.recv(1024)
      print(msg.decode())
   


sock= socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost',2500))


my_id = input("ID를 입력하세요 : ")
sock.send(('[' + my_id + ']').encode())

th = threading.Thread(target=handler , args=(sock,))
th.daemon= True
th.start()

while True:
   msg = '[' + my_id + ']' + input()
   sock.send(msg.encode())


# from socket import *
# import threading
# import time 


# sock= socket(AF_INET, SOCK_STREAM)
# sock.connect(('localhost',2500))

# port = 3333
# BUFFSIZE = 1024

# my_id = input("ID를 입력하세요 : ")
# sock.send(('[' + my_id + ']').encode())

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



# while True:
#    msg = '[' + my_id + ']' + input()
#    sock.send(msg.encode())