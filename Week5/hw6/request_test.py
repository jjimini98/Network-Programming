from socket import *

s = socket()
s.bind(('',80))
s.listen(10)

while True : 
   c, addr = s.accept()

   msg= c.recv(1024).decode()
   req = msg.split(" ")[1]


   myfile = "C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\index.html"    
 

   try:
      with open(myfile ,'rb') as file , open("C:\Users\jimin\vscode\network_programming\Week5\hw6\iot.png", "rb") as photo: # open file , r => read , b => byte format
         response = file.read()
         file.close()
 
      header = 'HTTP/1.1 200 OK\n'
 
      if(myfile.endswith(".jpg")):
            mimetype = 'image/jpg'
      elif(myfile.endswith(".css")):
            mimetype = 'text/css'
      else:
            mimetype = 'text/html'
 
      header += 'Content-Type: '+str(mimetype)+'\n\n'SSSSS
 
   except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
 
   final_response = header.encode('utf-8')
   final_response += response
   c.send(final_response)
   c.close()