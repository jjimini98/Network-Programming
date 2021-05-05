#1. 서브 스레드 1 = 모든  클라이언트에게 메세지를 전송
#2. 메인 스레드 = 새로운 클라이언트면 목록에 추가하고 quit 입력하면 remove 
#3. 새로운 클라이언트가 들어왔을 때 계속 연결할 수 있어야함. 


from socket import *
import time
import threading 

port = 3333
BUFFSIZE = 1024

print("Server is started ")

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',port))
sock.listen(10)

clients = []


def Task(sock) :
   conn, addr = sock.accept()
   while True:
      data = conn.recv(BUFFSIZE)

      if 'quit' in data.decode():
            if conn in clients:
               print(addr, 'exited')
               clients.remove(conn)
               continue
         
      if conn not in clients:
         print("new client", addr)
         clients.append(conn)


      for client in clients:
         if client !=conn:
            client.send(data)





         # elif client != addr:
         #    sock.send(data)
         #    print("done")


      print(time.asctime() + str(addr) + ": " + data.decode())



while True:
   

   th1 = threading.Thread(target=Task , args=(sock,))

   th1.start()
   