from socket import *  
import random
#1. request 메세지를 수신 -> recv(msg.decode())
#2. randint(0,40) / randint(0,100) / randing(70,150) 으로 randint 반환
#3. 나온 세개의 변수를 문자열로 묶어서 send(~.encode())
#4. if 사용자가 quit 메세지를 입력하면 - > sys.exit() or break

s = socket(AF_INET,SOCK_STREAM)
s.bind(('',80))
s.listen(5)

print("Device is running")

BUF_SIZE = 1024   

li = []
for _ in range(5):
   temp = random.randint(0,40)
   hum = random.randint(0,100)
   light = random.randint(70,150)
   li.append( "Temp="+str(temp) + ",Humid="+  str(hum)  + ",lilum=" + str(light) +" " )



while True:
   conn , addr = s.accept()
   print("accept : ",addr)
   msg = conn.recv(BUF_SIZE).decode() #User 로 부터 받은 메세지 Request 일수도 있고 quit 일수도 있음 

   if not msg:
      conn.close()
      continue 
   elif msg == "quit":
      conn.close()
      continue
   elif msg=="Request" :
      print('client : ', addr , msg)
      for x in li:
         conn.send(x.encode())

   conn.close()