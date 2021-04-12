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
      mimeType = 'text/html'
      c.send("HTTP/1.1 200 OK \r\n".encode())
      c.send("Cotent-Type : ".encode()+ mimeType.encode() + '\r\n'.encode())
      c.send("\r\n".encode())

      with open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html", 'rb') as f:
         try:
            data = f.read(1024) #1024바이트 읽는다
            while data: #데이터가 없을 때까지
            
               data = f.read(1024) #1024바이트 읽음
               c.send(data)
         except Exception as ex:
            print(ex)

      # 사진 보내기 
      
      # url = 'http://127.0.0.1/index.html'
      # files = {'html':open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html","r", encoding= 'utf-8'), 'media': open('C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png', 'rb')}
      # requests.post(url, files=files)

      c.close()

   else: 
      c.send("Not Found".encode())
      c.close()










