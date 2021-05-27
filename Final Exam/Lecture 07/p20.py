# # p.20 tcp_thread_chat_server

# from socket import *
# import threading

# port = 3333
# BUFSIZE = 1024

# def sendTask(sock):
#    while True:
#       resp = input()
#       print("보낸 메세지 : ", resp)
#       sock.send(resp.encode())

# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('',port))
# s.listen(2)
# conn , addr = s.accept()

# th = threading.Thread(target=sendTask, args=(conn,))
# th.start()

# while True:
#    data = conn.recv(BUFSIZE)
#    print("받은 메세지 : ", data.decode())



# p.20 tcp_thread_chat_server

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
      print("받은 메세지 : ", data.decode())


s = socket(AF_INET, SOCK_STREAM)
s.bind(('',port))
s.listen(2)
conn , addr = s.accept()

th1 = threading.Thread(target=sendTask, args=(conn,))
th1.start()

th2 = threading.Thread(target=recvTask, args=(conn,))
th2.start() 