from socket import * 
import time
import sys

BUF_SIZE = 1024
li = []

print("User is running")
user_input = input("어떤 디바이스와 연결할까요? :")

if user_input == "1":
   s = socket(AF_INET,SOCK_STREAM)
   s.connect(('localhost',80))
   s.send('Request'.encode())
   
   msg = s.recv(1024).decode("utf-8")
   msg = msg.split(" ")

   
   file = open("data.txt" , 'w')
   for x in msg:
      if x == '':continue
      else : file.write("{}{}{}{}".format(time.strftime('%c', time.localtime(time.time())) ,":  Device 1 :" ,str(x), "\n"))
   print("completed")
   
   file.close()
   s.close()

elif user_input == "quit":
   s.send("quit".encode())
   sys.exit()


elif user_input == '2':
   t = socket(AF_INET,SOCK_STREAM)
   t.connect(('localhost',81))
   t.send('Request'.encode())
   
   msg = t.recv(1024).decode("utf-8")
   msg = msg.split(" ")
   
   file = open("data.txt" , 'a')
   for x in msg:
      if x == '' : continue
      else: file.write("{}{}{}{}".format(time.strftime('%c', time.localtime(time.time())) ,":  Device 2 :" ,str(x), "\n"))
   print("completed")

   file.close()
   t.close()