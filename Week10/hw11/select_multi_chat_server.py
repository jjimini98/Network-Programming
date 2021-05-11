from socket import *
import select

#연결되는 소켓을 담을 리스트 
s_list = []

BUFFER = 1024
PORT = 3000 

s_sock = socket()
s_sock.bind(('', PORT))
s_sock.listen(10)

s_list.append(s_sock)
print(str(PORT) + " 에서 접속 대기중")

while True: 

   r_sock , w_sock, e_sock = select.select(s_list, [], [])
   for s in r_sock:
      print("r_sock is", r_sock)
      print("s_sock is" , s_sock) 
      if s== s_sock:
         c_sock, addr = s_sock.accept()
         print("c_sock is", c_sock)
         s_list.append(c_sock)
         print("Client {} connected".format(addr))
   
      elif s != s_sock:      
         data = s.recv(BUFFER)
         if data.decode() == "quit" :
            s.close()
            s_list.remove(s)
            continue
         
         print("send complete")
         print("Received : ", data.decode())
         if s != c_sock:
            s.send(data)

