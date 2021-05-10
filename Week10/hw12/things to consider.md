1. 서버 

- 스레드 말고 select로 
- 접속한 사람들의 ip를 리스트로 + 새로운 클라이언트가 들어오면 리스트에 append 
- 메세지 수신 recv  : 맨처음에 받는 recv는 id임  그다음 받는 메세지는 실제 id에서 보낸 메세지  (  if 메세지가 "quit" 면 해당 클라이언트 목록에서 삭제  , if 메세지 보낸 사람을 제외하고 나머지에게 send)   
+) 얜 select에서 read만 하면 되나? 






2. 클라이언트
- 스레드말고 select로 
- 메인 스레드 : 일단 사용자로부터 id를 input -> 받은 id를 서버에게 send
- 서브스레드에서는 서버로부터 메세지를 수신해 화면에 출력 (이부분을 select로 구현) 






3. select
- 여러개의 소켓에 대해 비동기 I/O 지원

```python 
r_sock, w_sock, e_sock  = select.select(rlist, wlist, xlist[,timeout])
```

- 에코서버의 경우
1) 서버의 소켓 생성 : 일단 클라이언트의 연결을 기다리는 소켓
2) 1)에서 만든 서버 소켓을 읽기 가능한 소켓 리스트에 append 
3) 클라이언트의 연결이 들어오면 select함수 return 
4) 해당 클라이언트의 소켓을 읽기 가능한 소켓리스트에 추가 + select 함수 호출
5) 새로운 클라이언트의 요청이 있거나 기존 클라이언트의 요청이 들엉면 select 함수가 반환됨 


``` python
import socket, select

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket() # default TCP socket
s_sock.bind(('',PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT)+"에서 접속 대기중")  #서버 소켓을 소켓 리스트에 저장 

while True : 
   r_sock , w_sock, e_sock = select.select(socks, [] , [] )

   for s in r_sock : 
      if s== s_sock:
         c_sock, addr = s_sock.accept()
         socks.append(c_sock)
         print("Client ({}) connected".format(addr))
      
      else:
         data = s.recv(BUFFER)
         if not data :
            s.close()
            socks.remove(s) #연결이 종료된 소켓을 지워버리기 
            continue
         
         print("Received : ", data.decode())

         s.send(data)

 ``` 



