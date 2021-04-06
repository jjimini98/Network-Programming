from socket import * 
import struct


def calculator(sentence):
   sentence = sentence.split(" ") 

   if sentence[1] == "+":
      return int(sentence[0]) + int(sentence[2])  
   
   elif sentence[1] == "-":
      return int(sentence[0]) - int(sentence[2])
   
   elif sentence[1] == "*":
      return int(sentence[0]) * int(sentence[2])

   elif sentence[1] == "/":
      return '%0.1f' %float(float(sentence[0])/float(sentence[2]))
   


s = socket(AF_INET , SOCK_STREAM)
s.bind(('',3331))
s.listen(5)

print("waiting....")

while True:
   client,addr = s.accept()
   print("Connection from : ", addr)
   
   while True : 
      data = client.recv(1024)
      if not data : break 
      try: 
         result = calculator(data.decode())
      except: 
         client.send(b"Try Again")
      
      else : 
         if type(result) == int:
            # en = (result).to_bytes(4,'big')
            # client.send(en)
            packed_int = struct.pack('i',result)
            client.send(packed_int)

         elif type(result) == float: 
           packed_float = struct.pack('f', result)
           client.send(packed_float)

   client.close()

s.close() 