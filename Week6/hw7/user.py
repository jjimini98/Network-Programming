# 얘가 서버의 역할 
# 만약에 input으로 1을 입력  -> device1과 연결 -> request 메세지 보내기 

from socket import * 
import time
import sys


BUF_SIZE = 1024
LENGTH = 20 
s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',80))

print("User is running")
user_input = input("어떤 디바이스와 연결할까요? :")

if user_input == "1":
   s.send('Request'.encode())
  
   result = s.recv(1024).decode()
   result = result.split(" ").remove('')
   
   file = open("data.txt" , 'wb')
   for x in result:
      file.write("{}{}{}{}".format(time.strftime('%c', time.localtime(time.time())) ,":  Device 1 :" ,x , "\n")
      # print("{}{}{}{}".format(time.strftime('%c', time.localtime(time.time())) ,":  Device 1 :" ,x , "\n")
