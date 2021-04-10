from socket import * 
import requests

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
   c , addr = s.accept()

   data= c.recv(1024)
   msg = data.decode()
   req = msg.split('\r\n')[0][4:15]


   if req == "/index.html" :
      # f = open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html", 'r', encoding= 'utf-8')
      # mimeType = 'text/html'
      # c.send("HTTP/1.1 200 OK \r\n".encode())
      # c.send("Cotent-Type : ".encode()+ mimeType.encode() + '\r\n'.encode())
      # c.send("\r\n".encode())
      # data = f.read()
      

      # # 그냥 텍스트로 보내지말고 html 파일로 보내야함.

      # c.send(data.encode())
      

      # 사진 보내기 
      
      # url = 'http://127.0.0.1/index.html'
      # files = {'html':open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html","r", encoding= 'utf-8'), 'media': open('C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png', 'rb')}
      # requests.post(url, files=files)

      c.close()

   else: 
      c.send("Not Found".encode())
      c.close()












   #  p = open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png",'rb')
   #    mimeType ='image/png'
   #    c.send("HTTP/1.1 200 OK \r\n".encode())
   #    c.send("Cotent-Type : ".encode()+ mimeType.encode() + '\r\n'.encode())
   #    c.send("\r\n".encode())

   #    picture = p.read(1024)
   #    while (picture):
   #       c.send(picture)
   #       picture = p.read(1024)
   #    p.close()
