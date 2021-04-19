from socket import * 

user = input("메세지를 입력하세요 : ")

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('localhost',70))

while True:
   if user == 'quit':
      s.send(user.encode())
      break 
   s.send(user.encode())

   if "receive" in user:
      s.send(user.encode())
      s.recv(1024).decode()
   
   if "send" in user:
      s.recv(1024).decode()

s.close()  
