from socket import *

s = socket()
s.bind(('',80))
s.listen(10)
print("Server is running ......")

while True : 
   c, addr = s.accept()
   print("Connection from : " , addr)

   while True:
      msg= c.recv(2000).decode()
      req = msg.split("\r\n")
      request = req[0].split(" ")
      route = request[1]
      route = route[1:]
      print("client wants ", route)


      try:
         if route == "index.html":
            f = open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html",'r',encoding='utf-8')
            # f = open("index.html",'r',encoding= 'utf-8')
            mimeType = 'text/html'
      
         elif route == 'iot.png':
            f = open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png",'rb')
            mimeType = 'image/png'
         
         elif route == 'favicon.ico':
            f = open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\favicon.ico",'rb')
            mimeType = 'image/x-icon'
         
         data = f.read()
         c.send(data)

         c.send(b'HTTP/1.1 200 OK\r\n')
         c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
         c.send(b'\r\n')
         data = f.read() # index.html 파일을 읽는다
         # c.send(data.encode('euc-kr'))
         # c.send(data)

         if route == 'index.html':
         
            c.send(data.encode('euc-kr'))
            # c.send(data.encode('utf-8'))  # 혹은 c.send(data.encode())
            #c.send(data.encode('euc-kr')) # ???????????
         else:
            data= f.read()
            c.send(data)
         print(route, 'send success!!')


      except Exception as e:
         header = 'HTTP/1.1 404 Not Found\n\n'
         response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
