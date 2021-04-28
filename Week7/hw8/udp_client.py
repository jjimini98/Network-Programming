from socket import * 
while True:
   user = input("메세지를 입력하세요 : ")

   s = socket(AF_INET, SOCK_DGRAM)
   s.connect(('localhost',70))

   if user == 'quit':
      s.send(user.encode())
      continue
   s.send(user.encode())

   if "receive" in user:
      s.send(user.encode())

      l = s.recv(1024).decode()
      text = ''
      for x in l[1:]:
         if x == "[" or x == "]" or x == "'" or x== ","  : continue
         text += x
      print(text)
   if "send" in user:
     print(s.recv(1024).decode())

   # s.close()
