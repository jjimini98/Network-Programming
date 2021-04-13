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
      print(msg)     
#    req = msg.split(" ")[1]


#    try:
#       with open(myfile ,'rb') as file , open("C:\\Users\\jimin\\vscode\\network_programming\\Week5\\hw6\\iot.png", "rb") as photo: # open file , r => read , b => byte format
#          response = file.read()
#          file.close()
 
#       header = 'HTTP/1.1 200 OK\n'
    
#       if(myfile.endswith(".png")):
#             mimetype = 'image/png'
#       elif(myfile.endswith(".css")):
#             mimetype = 'text/css'
#       else:
#             mimetype = 'text/html'
 
#       header += 'Content-Type: '+str(mimetype)+'\n\n'

#    except Exception as e:
#       header = 'HTTP/1.1 404 Not Found\n\n'
#       response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
 
#    final_response = header.encode('utf-8')
#    final_response += response
#    c.send(final_response)
#    c.close()