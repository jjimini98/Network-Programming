from socket import *
import struct
#클라이언트 소켓 생성 및 서버의 소켓과 연결
s = socket(AF_INET , SOCK_STREAM)
s.connect(('localhost', 3331))


while True:
   user_input = input("계산 식을 입력하세요: ")
   if user_input == "q":
      break 

   # 서버로 계산식 전송   
   s.send(user_input.encode())

   #서버에서 계산된 값을 받기)
   result = s.recv(1024)
  
   # if int(struct.unpack('i',result)[0]) == True:
   #    print("Received Messages : " , struct.unpack('i',result))
   # else:  
   re = struct.unpack('f',result)
   print(re[0])
   # print("Received Messages : ", int(re[0]))

   print("Received message : ", int.from_bytes(result,'big'))
   
s.close()