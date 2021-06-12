import selectors
from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',9999))

while True:
    number = input("Message to send: ")
    s.send(number.encode())
    msg = s.recv(1024).decode()
    print(msg)

