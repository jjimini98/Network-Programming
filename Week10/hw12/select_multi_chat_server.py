from socket import *
import select

#연결되는 소켓을 담을 리스트 
s_list = []

BUFFER = 1024
PORT = 3333

s_sock = socket()
s_sock.bind(('', PORT))
s_sock.listen(10)

s_list.apend(s_sock)
print(str(PORT) + " 에서 접속 대기중")

while True: 

   r_sock , w_sock, e_sock = select.select(s_list, [], [])
   
   for s in s_list:
      if s== s_sock:
         c_sock, addr = s_sock.accept()
         s_list.append(c_sock)
         print("Client ({}) connected".format(addr))
         

   