from socket import *  
import random

t = socket(AF_INET,SOCK_STREAM)
t.bind(('',81))
t.listen(5)

print("Device2 is running")

BUF_SIZE = 1024   

st = ''
for _ in range(5):
   hb = random.randint(40,140)
   step = random.randint(2000,6000)
   cal = random.randint(1000,4000)
   st += "Heartbeat="+str(hb) + ",Steps="+  str(step)  + ",Cal=" + str(cal) +" " 


while True:
   conn , addr = t.accept()
   print("accept : ",addr)
   msg = conn.recv(BUF_SIZE).decode() #User 로 부터 받은 메세지 Request 일수도 있고 quit 일수도 있음 

   if not msg:
      conn.close()
      continue 
   elif msg == "quit":
      print('client : ', addr)
      print("client : " , msg)
      print("client : completed")
      conn.close()
      continue
   elif msg=="Request" :
      print('client : ', addr)
      print("client : ", msg)
      print("client : completed")

      conn.send(st.encode())

   conn.close()