# # p.21 tcp_thread_chat_client

# from socket import *
# import threading

# port = 3333 
# BUFSIZE = 1024

# def recvTask(sock):
#    while True:
#       data = sock.recv(BUFSIZE)
#       print("받은 메세지", data.decode())

# sock = socket(AF_INET, SOCK_STREAM)
# sock.connect(('localhost', port))

# th = threading.Thread(target=recvTask, args=(sock,))
# th.start()

# while True:
#    msg = input()
#    print("보낸 메세지 : ", msg)

#    sock.send(msg.encode())


# p.21 tcp_thread_chat_client

from socket import *
import threading

port = 3333 
BUFSIZE = 1024

def sendTask(sock):
   while True:
      resp = input()
      print("보낸 메세지 : ", resp)
      sock.send(resp.encode())

def recvTask(sock):
   while True:
      data = sock.recv(BUFSIZE)
      print("받은 메세지", data.decode())

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

th1 = threading.Thread(target=recvTask, args=(sock,))
th1.start()

th2 = threading.Thread(target=sendTask, args=(sock,))
th2.start() 