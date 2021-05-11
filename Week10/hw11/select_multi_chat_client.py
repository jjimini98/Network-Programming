# 1. ID입력 
# 2. 메인 스레드는 사용자의 입력을 받아 서버로 전송
# 3. 서브 스레드는 채팅 서버로부터 메세지를 수신해 출력 


from socket import *
import time
import threading

port = 3000
BUFFSIZE = 1024


def recv(sock):
   while True:
      msg = sock.recv(BUFFSIZE)
      print(msg.decode())

sock= socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost',port))     

my_id = input("ID를 입력하세요 : ")
sock.send(('[' + my_id + ']').encode())


while True:
   msg = '[' + my_id + '] ' + input()
   sock.send(msg.encode())


   th = threading.Thread(target=recv , args=(sock,))
   th.start()