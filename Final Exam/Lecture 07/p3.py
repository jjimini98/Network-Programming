# p.3

from socket import *

s = socket(AF_INET , SOCK_STREAM)
s.bind(('',9000))
s.listen(2)


while True: 
   client, addr = s.accept()
   print("Connected from" , addr)
   print("addr is " , addr[0])
   client.send(b"Hello "+ addr[0].encode())
   client.close() 