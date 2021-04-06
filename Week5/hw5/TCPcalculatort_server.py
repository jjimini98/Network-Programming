from socket import * 

def calculator(sentence):
   sentence = sentence.split(" ") 

   if sentence[1] == "+":
      return int(sentence[0]) + int(sentence[2])  
   
   elif sentence[1] == "-":
      return int(sentence[0]) - int(sentence[2])
   
   elif sentence[1] == "*":
      return int(sentence[0]) * int(sentence[2])

   elif sentence[1] == "/":
      return format(int(sentence[0]) / int(sentence[2]), ".1f")
   


s = socket(AF_INET , SOCK_STREAM)
s.bind(('',3333))
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
         en = (result).to_bytes(4,'big')
         client.send(en)

   client.close()

s.close() 